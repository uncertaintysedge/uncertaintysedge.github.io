---
title: "Posts"
excerpt: "Here are some posts"
permalink: /posts/
---

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }} {% raw %}{{ page.date | date: "%-m" }}{% endraw %}</a>
    </li>
  {% endfor %}
</ul>