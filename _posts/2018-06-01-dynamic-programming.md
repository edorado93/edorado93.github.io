---
title: "Change the signs, a Codechef Problem"
header:
  overlay_image: /assets/images/dynamic-programming/header.png
  overlay_filter: 0.5
  og_image: https://og-image.vercel.app/Change%20The%20Signs,%20A%20Codechef%20Problem.png
excerpt: "How to use dynamic programming to solve a competitive programming question."
date: June 1, 2018
show_date: true
toc: true
toc_label: "Content"
toc_sticky: true
tags:
  - Competitive Programming
  - Dynamic Programming
  - Recursion
---

If you’re a competitive programmer like I am, one of the best feelings in the world is seeing your program getting accepted on first try on one of the most famous programming platforms, [CodeChef](https://www.codechef.com/).

The [CodeChef May 2018 Long Challenge](https://www.codechef.com/MAY18) ended about an hour ago, and I decided to write this article as a post describing one of the questions in the competition.

Without wasting any more time, let’s get to it.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-programming/img1.png" alt="">
</figure>

## Unravelling the Problem Statement

Let’s look at some examples to better understand what the problem statement is asking for.

Consider the following number sequence.

```
4 3 1 2
```

Now the question asks us to perform a certain operation (possibly 0 times, leaving the sequence unchanged). We can negate a certain subsequence of numbers and get a new sequence.

```
-4 3 1 2  
4 -3 1 -2  
4 3 -1 2  
4 3 1 -2  
-4 -3 1 2 etc.
```

The question says that the resulting sequence should satisfy the following constraint:

**Note:** The sum of elements of any substring with length greater than 1 is strictly positive.
{: .notice--info}

Clearly, the following sequences are not valid:

```
-4 3 1 2  
4 -3 1 -2   
4 3 1 -2   
-4 -3 1 2   
-4 -3 -1 -2  
4 3 -1 -2
```

We only have 2 valid subsequences that can be obtained by performing the operation mentioned above. Note that we haven’t written down all the possible subsequences. That would be `2^n`, that is `16` in this case, because for every number we have two options. Either to negate it, or not.

So the two valid sequences are:

```
4 3 1 2
```

and

```
4 3 -1 2
```

The original sequence would always be one of the valid sequences as all the numbers in it are positive.

Now the question asks us to find the sequence with the minimum sum. So for the example we have considered, the sequence required would be `4 3 -1 2` .

## Would Greedy Work?

A greedy approach in this question would be that if it is possible to negate a number while satisfying the given constraints, then we should negate that number. This approach however, would not always give the right results. Consider the following example.

```
4 1 3 2
```

Here, it is possible to have these three valid sets of numbers:

```
4 1 3 2           4 -1 3 2           4 1 3 -2
```

Clearly, both the numbers 2 and 1 can be negated. But not both of them at the same time. If we negate a number greedily — that is, if a number can be negated, then we negate it — then it is possible that we might end up negating the number 1. Then you won’t be able to negate the number 2. This would give us a suboptimal solution.

So this Greedy approach would not work here. We have to try out a specific choice of whether to negate or not for a number and see what choice gives us the optimal solution.
{: .notice--info}

This smells like _Dynamic Programming_.

## Good ol’ Dynamic Programming

One of the most interesting algorithmic techniques out there, and possibly one of the most dreaded, is dynamic programming. This is the technique we are going to use to solve this particular problem.

Two of the most important steps in any dynamic programming problem are:

1. Identifying the recurrent relation.
2. Figuring out what to [memoize](https://www.interviewcake.com/concept/java/memoization).

The DP-based approach here is divided into two basic parts.

* One is the main recursion that we use to find out the minimum sum of the final set. Note, the dynamic programming is not directly used to obtain the final set, just the sum of the final set of numbers. So our dynamic programming approach would correctly find out the sum for the example given above as 8. `4 + 3 + (-1) + 2 = 8` .
* What we actually need is the final modified set of numbers where some (possibly none) of the numbers are negated. We use the concept of a parent pointer and backtracking to find out the actual set of numbers.

Let’s move onto our recursion relation for our dynamic programming approach.

Before describing the recursive relation an important observation to make here is that if a number has been negated, then any adjacent number to it can not be negative. That is, two adjacent numbers cannot be negative as that would give a substring of length 2 whose sum is negative, and that is not allowed according to the question.
{: .notice--info}

For the recurrence relation, we need two variables. One is the index number of where we are in the array, and one is a boolean value that tells us if the previous number (one left to the previous number) is negated or not. 

So if the current index is `i`, then the boolean value would tell us if the number at `i — 2` was negated or not. You will know the importance of this boolean variable in the next paragraph.

We need to know in `O(1)` if a number *can* be negated or not. Since we are following a recursion with memoization-based solution, whenever we are at an index `i` in the recursion, we are sure that the numbers to the right (`i+ 1` onwards) have not been processed up to this point. This means that all of them are still positive.

The choice of whether the number at index `i` can be negated is dependent upon the right hand side (if there is one) and the left hand side (if there is one). The right hand side is easy. All we need to check is if

```
number[i] < number[i + 1]
```

because if this is not true, then adding these two would give a negative value for the substring `[i, i + 1]` thus making it an invalid operation.

Now comes the tricky part. We need to see if negating the number at `i` will cause a substring of negative sum to the left or not. When we reach the index `i` in our recursion, we have already processed the numbers before it, and some might have been negated as well.

So say we have this set of numbers `4 1 2 1` and we had negated the first `1` and we are now processing the last number ( `1` ).

```
4 -1 2 [1]
```

The last number in square brackets is the one we are processing right now. As far as the right hand side is concerned, since there is none, we can negate it. We need to check if negating this 1 at index 3 (0 based indexing) would cause any substring to the left of ≤ 0 sum. As you can see, it will produce such a substring.

```
-1 2 -1
```

This substring would have a 0 sum, and that is invalid according to the question. After negating a subsequence of numbers, the substrings in the final set should have a sum which is strictly positive. All the substrings of length > 1.

We cannot apply the following approach here directly:

```
if number[i] < number[i - 1], then it is good to go on negation.
```

because, although `1 < 2` , if we negate that last 1 as well we will have an invalid set of numbers as seen above. So this simple approach or check won’t work here.

Here comes the boolean variable which tells us if, given an index `i`, the number at `i — 2` was negated or not. Consider the two scenarios.

* Yes, the number at index `i — 2` was negated like in the example just showcased. In that case, negation of the number at `i — 2` would have a capacity reduction for number at `i — 1`. In the example `4 1 2 1` , negating the 1 at index 1(0 based indexing) would reduce the capacity of the number 2 (at index 2) by 1. We refer to remaining values of numbers as capacities here. We need to consider this reduced capacity when performing the check to see if a number can be negated or not.

```
number[i] < reducedCapacityOfNumberAt(i - 1)
```

*  In case the number at index `i — 2` wasn’t negated, the number at `i — 1` is at it’s full capacity. The simple check

```
number[i] < number[i - 1]
```

would be enough to see if we can negate the number at index `i` .

Let’s look at the code for the recursion containing all the ideas discussed above.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-programming/img2.png" alt="">
</figure>

That’s all nice and dandy. But, this is just recursion, and the heading says dynamic programming. That means there would be overlapping subproblems. Let us look at the recursion tree to see if there are any.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-programming/img3.png" alt="">
</figure>

As you can see, there are overlapping subproblems in the recursion tree. That is why we can use memoization.

The memoization is as simple as:

```python
""" This comes at the top. We check if the state represented by the tuple of the index and the boolean variable is already cached """
if(memo[i][is_prev_negated] != INF)   
{  
    return memo[i][is_prev_negated];  
}  

# ...... CODE  

# Cache the minimum sum from this index onwards.  
memo[i][is_prev_negated] = min(pos, neg);

# The parent pointer is used for finding out the final set of #s  
parent[i][is_prev_negated] = min(pos, neg) == pos ? 1 : -1;
```

As pointed out earlier, this recursive approach would return the minimum sum of the set of numbers possible after making the valid set of modifications to them.

The question, however, asks us to actually print the final set of numbers that gives the minimum sum after making such modifications. For that, we need to use a parent pointer that would tell us at every index and boolean variable `is_prev_negated` ’s value as to what optimal action was taken.

```python
parent[i][is_prev_negated] = min(pos, neg) == pos ? 1 : -1;
```

So we simply store 1 or -1 depending upon if negating the number at index i (if possible!) gave us the minimum sum or if choosing to ignore it gave the minimum sum.

## Backtracking

Now comes the part where we backtrack to find the solution to our original problem. Note that the decision for the very first number is what propagates the recursion further. If the first number was negated, the second number would be positive and the third number’s decision can be found using `parent[2][true]`. Similarly, if the first number wasn’t negated, then we move onto the second number and it’s decision can be found using `parent[1][false]` and so on. Let’s look at the code.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-programming/img4.png" alt="">
</figure>

## A Better Approach

If you take a look at the space complexity of the solution suggested, you will see that it’s a 2 dimensional dynamic programming solution because the state of the recursion is represented by two variables i.e. the index `i` representing what number of the array we are considering and then the boolean variable `is_prev_negated` . So the space complexity and the time complexity would be O(n*2) which is essentially O(n).

However, there is a slightly better approach as well to solving this problem which involves using a 1 dimensional dynamic programming based solution.

Essentially, the boolean variable `is_prev_negated` is helping us to decide if we can negate a given number at index `i` or not as far as the left hand side of the array is concerned i.e. `all the numbers from 0 .. i-1` because the right hand side is anyways safe as all the numbers on that side are positive (as the recursion hasn’t reached them yet). 

So for the right hand side we simply checked the number at `i+1` but for the left hand side of index `i` we had to make use of the boolean variable `is_prev_negated` .

It turns out, that we can simply skip this boolean variable altogether and simply look ahead to decide if a number can be negated or not. Which simply means if you are at an index `i`, you check if that element along with the element at `i+2` have the capacity to swallow the element at `i+1` i.e.

```
numbers[i] + numbers[i+2] >= numbers[i+1  (SWALLOW)
```

If there is a such a possibility, then we directly jump to `i+3`if we negate element at `i` because element at `i+1` and `i+2` both can’t be negative in such a scenario.

In case the swallow condition is not satisfied and we end up negating the number at index `i` , then we would jump to index `i+2` because in any case, two consecutive numbers cannot be negated. So if the number at `i` was negated, then the number at `i+1` has to be positive. The swallow check is to see if the number at `i+2` would definitely have to be positive or if we can exercise the choice of whether to negate or not there.

Have a look at the code for a better understanding.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-programming/img5.png" alt="">
</figure>

Hence, just a single variable i.e. the index is used to define the state of the recursion. So the time and space complexity, both got reduced to half of what they were in the previous solution.

I hope you were able to grasp the working of the algorithm described above and how the dynamic programming technique fits into this problem. I think it’s an interesting problem, because you not only have to use dynamic programming but also the concept of parent pointer to retrace the steps through the optimal solution and get the answer required in the question.
