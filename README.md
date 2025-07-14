# General Info

The website and Hugo theme are put into two seperate zip files:
`site.zip` and `themes.zip`. The Hugo theme we used is based on [Hugo Conference Theme](https://git.ins.jku.at/conferences/template-hugo-conferences) with some small modifications.

Create a new folder and unzip both files to the new folder so that the new directory looks like this:
```
.
├── archetypes
├── config.toml
├── content
├── layouts
├── LICENSE
├── README.md
├── rebuild.sh
├── scripts
├── static
└── themes
```
, in which `themes` folder is from `themes.zip` and other files are from `site.zip`.

# Build & Run

First install [Hugo](https://gohugo.io/) on your machine.
Once installed, you can locally test the website by executing:

	hugo server

In my case the output states that you can locally visit the website
at [http://localhost:1313/wisec21/](http://localhost:1313/wisec21/).

To let Hugo generate the website execute:

	./rebuild.sh

Once finished, you can then upload the generated files to the web server
with the following command (You may need to replace `WEB-SERVER` and `PATH` accordingly):

	rsync -chrvP --stats public/ WEB-SERVER:/var/www/PATH/wisec21/

