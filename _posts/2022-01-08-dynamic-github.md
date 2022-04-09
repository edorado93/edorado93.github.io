---
title: "Building a Dynamic Github profile with Github Actions"
header:
  overlay_image: /assets/images/dynamic-github/header.jpeg
  overlay_filter: 0.5
  og_image: https://og-image.vercel.app/Building%20A%20Dynamic%20Github%20Profile.png
  collection: blog
excerpt: Show off your Github activity, latest blogs, Spotify streams, and much more with dynamically updating GitHub Profile READMEs!"
date: January 08, 2022
show_date: true
toc: true
toc_label: "Content"
toc_sticky: true
tags:
  - Open Source
  - Github
  - Frontend
  - Github Actions
---

Hey y ’all, if you’ve stumbled across this post on Medium, just note that this was _originally_ posted on Hackernoon. If you want to check out the post there, head over to this [link](https://hackernoon.com/how-to-make-a-rockstar-github-profile-readme).

A couple of years ago Github launched a neat “hidden” feature (seems like it’s still somewhat hidden these days) which allowed you to create a special kind of repository in your account.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img1.png" alt="">
</figure>

So you see, Github allows you to create this special repository and the README for this repo, acts as the landing page for your profile. You can read more about it in this [official blog post](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme) by Github.

You can share information about yourself with the community on GitHub.com by creating a profile README. GitHub shows your profile README at the top of your profile page.

## A Hello-World README page 👓

It’s pretty simple to whip up a bare-bones profile page.

All you need to do is create this special repository named after your username and add a README page to it.

Make sure to make this repository public and for starters, go ahead and check the “Add a README file” box while creating the repository.
{: .notice-info}

The newly created repo will contain a templated README courtesy of Github and Bob’s your uncle!

## Wow, this was pretty simple! 🍦

Well, yeah! But this is like a vanilla [soft-serve](https://www.mcdonalds.com/us/en-us/product/vanilla-cone.html). It’s quick and it’s delicious.

But, that’s not what we really want now, is it?

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img2.gif" alt="">
</figure>

I for one want to have “some” sundae 😝

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img3.png" alt="">
</figure>

That’s not a typo, btw (Software Enginee 😅). That’s a dynamic piece of text. Lemme go over what all is there in [my Github profile](https://github.com/edorado93) and see if that is something that might interest you :)

* _Profile Views —_ Number of people who visited the profile.
* _Social badges_ — Instagram, LinkedIn, Personal Website, Medium.
* _Typewriter Text_ — That’s a very simple text/banner generator that takes up any text you want and displays it in a typewriter fashion.
* _Basic Information_— A few bullet points about myself.
* _Programming Quote of the day —_ A daily programming quote that gets updated on the profile dynamically.
* _Latest Blog Posts_ — This article will also show up on the profile the next time you visit :)
* _What’s Vibin? —_ Displays the song I’m listening to right now on Spotify!
* _Hey there, Seattle!_ — Most recent posts from an amazing Instagram account exploring Seattle, WA.
* _Github Stats_ — There’s a whole lot to unpack here so we’ll get to this later on in the article.
* _The Dev card_ — That orange-colored card you see on the right.

The profile is not a static one but a dynamic one.

Why is that?

Because we use Github Actions — a whole lot of them — to update various parts of the README at different times of the day 🤘🏻.

If this all sounds fun to you and you want to upgrade your Github profile as well, read on!

## Profile Views Counter 👁‍🗨

This one’s pretty simple to set up. All you need to do is, add the following line of code to your README wherever you want the counter to appear.

```
![](https://komarev.com/ghpvc/?username=your-github-username)
```

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img4.png" alt="">
</figure>

For more customizations to how this appears on your profile, refer to the official documentation [here](https://github.com/antonkomarev/github-profile-views-counter).

## Social Badges 🏅

For the badges, the [shields project](https://shields.io/) was super handy. For ease of use, here are the relevant badge links from my profile. Feel free to change the “HANDLE” below and copy-paste the same to yours :)

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img5.png" alt="">
</figure>

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img6.png" alt="">
</figure>

We have the profile view counter and the badges set up. Woot Woot!

## Typewriter Text

This one’s also pretty simple to set up. We’re not addressing the elephant in the room first!

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img7.png" alt="">
</figure>

Head over to [this website](https://readme-typing-svg.herokuapp.com/demo/) and add whatever text you need along with your own customizations and finally, copy the markdown link for the same and add to your README. Easy peasy!

## Basic Information

Nothing’s really fancy here. It’s just some pieces of information about myself. You don’t necessarily have to write about your technical accomplishments.

Go crazy with what you write. I added my tennis profile, my pronouns, my hiking interests, in addition to where I work.

The world is your oyster!

In general, though, try to keep it anywhere from 8–10 bullet points. Any more than that and it will start to weigh on the reader.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img24.png" alt="">
</figure>

Basic information section from the profile.

## Programming Quote of the day 📜

There are multiple ways of adding a daily quote to your profile. If you’re feeling a little adventurous, you can write a script to call an external API that fetches the most recent quotes. The API being:

```
[https://programming-quotes-api.herokuapp.com/Quotes?count=](https://programming-quotes-api.herokuapp.com/Quotes?count=2)2
```

And this is what the response looks like in the JSON format.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img8.png" alt="">
</figure>

You can then parse this response to fetch the quotes, however many you requested — count=2 in the API — and display them in the README in some format.

In order to update the quotes regularly, you’ll need to add a Github Action that will run your script on a regular basis, maybe once each day, and update the README with the quotes.

While this might seem the programmatically pleasing way to go, the final result might require a lot more effort as the presentation is equally important for the quotes.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img9.png" alt="">
</figure>

This seems more aesthetically pleasing than the quote itself, doesn’t it?

If you think it does, then go ahead and follow the details in this [great repository](https://github.com/PiyushSuthar/github-readme-quotes).

Essentially, you need to add this image tag to your README file wherever you want the quote to appear. A new quote might appear whenever someone opens your profile page.

This is the one-liner solution that in most likeliness, does the API calls and SVG rendering in the background and simply returns an image. Notice the “_quotes-github-readme.vercel.app_”. Well, that’s the hosted service linked to the Github repository that is running the quote image generator server or something.

Pretty cool stuff!

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img10.png" alt="">
</figure>

## Daily Dev Card 🏋

Do you like to read?

If the answer’s yes and your reading list includes some technical blogs from time to time, you might want to consider daily dot dev.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img11.png" alt="">
</figure>

Personally, I’ve added the chrome extension to get a regular feed of articles about topics I love to read about. Not really publicizing the platform but it is a great extension and platform.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img12.png" alt="">
</figure>

They generate an awesome dev-card for you based on your reading interests including all the badges, publications, topics you like, etc. The more you read, the better it gets.

Follow [this great blog](https://daily.dev/blog/adding-the-daily-devcard-to-your-github-profile?utm_source=webapp&utm_medium=devcard&utm_campaign=devcardguide&utm_id=inapp) post on how to add this dev-card to your profile. Most importantly, this is a dynamic card i.e. we use Github Actions workflow to update the card at frequent intervals.

## Latest Blog Posts ✏️

This one’s especially important if you’re an avid writer. There are a lot of platforms these days for writing and sharing both technical and non-technical content. There’s [Medium](https://medium.com/), [Dev.to](https://dev.to/), [Ghost.io](https://ghost.org/), and maybe your own personal website.

Basically, if you have any kind of RSS feed, you can hook it up with the README profile and keep updating it with the latest posts.

How, you might ask? Via Github Actions of course :)

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img13.png" alt="">
</figure>

This Github Action periodically replaces the following comments in your README with the hyperlinks to your recent 5 blog posts.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img14.png" alt="">
</figure>

Follow the steps mentioned [here](https://github.com/gautamkrishnar/blog-post-workflow#how-to-use) to set this up.

Also, as a general rule of thumb, if you end up using any open source software, make sure to start it and share it! Goes a long way to help open-source developers.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img15.png" alt="">
</figure>

## What’s Vibin? 🎧 🎼

I had the most fun setting this up. Before we get to the steps, one might ask why do we need Spotify’s now playing on a Github profile page?

Well, why not? A developer is not just a bunch of commits, PRs, and open source projects.

This is just an effort to make it more personal. Go ahead and add those Strava runs, Goodreads reading lists, anything you want really.

[This great repository](https://github.com/novatorem/novatorem) contains all the details on how you can set this up for your README.

I ran into trouble setting this up with Vercel or Heroku based on the steps [here](https://github.com/novatorem/novatorem/blob/master/SetUp.md).

The server is simply running the script “fetch_spotify.py” to get the currently playing song details for a user and then render an SVG based on a template.

Instead of a hosted service, I decided to make use of Github Actions to call the same script every 5 minutes (can’t have a higher frequency) and do the exact same thing: generate an SVG from the currently playing song.

Here are the steps I followed to set this up:

1.  Generated the Client Id, Client Secret, and the Refresh token as mentioned in the repository linked above.
2.  Copied the [templates folder](https://github.com/novatorem/novatorem/tree/master/api/templates), [spotify.py](https://github.com/novatorem/novatorem/blob/master/api/spotify.py), and [templates.json](https://github.com/novatorem/novatorem/blob/master/api/templates.json)
3.  Renamed spotify.py to fetch_spotify.py and made some changes to it. We don’t want to run a flask server. Instead, it should be invokable via the main function.
4.  Setup a new Github Actions workflow to call the script at a set schedule

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img16.png" alt="">
</figure>

The script runs every 5 minutes and generates the “spotify.svg” file which gets placed in the repository root folder. From there, it gets picked up by the README file.

## Hey there, Seattle! 🏞

This might be a bit too much on the Github profile, but, I felt it’s worth showing off the beautiful place that Seattle is which is where work and home-away-from-home is currently for me :)

For this, I wrote a Python script that uses the [instaloader](https://instaloader.github.io/index.html) module to download the recent posts from a given Instagram account. We don’t need any sort of login functionality for accessing public accounts so make sure the account you choose is public.

Again, the script is attached to a Github actions workflow so that we keep the profile updated with the latest Instagram posts from the account.

You just need to set “INSTAGRAM_PUBLIC_HANDLE” as the secret for your Github Actions workflow to access and that’s about it :)

The script looks something like this:

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img17.png" alt="">
</figure>

The script downloads the recent 3 posts from the Instagram account and stores them in separate directories. Then, the README file can access them and display side-by-side.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img18.png" alt="">
</figure>

## Github Stats 🍬 🍭

This is really the meat (vegan!) of the profile. It’s the place where you really show off what your open-source contributions amount to in a crisp, easy-to-digest fashion. Mine doesn’t look like much right now but it’s a work-in-progress.

The first thing we have here is the Github stats card. This is a purview of all of your contributions so far on the platform like total stars, total PRs, commits, etc.

Follow the steps mentioned [here](https://github.com/anuraghazra/github-readme-stats#github-stats-card) to get the design you want for your card.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img19.png" alt="">
</figure>>

Next up, we have the top-languages card. This is something we tend to mention in our resumes. However, it’s better if Github compiles that for us based on our LOCs, right?

From the same repository as before, [follow the steps](https://github.com/anuraghazra/github-readme-stats#top-languages-card) to incorporate the top languages card in your profile.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img20.png" alt="">
</figure>

Finally, there’s the big Github stats image that has a bunch of theatrical statistical stuff from your profile and contributions over the years.

That comes from a separate repository and like all of these Github stats, that is also something that is dynamically updated. The stats and top languages above come from a hosted service, but, the image/card is updated by Github Actions.

There’s a whole lot of customization around what you want and don’t want to include in the card and you can refer to the information mentioned [here](https://github.com/lowlighter/metrics) for that.

Personally, I got a lot of inspiration for my profile from [Waren Gonzaga](https://github.com/WarenGonzaga/WarenGonzaga/blob/main/README.md).

I also kinda copied the Github Actions for generating the stats card from their repository as well.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img21.png" alt="">
</figure>

In case you wanna have a quick look at the workflow.

## Other Notable mentions

That’s pretty much what all was needed to set up a great (rockstar? you tell me!) Github profile. There are a few other notable mentions that I’d like to point out though.

### Carbon

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img22.png" alt="">
</figure>

[Carbon](https://carbon.now.sh/) is a great tool for beautifying your code snippets and adding them to your articles. The only downside is, they’re images and not scrollable like Github Gists or something.

### Awesome Github Profiles

A [brilliant collection](https://github.com/abhisheknaiidu/awesome-github-profile-readme) for some of the greatest, inspiring Github profiles. This is where I personally started to get some inspiration for my profile.

### Slackmojis

Head over [here](https://slackmojis.com/) and see for yourself! Great collection of animated emojis that you can use in your profile.

### Capsule Render

The [footer for the profile](https://github.com/kyechan99/capsule-render#text) README is this wave-like animation that keeps changing colors and gradients on its own.

<figure class="align-center">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img25.png" alt="">
</figure>

If this is something that interests you, head over to the link shared before (capsule-render).

Thanks!
=======

If you’ve made it this far, kudos to you! If you found this article useful, do make sure to share it amongst your friends and folks who are looking to upgrade their READMEs as well.

Also, [here’s a link to my Github Profile](https://github.com/edorado93/edorado93) repository. Feel free to fork and play around.

<figure class="align-center">
  <a href="https://ko-fi.com/letscatchupoversomecoffee"><img src="{{ site.url }}{{ site.baseurl }}/assets/images/dynamic-github/img23.gif" alt=""></a>
</figure>
