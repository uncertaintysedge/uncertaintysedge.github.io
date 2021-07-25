# uncertaintysedge.github.io/

Do words show up here?

## why make static site?

1. Organize
2. Possible methods: site vs. journal vs. documents
3. 1&2 --> site is most external
4. Possible writings: drafts, outlines(start draft), posts, essays(formal post)

#### why jekyll?

1. Github hosting = familiar & free
2. Every SSG has quiarks (i.e. innessential & arbitrary dependencies)
3. lost in details of JAMstack --> provides arbitrary structure

#### why not alternatives?

1. Medium & Tumblr: No
2. Blogger: No
3. Wix: No
4. Wordpress: beyond necessities (need to weight pros and cons of server dependence)   
6. eleventy: considering this?

## directory structure

[Source](https://jekyllrb.com/docs/structure/)

```
.
├── _config.yml
├── _data
│   └── members.yml
├── _drafts
│   ├── begin-with-the-crazy-ideas.md
│   └── on-simplicity-in-technology.md
├── _includes
│   ├── footer.html
│   └── header.html
├── _layouts
│   ├── default.html
│   └── post.html
├── _posts
│   ├── 2007-10-29-why-every-programmer-should-play-nethack.md
│   └── 2009-04-26-barcamp-boston-4-roundup.md
├── _sass
│   ├── _base.scss
│   └── _layout.scss
├── _site
├── .jekyll-cache
│   └── Jekyll
│       └── Cache
│           └── [...]
├── .jekyll-metadata
└── index.html # can also be an 'index.md' with valid front matter
```
