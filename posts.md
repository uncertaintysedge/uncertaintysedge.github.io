---
title: "Posts"
excerpt: "Here are some posts"
permalink: /posts/
---

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }} {{ page.date | date: '%B %d, %Y' }}</a>
    </li>
  {% endfor %}
</ul>