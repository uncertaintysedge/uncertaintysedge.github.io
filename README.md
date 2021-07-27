# uncertaintysedge.github.io/

Do words show up here?

## why make static site?

1. Organize
2. Possible methods: site vs. journal vs. documents
3. 1&2 --> site is most external
4. Possible writings: drafts, outlines(start draft), posts, essays(formal post)

### why jekyll?

1. Github hosting = familiar & free
2. Every SSG has quiarks (i.e. innessential & arbitrary dependencies)
3. lost in details of JAMstack --> provides arbitrary structure

### why not alternatives?

1. Medium & Tumblr: No
2. Blogger: createive deadend
3. Wix: No
4. Wordpress: beyond necessities (need to weight pros and cons of server dependence)   
6. eleventy: considering this?

#### why not Medium?


> Medium is an American online publishing platform developed by Evan Williams and launched in August 2012. It is owned by A Medium Corporation.[2] The platform is an example of social journalism, having a hybrid collection of amateur and professional people and publications, or exclusive blogs or publishers on Medium,[3] and is regularly regarded as a blog host.

[Source](https://en.wikipedia.org/wiki/Medium_%28website%29)

#### why not eleventy?

1. preaches lack of dependencies
2. I don't care about client-side JavaScript
3. JavaScript Frameworks and Libraries vs Ruby or Templating Langs.

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

## file names

**leading underscores**

>Web Pages framework has been configured not to allow files with leading underscores in their names from being requested directly.

[Source](https://stackoverflow.com/questions/4576548/why-does-razor-layout-cshtml-have-a-leading-underscore-in-file-name)

**leading periods**

> Historically they are meant to be used for configuration files and directories. They are 'hidden' (the leading dot) by convention. The dot also makes sure that these files/directories are hidden from 'normal' operations (example: ls -l will not show them, ls -la will).

[Source](https://www.linuxquestions.org/questions/linux-general-1/files-starting-with-period-722237/)
