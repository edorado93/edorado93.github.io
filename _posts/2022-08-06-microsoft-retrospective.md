---
title: Life of a Software Engineer at Microsoft
header:
  overlay_image: https://cdn.hashnode.com/res/hashnode/image/unsplash/_g1WdcKcV3w/upload/v1655962322241/cldNadbMg.jpeg
  overlay_filter: 0.5
  og_image: https://og-image.vercel.app/Life%20of%20a%20Software%20Engineer%20at%20Microsoft.png
  collection: blog
excerpt: A retrospective of my time as a software engineer in the Azure DNS team at
  Microsoft.
date: August 06, 2022
show_date: true
toc: true
toc_label: Content
toc_sticky: true
tags:
- Software Engineering
- Interviews
- Retrospective
applause_count: 0
---

Back in 2019, a few months before joining Microsoft, one of my daily activities used to be searching "a day in the life of" videos on Youtube. I was obsessed with how the Microsoft campus looked and what the NEO (new employee orientation) entailed.

Back then we didn't know COVID existed so exploring the campus, the cafes, the office buildings, and actually meeting new engineers was all the rad.

I ended up spending almost 3 years at the company, within the same team I joined in 2019. This post is almost 2 months late now, mostly because of my supreme laziness! 

![snorlax_by_andrea455_dakdt8o-fullview.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1655963036945/LGuxpQEi8.png)

If you've stumbled upon this post, welcome! This is a recollection of my time as a Software Engineer within the Azure DNS team at Microsoft. During this time, I went through 2 different promotions and a few "above-and-beyond" reward cycles. 

## What's in it for me, the reader?
Great question! Personally, if I were you and I had a few years in the industry already, I'd skip over to the stats section to see some fun charts and observations. 

That being said, if you're new to the industry and are either starting out on a new path as a Software Engineer or have 1-2 years of experience, the retrospective and the general guidelines might be of some merit.

Without further adieu, let's get started. As I mentioned before, I started out with Microsoft back in June 2019 and joined the DNS team under the Networking organization for Azure. Let's chat a bit more about the team.

## The team!

DNS - Domain Name System. If you wanted to explain it in CS-101 terms, you'd say it's just a cache. 

![dns-1.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1656046103617/B-qLVd--H.png)

There's not just one team that powers the DNS offering at Microsoft. There's a whole bunch of them powering different components of the DNS stack. The team I worked on was the *authoritative DNS* team i.e. the machines responsible for providing an authoritative answer for each DNS query.

### The tech stack 🤓
Most of the code was either in C++ or C#. This was all pretty new to me coming from a Python world (during my Master's and my previous job which mostly involved Python and Java).

That's pretty much the only part that the outside developer community would be familiar with as far as the tech stack is concerned. As with most companies operating at Microsoft's scale, most of the tools and frameworks are built in-house. 

Some of them get re-branded and are provided as customer offerings. However, you as the engineer get to experience these cutting-edge frameworks and tools first-hand.

Not just that, you even have the luxury of reaching out and interacting with the creators of these frameworks and services!

From monitoring services to logging frameworks to the machines running our code, everything was developed in-house. 

![1631050856_1075100.gif](https://cdn.hashnode.com/res/hashnode/image/upload/v1656047205952/_d5rH8DY9.gif)

### Pros and Cons of working on a Tier-0 service

>“There are only two hard things in computer science: cache invalidation and naming things.” -- Phil Karlton

DNS at its essence is a cache. It is a distributed cache that maintains a key-value mapping from some name to an IP address. There is a lot going on behind the scenes, but at its core, this is what we maintain. 

A DNS service is what we call a tier-0 or ring-0 service. That means we cannot have our service rely on any higher-level services like tier-1 or tier-2. 

The main disadvantage of this situation is that we cannot use all the cool technology (think Azure VMs) for building, running, and maintaining a tier-0 service since a VM deployment lifecycle depends on DNS provisioning in some manner. 

On the other hand, maintaining [5 9s of availability](https://www.techtarget.com/searchnetworking/feature/The-Holy-Grail-of-five-nines-reliability#:~:text=Five%2Dnines%20availability%20%2D%2D%20or,usually%20defined%20as%20a%20year.) for a tier-0 service, especially one like DNS that has a humongous QPS (think millions of queries per second) is a huge responsibility! 

## Well, go on, tell us what did you learn in all these years? 
Okay Okay! Jesus Christ, you're impatient. As mentioned before, I ended up spending about 3 years in a single team within Microsoft. It's not an awfully long tenure. It's a pretty short-term stint for an engineer at a place like Microsoft. 

I'll cover my reason for looking to switch in a separate post. For now, let's dig into things I'd probably tell my 20-year-old self (and along with that, all the young engineers out there who are just starting out).

### You're background till now doesn't matter!
This is one of the most important things that I've had the "privilege" to learn in my career so far. Your schooling, education, and I'll even go out on a limb and say, your previous work experiences don't matter as much as you think.

There are a lot of opinions (and facts too!) about the ease of hiring from Tier-1 colleges and universities around the world. That is very true. 

>However, not everyone in the world can make it to that top university, college, or high school. Regardless of where you come from and what your educational background is, passion and hard work end up being the defining factor that separates a 10X engineer from an average software engineer.

I've had the privilege of studying under some great professors and mentors. However, if I didn't put as much effort and heart into what I do, I'm not sure my career path would look even remotely the same.

* If you love building software,
* Are willing to put in the hard work to catch up and stay relevant in our industry,
* And are really looking to contribute to this vast field (with a bazillion opportunities), 

you'll be just fine!

![cf9f69df5c7914857fb4991b42eded02.jpeg](https://cdn.hashnode.com/res/hashnode/image/upload/v1656304114249/oIsaaYvEF.jpeg)

### It's tough to land an interview
The internet is full of advice on how to prepare for cracking software engineering interviews involving coding and system design elements. A lot of set patterns for preparation are out there. 

But, what we don't really talk about as much is the ability to land an interview. 

>What if you spend 6 months, burning the midnight oil, preparing for landing your dream job at some XYZ company, and they never even select or shortlist your resume?

Your resume is one of the most important pieces of your online profile that can help land that first email/call with a recruiter or an engineering manager. Again, a lot has been said and a lot of advice is out there on how to improve your resume so not going to add to that information here. 

>What I'll mention here (or rather, really stress!) is that just applying for a job on a company's website is not enough these days.

A company like Google or Microsoft receives hundreds of thousands of applications in a week. The competition is too tough there. Everybody is trying to make their way through the funnel and get a chance to even interview these big software giants. 

>What a lot of engineers don't do, is try to build a personal connection with recruiters or engineers or engineering managers.

Building personal connections, in my experience, is much more effective to landing interviews than merely applying on job forums. If you feel your profile really fits a particular role at a company you're interested in working at, try reaching out to some engineers or even managers in that company.

* Be polite with your introductions
* Share your resume
* Give a TL;DR as to why you might be a good fit for a role in the company and briefly mention your industry experience.
* Most importantly, thank them for the time they spent reading your message/email.

Even if one of the people you reach out to in this manner replies back, they would help short-circuit the application process and help you land that interview even before you can process happiness from their reply!

### It's ok to feel like an imposter
Preparing, interviewing, negotiating, and finalizing an offer is just the tip of the iceberg. The excitement of getting into a great company will only get you so far on the job.

My first month or so was a whirlwind of information and acronyms (Microsoft is pretty infamous for them!). Most importantly, I did feel like an imposter, a lot during the initial weeks or so.

>What you need to understand is that it is perfectly ok to feel like an imposter. You simply need to redefine your expectations from the role. Instead of trying to be a rockstar on the team from day-1, you need to act like a sponge and be a very good sponge for a long time.

If you understand and accept your role as the sponge on the team, you won't feel like an imposter. You simply need to accept the fact that every other engineer who has more tenure than yourself on the team is more experienced and probably smarter than you when it comes to doing tasks on that team.

![Screen Shot 2022-06-27 at 11.17.08 PM.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1656397064523/GAhiEjn_R.png)

### Asking for help is not a crime
You might get mixed takes on this one. However, my personal opinion is that we should not be shying away from asking for help. When I started working in the team, my ego always dictated the amount of time I spent trying to solve a particular problem. As a young engineer, completely new to the tools and infrastructures in a company as large as Microsoft, running into issues became second nature. 

After a couple of fiascos where hours or even days went by and I was stuck trying to figure out a problem only to be helped by a senior engineer in a matter or minutes, I realized that there needs to be an intricate balance between going down the rabbit hole and asking for help from others. 

>Doing due diligence, whether it's for reading a piece of code or reading some documentation, is very important for an engineer's growth and learning. However, after a point of time, we start to go down the rabbit hole and stop being productive at all. At that time, we should just reach out to senior engineers, our manager, internal slack channels (teams channels for Microsoft) and any other avenues you can find. 

Communication is the key, especially to being an effective engineer in a remote-first world during the COVID era. 

### Chasing Impact!
Say you've joined a great engineering team and have started to settle in. The work you're getting is great and is really satisfying your engineering acumen. After a year or so, things start to stagnate a bit. Not in terms of what work you're getting to do, but in terms of your own learning experience.

At this point, you're mostly familiar with the technology being used inside the team and so, there's no new learning opportunity there. The team is relatively stable and is hence, not facing any scalability challenges. The new work that is coming your way is mostly along the lines of what you've dealt with in the past. 

At this point, you might get an urge to explore other avenues since you don't see any new work coming your way. As a young engineer, it is easy to get "bored" of the work you're doing. 

![60efb75ab39a8f3dbc69dedb_plateau.jpeg](https://cdn.hashnode.com/res/hashnode/image/upload/v1657323500315/VbcqPjP4l.jpeg)

At this point, what really separates a senior engineer from others is the perseverance and the ability to think about systems from a holistic perspective. When you join a company as a new engineer, you expect to be handed new work during the initial few months. If you're just starting out in the industry, you can expect to be handed new work 90% of the time during the first couple of years. 

However, for you to really transition into a senior engineer on the team, you need to find opportunities for improvement yourself. After a year or so when you get a decent idea about the codebase and the tools and processes on the team, you can start thinking about the pain points that nobody is prioritizing on the team. Things like:

1. The extremely slow build times. 
2. That broken suite of integration tests that nobody wants to look into.
3. Absence of good troubleshooting guides for on-call engineers.
4. A suboptimal design you notice for that service which has extremely high latency which is going un-noticed.
5. Absence of good dashboards and metrics which can help provide visibility into how the services are doing.

The list goes on and on and the more ownership you take, the more work will come your way and this is one of the sure-fire ways of becoming an SME -- a subject matter expert on the team.

Everybody wants to work on that big swanky feature and build a system that maybe handles millions of QPS with 5-9s of availability and millisecond latencies. However, only a select few get to do that. In order to reach a point where you have the luxury of selecting what you want to work on, you have to work on improving the peripherals for your team. 

A lot of low hanging fruits always exist within any team that are free to pick up and can be worked on the side. The best part is, they have huge scope for impact which is the one true metric that comes in handy when there are talks about promotion!

### Dealing with a conflict is a key skill
The engineers and PMs on your team come from a diverse set of backgrounds and work experiences. It is only natural that you might run into conflicts and difference of opinion with them especially if you're continuously collaborating on features with multiple engineers. 

How you handle conflict is yet another invaluable skill that you must learn during your time at a company. There were multiple instances where my way of approaching a problem was completely opposite to that of another engineer(s). In these times, there are multiple ways you can go about this situation:

1. Go on an all out war and declare that what you're saying is absolutely right and ignore what the other individual has to say. *Don't do this, it doesn't work out!*
2. Try and understand the reasoning behind the other points-of-views on the table. Even though people may present views that do not align with your thought process, always try to understand the reasoning behind the other viewpoints. Maybe there are things you're completely ignoring and if that is the case, you can learn a thing or two in the process. 
3. Completely succumb to what a more experienced engineer has to say considering they are .... senior? This might be the most common things we as engineers tend to do. However, every once in a while, make sure to put your point across, especially if you feel it has some merit after listening to what others on the team have to say. It not only shows good communication and listening skills, but you might end up providing a unique perspective that others might have missed.

### Lastly, make sure you have fun!
This one goes without saying, have fun while you're at it!

The grass always "seems" greener on the other side. Someone out there will always be earning more than what you are at the moment or doing better work than what you're doing. It is very easy to get bored and have that nagging feeling to switch too soon to get better work or to make more $$. 

>That being said, it takes time for a new engineer to really settle down on a team.

No matter your level i.e. Software Engineer, Senior Software Engineer, or a Staff Software Engineer, it takes time to get the ground running and really make an impact in the team. Also, your morale while you're working is more of a sine curve. 

Sometimes, the projects you're getting are really satisfying, both as an engineer and as a deliverable for the company/business unit. On the other hand, you might be doing shitty config pushes every now and then and not doing anything really productive.

The thing you have to remember is that our work is more of a marathon rather than a sprint! You need to to stick it our to really peak as an engineer within the team. 

At the same time, do remember that you're the best judge of what new work is coming your way (possibly) in the next year or so. If that is something that really throws you off and is not challenging at all, it's time to look elsewhere :) Again, this is more of a personal recommendation rather than a well defined standard. Everyone has their own timelines for when they start to look for a switch.

## Too much guidance, Sachin! 
Yeah, I do realize that this post might start to feel a little bit boring at this point. This later half of the post is going to be more "stats" heavy! Don't know what that means? Stick around to find out.

![giphy.gif](https://cdn.hashnode.com/res/hashnode/image/upload/v1657504059886/S1HvnI29g.gif align="center")

### My last day at Microsoft
I had this weird idea in my mind as to what I wanted to do on my last day at the company. We tend to forget most events in life as time goes on unless we have something to show for it or recall it. You'd probably forget that amazing road trip unless you keep an album for it containing all the fun memories. Even better if you wrote a blog about it to remind you of *what happens in Vegas stays in Vegas* moments. 

Similarly, I wanted to keep an account of sorts for myself as to what value I was able to produce as an engineer during my stint in the team. A lot of things cannot be accounted for. The things we can however take into account are your pull request data. At the end of the day, whether you're making bug fixes or adding new documentation, it ends up being managed by some sort of version control and you do have a PR to show for it. 

Now I didn't have the time to write a tool to parse all the PRs I had merged into various codebases over my 3 years time period. So, as an extremely smart engineer, I umm, uhh.

>Went ahead and made manual entries for all of them! 

Yep! I added data like 

* Number of inserts
* Number of deletes
* Lines of code changed and
* Number of comments
* Date when the PR was merged

to a Notion database, ***manually***.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1657504972874/yWkQu-RXi.png)

The data was too precious to let go. 

![giphy.gif](https://cdn.hashnode.com/res/hashnode/image/upload/v1657504894992/Wliz4aHnI.gif align="center")

I wanted to crunch some numbers using all of this precious information I had gathered and jot down some useful information for myself and for any other engineers out there. This is by no means any sort of a *10X engineer baseline* or something. This is simply the performance and outcome of my inputs over time at the company. This might look completely different for other engineers and and even if it looks completely same, they might be a whole lot more productive than myself. 

Remember, these metrics by no means represent the actual contribution that an engineer made within the team. The number of lines of code changed does not translate to impact. The time spent building those design documents, leading crucial meetings with multiple stakeholders, thinking through those gnarly edge cases is also what counts as great impact :) Unfortunately, that is not really tangible. 

So, here we are with some of the data I crunched from the stats I collected from my pull-requests over the years. Feel free to drop off and maybe read another fun post out there if this doesn't seem helpful :)

### Number of PRs 

Looks like I worked on and merged 310 pull requests over the 3 year period. 

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1657505574129/v2Fb5fhzE.png)

The distribution for the number of PRs over the years looks somewhat like this:

* 2019 --> 29
* 2020 --> 129
* 2021 --> 120
* 2022 --> 32

### How'd you do in 2019?

That's the year I had just joined the team. So it naturally took some time for me to settle down and try to understand the codebase, the deployment and release processes, and a bazillion set of tools we had to use on a day-to-day.

![abc (8).png](https://cdn.hashnode.com/res/hashnode/image/upload/v1657506931803/EQoreLgN_.png)

![abc (10).png](https://cdn.hashnode.com/res/hashnode/image/upload/v1657507167611/qHMz_vuBI.png)

I was really lucky to be able to work on a lot of bugs that we were facing in our production services, early on in the team. Our on-call load was pretty bad those first few months when I was on the team. That is something that turned out advantageous for me since it presented a unique opportunity to understand the code and see how and where it's going wrong. 

The ability to correlate the logs and metrics with the code was a key debugging skill that I got to learn early on and it became pretty handy as the time went by. 

Something most engineers don't realize is that focussing on your on-call shifts is one of the best ways to make an impact. You get a unique opportunity to debug that nagging issue that has been raising hell recently and if you do get to figure out the root cause, you naturally get to lead the fixes for the same. That is precisely what I did during my first few months on the team.

Most of the changes in the graphs above are focussing on adding and improving our integration test suite and patching heaps of bugs in our code base. 

### What about 2020? 

Ah! The year we suddenly started working "fully remote"? No longer able to access all the perks and beautiful offices that the Microsoft headquarters had to offer. That was a huge mental shift for a whole lot of us not used to remote work yet. 

![abc (23).png](https://cdn.hashnode.com/res/hashnode/image/upload/v1659110159036/esw8H-FJi.png)

![abc (12).png](https://cdn.hashnode.com/res/hashnode/image/upload/v1657507849396/nGdyAxQYb.png)

Well, the piechart now contains changes over each quarter of the year as opposed to each month. The reason for that is my lack of knowledge in visualization charts. If I tried to display the data for each month, I ran into overlapping labels which was looking weird. Additionally, the working pattern remains interesting even if we visualize things over each quarter. The second and the third quarter seemed to be the ones where the most PRs were raised. The last quarter is usually pretty chill given all the holidays and festivals. Additionally, it feels like a slumber coming out of the holiday season and into the new year during the first quarter of the year. 

### 3000 changes in a single PR?

March, April, and May seems to be the months where I made most of the changes for the year. There were a couple of features that I had been working on for a month or so before things got shut down. They eventually came to conclusion during March and April and had over 3k inserts. 

There are multiple ways of working on big features. For these specific ones I had one-boxed all the changes in a single PR. That means all the code, configuration, and tests were included in a single pull request. The advantage of doing things this way are that it's easy to figure out bugs in the future and revert in a single operation if needed in the future. 

The biggest disadvantage however is for the reviewer. They won't have the time and the patience to go through a PR that has 3000 or inserts. They would have to understand and spend a substantial amount of time to really review the PR. In this case, it might be the case that the reviewer either approves the pull request without doing a diligent review and this can turn out to be dangerous as some bugs might go unnoticed. On the other hand, the reviewer might not be able to get to the review for extended periods of time thus delaying the overall feature rollout.

Looking back, I'd probably break the feature down into smaller byte-sized chunks and have multiple pull-requests instead.  

### Slogging towards year end eh?
Not intentionally at least. The tail ender months tend to be the ones with a lot of festivals and a bunch of public holidays. So, we usually blocked out any production rollouts during this time. That being said, these were also the months where we focussed on other quality improvements in our tools and processes. 

Rather than working on a big feature, we spent time working on improving things like:
1. Dashboards.
2. Build and deployment times. 
3. Removing code smells.

Truth be told though, I usually traveled back to India to be with family during this time and that also caused a dip in the overall efficiency owing to the huge time difference in working hours. 

## 2021, the penultimate year

This year seemed to follow a similar trend in terms of number of PRs that I worked on during the initial months of the year. March, April, and May seem to be the focus months. 

![abc (24).png](https://cdn.hashnode.com/res/hashnode/image/upload/v1659110236467/OwTtAZY9r.png)

![abc (16).png](https://cdn.hashnode.com/res/hashnode/image/upload/v1657986999160/HWzYIPMA3.png)

This is pretty unusual if you ask me! The second quarter seems to be the one with the maximum set of PRs overall. It's difficult to recall what went down exactly during those months since I don't have access to the PRs themselves. But the contribution pattern of April, May, June being the best months of the year seems to be consistent across the years for me personally. 

In all honesty though, I also feel that living in a place like Seattle, the months of April and May bring about the onset of Spring and you start to get slightly better weather and slightly longer days. That is also something that boosts my spirits and it would be the same for a lot of people. 

An upside of working from home has turned out to be the extreme flexibility in terms of working hours. There have been times where I was able to "sneak" out early morning, do a hike and come back late in the afternoon and then work rest of the day. This might not have been possible with the requirement of going to the office. 

>This is however, a double edged sword. A lot of people in the tech industry, who are working from home during, tend to lose track of time while working. The sense of "working hours" is now very bleak and due to that, a lot of engineers might feel that they end up working more than they used to when working from office. 

Be mindful of your work life balance, especially when working from home!

## 2022, the last year

I left my job at Microsoft by the end of May, 2022, just shy of that 3 year mark at the company. The process of interviewing was rigorous and looking back, I could have skipped a bunch of interviews and been more selective. However, I had a lot of fun during my interview preparation which I began somewhere around February. 

Naturally, my work and performance suffered in comparison to previous years around this time. 

![abc (17).png](https://cdn.hashnode.com/res/hashnode/image/upload/v1657987119067/oL1kB59Jt.png)

![abc (18).png](https://cdn.hashnode.com/res/hashnode/image/upload/v1657987226071/0rIsZmzqj.png)

Interestingly though, I made quite a few changes towards the fag end of my time. As a matter of fact, there were 3 set of code changes with over 2000 inserts that I ended up testing and deploying during my last week. 

I had finalized an offer by the end of April and hence, I spent quite a lot of time trying to wrap up pending work items on my plate. I had a couple of big features that would get stalled in case I left them in a pending state. So, thankfully, I was able to wrap things up (no corners cut!) right before I switched. 

## Overall insert trends

Before wrapping up this long post, there are a couple of other interesting things that I want to document for my future self and for anyone who has been reading so far.

At the very beginning of this metrics analysis I had mentioned that I merged around 310 pull requests over the 3 year period that I worked at the company. That number might seem insignificant if I mention that these were all configuration changes or something like that (one liners essentially). 

On the other hand, this number might feel pretty darn good if I mentioned that 90% of the pull requests had at least 1000 inserts/deletes. 

>If you're thinking why do the deletes matter? Well, code cleanup is an important part of the overall code hygiene. The less code you have to maintain, less chances of you running into issues and easier things will be to debug. 

![abc (22).png](https://cdn.hashnode.com/res/hashnode/image/upload/v1657988650001/Ss_8vrifR.png)

* Between 10 and 100 inserts -- 122 PRs
* Between 100 and 500 inserts -- 71 PRs
* Between 500 and 1000 inserts -- 11 PRs
* More than 1000 inserts -- 13 PRs
  
This information is pretty significant because we can see that the big features i.e. the ones that tend to have a huge set of changes are few and far between. There were just 13 pull requests with more than a 1000 inserts.

Why is this information important you might ask? Well, it's important to understand that us engineers don't necessarily build infinitely scalable systems (or their parts) all the time. Such good and lengthy work comes with experience and also, there is limited opportunity for it. If there are multiple engineers who can work on a big ticket item, it is possible that the work might be split and you may not get to work on the "cool" stuff. 

## Wrapping up

That's a whole lot of data to consume for a reader in a single post. Frankly, all of these stats might not feel to relevant or important right off the bat to an engineer. As mentioned before, this is by no means a baseline or any ballpark that you should be striving by. This is simply a documentation on my behalf for future me, so that I can analyze these trends as I move along in my career and switch across various domains. 

It's a good idea to be looking at these metrics from time to time so as to get a holistic view of your overall contributions to the team over time. Usually, us engineers work from feature to feature and never dedicate time to look back at what was done in the past 6 months or 1 year (unless we're preparing that promo packet!). 

>Retrospective is a great tool for improving and paying attention to what is still missing and celebrating what has been working out well!

## So, what's next for me? 

If you've read so far, thanks! Hopefully, there was something useful in there for you. If my future self is reading this, hopefully, you're having a good laugh.

One of my primary aim for pursuing a Master's degree was to get a pathway into Machine Learning. I was privileged enough to not only pursue really good courses, but also work as a Research assistant in one of the best NLP and Vision labs across the country, the Information Sciences Institute, during my Masters. Unfortunately my role at Microsoft did not involve any sort of work along the lines of Machine Learning. So, I had to put this urge to work in this field on hold. 

When I started looking out for a new role, one of my primary motives was to search for opportunities that are not purely research based, but involve a good combination of Software Engineering and Machine Learning. Fortunately enough, I came across a wonderful opportunity at a company that was never even on my radar when I started searching for new roles!

As for my next gig, I bagged a unique opportunity to switch domain and enter the world of MLOps. My interviewing experience has also been quite the roller coaster ride and there would be a follow-up post documenting all of the experiences and preparation strategies that I followed. 

For now, I joined Etsy's Personalization organization as a Staff Machine Learning Engineer in the Computer Vision team. Quite the drastic jump coming from working on a Tier-0 service at an astronomical scale. 

![JoinedEtsy1.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1658128938565/BPd73KVL3.jpg)