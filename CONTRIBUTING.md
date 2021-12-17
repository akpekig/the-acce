
# Contributing
## Keep in mind
This project is developed with vulnerable users as the audience; this means people with conditions including visual impairments, learning difficulties, developmental disorders, difficulty understanding English, mental health syndromes, hearing impairments, and so forth. Not all conditions can be accounted for, due to the limitations of the internet, but many can. This audience should be considered before thinking of adding features. Could this feature hinder them, i.e. complicated terms of service? Bright colours with no alternative? Information provided exclusively through audio? If so, think of a fallback or alternative. If neither of those are possible, exclude the feature entirely.
## Fork / Clone from Master and create a new branch

The master branch must be bug-free. As such, any new features should be added to a new branch. Only if the branch passes all tests should it be merged with master. Do not commit values placed in the `.env` file, as these are made to be kept secret. Store them locally, using the `git update-index --assume-unchanged .env` command from your terminal to keep the file ignored. Generally, any cache files, local settings and dependencies should not be uploaded. These can be ignored in `.gitignore`. You may or may not update the `.gitignore` file at your discretion. 

In order to run the site locally, a database must be running as a daemon and configured in the `.env` file. These values are passed in `./settings.py`. Testing may be done in a virtual environment, constructed with either [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) or [conda](https://docs.conda.io/en/latest/). Running `pip install` where the file `./requirements.txt` is present will automatically install all the dependencies required by the project to run. Should you add new dependencies with the implementation of new functions, run `pip freeze > requirements.txt`. Pay attention to the versioning of dependencies, as this may cause conflict in the feature.

## Naming branches

It's useful to have branches with relevant names. If you are, for example, adding a new feature that allows for theme changes, name the branch something along the lines of `theme-change-function` and not `i-wanted-to-make-a-branch-xyz`. Try to have a branch per feature, and not one for several or several for one (The author of this is especially guilty of this, but it's still worth trying). 

## Adding new pages

As the website is a Django project, each page is mapped to views in specific apps. Each view requires a template and each template should depend on the base template, currently located in the `home` folder. No two templates should have the same path or name. No template should depend too heavily on HTML or Javascript. 

## Adding new styles

The relevant naming rule is true here as well. It should also go without saying that named classes, ids and even elements should avoid conflict with other styles. It is *never* worth attempting to edit existing stylesheets, especially third-party ones such as Bootstrap or jQuery. 

Hyperspecific styles should be avoided. If necessary, added it to the main stylesheet relevant to where the style will be used. Remember that stylesheets are written in Sass/SCSS before compilation, with the exception of splash/skeleton screens. SCSS stylesheets should be prefixed with an underscore and imported where relevant.

**Hypo**specific styles should be avoided too. Unstyled elements should not be given styles as this is one very quick way to conflict among all stylesheets and even browsers. If you absolutely must style an element without a class or id, nest it within parent class or id that can contain the style and prevent conflict with other stylesheets.

## Adding fonts

Don't.

## Adding miscellaneous features

It's always worth knowing exactly what feature you wish to add before going ahead and adding it, as not doing so will lead to inefficient implementation. For example, if you want a counter, Javascript has built-in functions to increment or decrement a given number. Thus, it would be unreasonable to write a conditional for `i + 1` where i is your own variable that you will then assign to another variable, etc. This is extremely long and difficult to maintain. 

*However*, if the code you need to write is in fact made shorter and easier to maintain by doing so yourself, please do so without relying on a dependency. Many dependencies are not maintained and thus, may quickly become full of bugs. Counting functions or testing suites are all well and good, but a Clock component essentially just wrapping a counter in someone else's styled div is not necessary. 

## Patching / Fixing bugs

First, be sure that a bug is a bug and not just a feature. For example, newer font formats `WOFF` and `WOFF2` will not work on older browsers, especially *not* IE. In this case, these fonts need not be considered a bug and removed. Instead, try adding compatible font formats such as `OTF` *in addition to* the existing ones. Some browsers may not have any easy fix. For example, Chrome often fails to implement the animated or smooth behaviours of Safari and Mozilla. Likewise, Safari fails to implement and endless number of things. These are not bugs, but browser issues. You may try to fix them, but if that means adding too much code, several more dependencies, or removing what works fine with other browsers, or even adding *new* bugs, move on.

Second, be sure that the bug does not lead to other bugs. These things can be an endless rabbit hole when trying to fix them by yourself. Sometimes, it is simply worth disabling what is experiencing the effects of the bug. Sometimes, it is worth letting it exist.

## Adding assets

Assets are added through a `static` directory in any given Django app. Assets should have relevant names. No two assets should have the same path or name name. No feature should be overly dependent on them, such that the site may crash should they fail to load. Should there be a feature so dependent on an asset, this feature should have a catch or fallback to prevent such the site from crashing.

## Folder Hierarchy (Main Branch)

```bash

├── README.md
├── accounts
	├── __init__.py
	├── __pycache__
		└── (cache files)
	├── admin.py
	├── apps.py
	├── forms.py
	├── migrations
		└── (migration files)
	├── models.py
	├── templates
		└── (HTML template files)
	├── tests.py
	├── urls.py
	└── views.py
├── home
	├── __init__.py
	├── __pycache__
		└── (cache files)
	├── admin.py
	├── apps.py
	├── migrations
		└── (migration files)
	├── models.py
	├── static
		└── (static files)
	├── templates
		└── (HTML template files)
	├── tests.py
	├── urls.py
	└── views.py
├── manage.py
├── matters
	├── __init__.py
	├── __pycache__
		└── (cache files)
	├── admin.py
	├── apps.py
	├── forms.py
	├── migrations
		└── (migration files)
	├── models.py
	├── templates
		└── (HTML template files)
	├── tests.py
	├── urls.py
	└── views.py
├── negotiations
	├── __init__.py
	├── __pycache__
		└── (cache files)
	├── admin.py
	├── apps.py
	├── forms.py
	├── migrations
		└── (migration files)
	├── models.py
	├── templates
		└── (HTML template files)
	├── tests.py
	├── urls.py
	└── views.py
└── the_acce
	├── __init__.py
	├── __pycache__
		└── (cache files)
	├── asgi.py
	├── settings.py
	├── urls.py
	└── wsgi.py
```