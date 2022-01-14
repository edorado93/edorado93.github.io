---
title: "Fun with array rotations"
header:
  overlay_image: {{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/header.gif
  overlay_filter: 0.5
  og_image: https://og-image.vercel.app/Fun%20With%20Array%20Rotations.png
excerpt: "Rotate an array, they said. It will be fun, they said."
date: September 17, 2018
show_date: true
toc: true
toc_label: "Content"
toc_sticky: true
tags:
  - Competitive Programming
  - Arrays
---

Arrays are one of the most versatile data structures out there. Arrays form the basis of so many applications and numerous algorithms and data structures are based on them.

For e.g. the [binary search](https://www.geeksforgeeks.org/binary-search/) algorithm works the way it does because the array data structure provides us with **_random access_** of the contents. If we take away the random access, we can’t execute the famous binary search algorithm with the same time complexities as before.

Similarly, we have the [priority queue](https://www.geeksforgeeks.org/priority-queue-set-1-introduction/) data structure which is again based on the array representation of a complete binary tree and the heap in itself is a root of a so many applications out there.

This particular article will deal with [programming](https://hackernoon.com/tagged/programming) problems related to **rotation in arrays and strings.** This is a fairly interesting domain of problems and we will look at a bunch of different problems based on the concept of rotation in the arrays.

Before starting off with the actual problems, let us first look at some examples of rotations and try and answer the following questions about rotations:

1.  What is a rotation ?
2.  How many rotations are possible for an array containing N elements ?
3.  What is the time complexity of rotating an array by one element ?
4.  Some [Python](https://hackernoon.com/tagged/python) magic to implement rotations.

## What is a rotation?

The diagram below will make it fairly clear as to what rotation is actually.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img1.png" alt="">
</figure>

Essentially, we remove the first element of the array and we place it in the end and we shift all of the remaining elements one step to the left. This is an example of left rotation.

Similarly we can have right rotation.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img2.png" alt="">
</figure>

## Number of Rotations?

The diagrams above make it pretty clear. Whether we have left rotation or right rotation, for an array of N elements, we will have N possible rotated arrays (including self).

## Time Complexity of Rotation?

Essentially what we do when we rotate an array is we remove the first element (considering we are talking about left rotation) and we shift **all of the remaining elements** one place to the left and finally we insert the element we removed from the first location at the very end of the array.

Since every time we have to do a rotation step, be it left or right rotation, the remaining N-1 elements have to be **shifted** as well to accommodate the rotation, the time complexity of this operation is **O(N).**

## Python Magic! 🧙‍

There are many ways we can go about this. We will only showcase methods for doing left rotation and the right rotation can be achieved in similar ways. So that is left as an exercise for the reader.

<script src="https://gist.github.com/edorado93/86843f5fcab64edb03c568b1dc16d92f.js"></script>

This is the most basic way of implementing one step of left rotation on a given array. We simply place the first element in the very end and before we do that we shift each of the remaining elements i.e. starting index 1 (for a 0 based indexing of the array), one step to the left.

This approach actually ends up modifying the underlying array. A lot of times we are only interested in the rotated version of the array or we are interested in all of the rotations of the given array, however, _we don’t really want to modify the underlying array_. You can say that the given array is a read only data structure.

If you notice carefully, in order to do left rotation for the Nth time, you would need the result of the previous rotation. So, for e.g. if the original array given to us was `[1,2,3,4,5]` and you follow the method listed above, after one rotation this would become `[2,3,4,5,1]` and then we can perform one more left rotation on this and get `[3,4,5,1,2]` .

By following the above method, it’s really difficult to obtain the array that remains after N left rotations.

Let’s look at an interesting way using which we can achieve this.

<script src="https://gist.github.com/edorado93/999c7f812a456965de438df23d201769.js"></script>

The trick here is the **modulo** operation. If you notice the rotated arrays, its like the starting point for the rotated array is actually some index `i` in the original array. This index `i` can be determined by the number `N` which represents the number of rotations we want to perform on the given array and then return the result.

Also, as you can imagine, N can be large as well. It can be larger than the length of the original array. However, after a certain point of time, the rotated array start to **repeat itself**. So, for an array of size N, after N-1 rotations, the next rotated array we get is the original one.

To understand why the modulo operation here works, have a look at the diagram below which shows a few rotations.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img3.png" alt="">
</figure>

Hope this diagram gives you enough clarity as to why we can simply do the modulo operation and we can directly get the array after N rotations have been performed on it.

Instead of writing the code like it has been shown in the code snippet earlier, we can also have a one liner for this in Python.

<script src="https://gist.github.com/edorado93/b4ad60251d88c10292733c18a0f7f833.js"></script>

Now that we have a sense of rotations and we know how to play around with our array, we can finally look at some interesting problems centered around the concept of rotating an array.

## Rotate Strings

Suppose you are given [two strings](https://leetcode.com/problems/rotate-string/description) A and B, which may or may not be of equal lengths 😛 (did you miss this ?), and we are to return true if any specific rotation of the string A can give us the string B.

In the diagram below we consider two strings `A = abcde` and `B = cdeab` and after two rotations the string A becomes equal to the string B. So in this case we return `True`

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img4.png" alt="">
</figure>

A simple check that will definitely return `False` is if the lengths of the two strings are different. In this case no matter what rotations we do, the strings can never be equal.

A very naive way of solving this problem is to find out all the rotations and then do string matching with the string B to see if the two strings become equal. We’ll look at the solution first, then we’ll see it’s complexity analysis and finally we will look at how well it fares among other solutions on the [leetcode](https://leetcode.com/) platform.

<script src="https://gist.github.com/edorado93/c9ba2f37d3f3612ccb7ab95b11240927.js"></script>

**Time Complexity:** `O(N²)` because for every rotation we do a string matching of two strings of length N which takes O(N) and we have O(N) rotations in all.

**Space Complexity:** `O(N)` because we create a new list per rotation.

On the leetcode platform this solution performs poorly as expected.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img5.png" alt="">
</figure>

It turns out that we can do better than this.

> The idea here is to append the string A to itself and then check if the string B is a substring of this extended string A + A

Why do we do this you might ask?

Well, it turns out that if we append a given array / string to itself, the resultant array or string covers all of the rotations of the original array. Let’s have a look at the diagram below to understand how this concatenation operation effectively yields all possible rotations. The string we will consider for this diagram below is `abcde` and so after concatenating this string with itself we get `abcdeabcde`

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img6.png" alt="">
</figure>

Figure showing all possible rotations for string “abcde” covered by “abcdeabcde”

Now if the string A or any rotation of A does in fact equal the string B, then the string B would be a substring of this enlarged string 2A.

**Time Complexity:** `O(N)` because all we are doing is string matching between a string of size N and another one which is 2N.

**Space Complexity:** `O(N)` because we have to create a new string of size 2N to accommodate this enlarged version of the string A.

This algorithm is much faster than the previous one and much shorter to implement as well. It’s a one liner in Python 🙈.

<script src="https://gist.github.com/edorado93/89dfb65f8bddee1373a4a149a2f57288.js"></script>

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img7.png" alt="">
</figure>

I’d say that’s fast enough!

Let’s move on to another interesting problem that seems simple enough but has a bunch of caveats to consider before we get the perfect solution.

## Minimum in Rotated Sorted Array

Let's take a look at another interesting problem from [leetcode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/).

So the question simply asks us to find an element in an array that is

* sorted,
* rotated and apparently
* doesn’t contain any duplicate elements.

A very brute way of solving this question is to search the entire array and find the minimum element. This approach would simply ignore the fact that the given array is sorted and this is the naive approach to solve this problem. So first let us look at a simple linear search based solution for this problem.

<script src="https://gist.github.com/edorado93/274079fcb8739be1908df05f14110ab4.js"></script>

**Time Complexity:** O(N) if there are N elements in the given array.

**Space Complexity:** O(1)

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img8.png" alt="">
</figure>

This is actually interesting. An O(N) solution gives us the best execution time on leetcode. However, it turns out that we can do way better than this as far as the asymptotic complexity is concerned.

The fact that the given array is sorted is a huge hint in itself. Since the array is sorted and we are to find an element in the array, we can use the binary search paradigm.
{: .notice--info}

However, the array is rotated. So simply applying the binary search won’t work here.

In this question we would essentially apply a modified version of binary search where the `condition` that decides the search direction would be different than in a standard binary search.

In a standard binary search algorithm we do the following

```
1. while left <= right  
2.     mid = (left + right) / 2  
3.     if element == middle element:  
4.         return mid   
5.     elif element < middle element:  
6.         move to the left i.e. [left, mid - 1]  
7.     else:  
8.         move to the right i.e. [mid + 1, right].
```

Since the given array is sorted, we can definitely apply the binary search algorithm to search for the element. The only thing is, that the elements have been rotated and that is something we have to account for.

How do we check if the array is even rotated or not in the first place?

If the array is not rotated and the array is sorted in ascending order, then

```
last_element > first_element
```

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img9.png" alt="">
</figure>

In the above example `7 > 2`. This means that the array does not have any rotation. In this case we can simply return the first element of the array as that would be the minimum element.

However, if the array is in fact rotated, then there would be a heartbeat formation happening somewhere in the array. Let’s look at what we mean by a heartbeat formation.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img10.png" alt="">
</figure>

If you look at the elements of the array above, they are in increasing order as expected (because the array is sorted in ascending order). However, after the element 7, there’s a sudden drop and then the values start to increase again. This is the heartbeat structure we are talking about.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img11.png" alt="">
</figure>

In the array given above `3 < 4`. Hence the array is rotated. This happens because the array was initially `[2, 3 ,4 ,5 ,6 ,7]`. But after the rotation the smaller elements`[2,3]` go at the back. i.e. [4, 5, 6, 7, `2, 3]`. Because of this the first element `[4]` in the rotated array becomes greater than the last element.

The heartbeat structure that is evident from the question means there is a point in the array at which you would notice a change. This is the point which would help us in this question. We call this the `Inflection Point`.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img12.png" alt="">
</figure>

An important property of the inflection point that would be critical in solving this question is:

> All the elements to the left of inflection point > first element of the array.  
> All the elements to the right of inflection point < first element of the array.

Let us now look at the algorithm to solve this question before looking at the implementation.

1. Find the `mid` element of the array.
2. If `mid element > first element of array` this means that we need to look for the inflection point on the right of `mid`.
3. If `mid element < first element of array` this that we need to look for the inflection point on the left of `mid`.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img13.png" alt="">
</figure>

We stop our search when we find the inflection point, when either of the two conditions is satisfied:

→ `nums[mid] > nums[mid + 1]` Hence, `mid+1` is the smallest.

→ `nums[mid - 1] > nums[mid]` Hence, `mid` is the smallest.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img14.png" alt="">
</figure>

<script src="https://gist.github.com/edorado93/4912438b127ef4f46140c419e62c4304.js"></script>

**Time Complexity:** `O(logN)` because all we are doing here is relying on our good friend, binary search and thus making use of the sorted nature of the original array.

**Space Complexity:** `O(1)`

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img15.png" alt="">
</figure>

Can’t do better than that now, can we ? 😉

The big catch in this problem is that there are no duplicate elements in the array. What if there are duplicate elements in the array ? Can we still follow a similar approach to solve the problem?
{: .notice--danger}

The answer to this question is yes and no. The same concepts that we discussed above apply to the this modified version of the problem as well. However, the time complexity is no longer guaranteed to be O(logN). Look at the following examples.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img16.png" alt="">
</figure>

The two cases mentioned below are easier to solve because the middle element is different from the first and the last elements and can help direct the binary search (although you’d get stuck with a 4 as the mid point further down the binary search).

The point being is that since duplicate elements are allowed here, it is possible to have a scenario where:

```
leftmost element == middle element == rightmost element
```

and when this scenario takes place, how do we decide what direction we need to move towards. There is no possible way for us to know the direction that can be ignored by the binary search algorithm. So, we would have to try and consider both as possible candidates and process them and in case all of the elements are the same in our array i.e. `[4,4,4,4,4,4,4,4]` then we would eventually end up processing each of the elements one by one.

Therefore, with a heavy heart 😢 we have to conclude that there is just no way to get a guaranteed O(logN) complexity algorithm on this question. The worst case time complexity of a modified version of the binary search algorithm we looked at above would be O(N).

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img17.gif" alt="">
</figure>

Let us move on to the final question for this article and it is going to be a blockbuster one. Trust me!

## Orderly Queue

Take a look at the problem statement [here](https://leetcode.com/problems/orderly-queue/description).

Let’s look at some of the possible string rotations first before getting to the solution. The string we will consider is `baaca` and K = 3 that means we can select *any* of the first three characters and then remove it from its location, add it to the very end and finally shift all the characters one position to the left to accommodate this new element in the end.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img18.gif" alt="">
</figure>

Assume the string has the following characters: `a[0], a[1], a[2] … a[n-1]` and we want to swap some position i (i >= 0 && i < n — 1) with position i+1, or swap a[i] and a[i+1]. The claim is that we can achieve this for any two adjacent elements in the string by using rotations on the string. e.g.:- Say the string consists of 5 characters and we want to swap `a[2] and a[3]` , here’s how we can achieve this with array rotations.

```
a[0], a[1], **a[2], a[3]**, a[4], a[5]     ROTATE around first element
a[1], **a[2], a[3]**, a[4], a[5], a[0]     ROTATE around first element
**a[2], a[3]**, a[4], a[5], a[0], a[1]     ROTATE around **second** element
**a[2],** a[4], a[5], a[0], a[1], **a[3]**     ROTATE around **first** element
a[5], a[0], a[1], **a[3], a[2],** a[4]     ROTATE around first element
a[0], a[1], **a[3], a[2],** a[4], a[5]     ROTATE around first element
```

You can try playing around with this idea, but essentially we can swap any two adjacent elements in the given string by performing multiple rotations in the manner shown above.

> Since we can swap any two elements, we can perform **Bubble Sort!**

The bubble sort algorithm essentially involves comparison amongst adjacent elements for the purpose of _bubbling up/down elements to their respective positions in the array._

Thus we have achieved swapping of chars a[2] and a[3] without disturbing ordering of other characters (similarly this can be done for any pair of adjacent indices).

Therefore, if K > 1 in the question, we can essentially perform the bubble sort algorithm by using rotations and eventually the smallest lexicographic string that we would get would be the original string sorted in ascending order.

## What about when K = 1?

In this case we don’t get that much freedom in “choosing” which element to move to the back of the array. In this case we have to look at all of the possible rotations of the original string and return the one that is lexicographically the smallest one.

If you remember correctly, the number of rotations for a string of size N are N. So, when K = 1, we would have to look at all of the array’s rotations (remember the *mod* method or *concat* methods we discussed in the article to get all rotations?) and obtain the smallest one lexicographically.

Let’s look at the implementation even though it is a very small one.

<script src="https://gist.github.com/edorado93/7f81dc1c7ede45e3bccec6ef3d436ba4.js"></script>

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img19.png" alt="">
</figure>

**Time Complexity:** `O(NlogN)` because we are sorting the string for K > 1

**Space Complexity:** `O(N)` because if K = 1, then we create S+S which is O(N) space allocation.

That’s it for this article. Hope you had a fun time learning rotations in arrays and I hope you were able to grasp all of the concepts that we discussed here.

> All Hail Coding…

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/array-rotations/img20.gif" alt="">
</figure>
