# How to Contribute

`isbnlib` has a very small code base, so it is a good project to begin your
adventure in open-source.

> **NOTE**: By contributing you agree with the [license terms](LICENSE-LGPL.txt)
  (**LGPL v3**) of the project.


## Main Steps

1. Make sure you have a [GitHub account](https://github.com/signup/free)
2. Submit a ticket for your issue or idea (**ONE ticket for each issue or idea**)
   ([help](https://www.youtube.com/watch?v=TJlYiMp8FuY)),
   on https://github.com/xlcnd/isbnlib/issues,
   (if possible wait for some feedback before any serious commitment... :)
3. **Fork** the repository on GitHub and **clone it locally**
   ([help](https://help.github.com/articles/fork-a-repo)).
4. `pip install -r requirements-dev.txt` (at your local directory).
5. Do your code... (**remember the code must run on python 2.7, 3.5+
   and be OS independent** It is easier if you start to write in python 3 and then
   adapt for python 2) (you will find [Github Actions](https://docs.github.com/en/actions) very handy for
   testing with this requirement!)
6. Write tests for your code using `nose` and put then in the directory `isbnlib/test`
7. Pass **all tests** and with **coverage > 90%**.
   Check the coverage locally with the command
   `nosetests --with-coverage --cover-package=isbnlib`.
8. **Check if all requirements are fulfilled**!
9. **Push** your local changes to GitHub and make there a **pull request**
   ([help](https://help.github.com/articles/using-pull-requests/))
   **using `dev` as base branch** (by the way, we follow the *fork & pull* model with this small change).
   **VERY IMPORTANT:** Don't put in the same pull request unrelated changes in the code,
   make one pull request for each set of related changes!

> **NOTE**: *Travis*, *coverage*, *flake8* and  *pylint*, have already
configuration files adapted to the project.

## Style

Your code **must** be [PEP8](http://legacy.python.org/dev/peps/pep-0008/) compliant
and be concise as possible (use `yapf` then check it with
`flake8` and `pylint`).

Use doc strings ([PEP257](http://legacy.python.org/dev/peps/pep-0257/))
for users and comments (**few**) as signposts
for fellow developers. Make your code as clear as possible.


## Red Lines

**Don't submit pull requests that are only comments to the code that is
already in the repo!**
Don't expect kindness if you do that :) You **can** comment and give
suggestions on the code at the
[issues](https://github.com/xlcnd/isbnlib/issues/5) page.

**No** doc tests! Remember point 6 above.

**Don't** submit pull requests without checking points 8 and 9!



## Suggestions

Read the code in a structured way at [sourcegraph](https://sourcegraph.com/github.com/xlcnd/isbnlib).

Goto [issues/enhancement](https://github.com/xlcnd/isbnlib/issues?labels=enhancement&page=1&state=open)
for possible enhancements to the code.
If you have some idea that is not there enter your own.
Select some focused issue and enter some comments on how you plan to tackle it.


## Important

If you don't have experience with these issues, don't be put off by these requirements,
see them as a learning opportunity. Thanks!



## Resources (for *newbies*)


### Minimum git & GitHub

- https://guides.github.com/activities/hello-world/
- https://guides.github.com/introduction/flow/index.html
- https://www.youtube.com/watch?v=IeW1Irw45hQ
- https://www.youtube.com/watch?v=U8GBXvdmHT4
- https://www.youtube.com/watch?v=9Blbj1HMROU


### More Resources by Topic

|                  **Topic**  |                              **Resource**                               |
|----------------------------:|:------------------------------------------------------------------------|
|                 fork a repo | https://help.github.com/articles/fork-a-repo                            |
|                pull request | https://help.github.com/articles/using-pull-requests/                   |
|                     git log | https://www.youtube.com/watch?v=U8GBXvdmHT4                             |
|      local feature branches | https://www.youtube.com/watch?v=ImhZj6tpXLE                             |
|           git & GitHub tips | https://github.com/tiimgreen/github-cheat-sheet                         |
|                             | http://cbx33.github.io/gitt/intro.html                                  |
|                             | http://git-scm.com/documentation                                        |
|                             | http://gitimmersion.com/                                                |
|                             | http://www.youtube.com/playlist?list=PLq0VzNtDZbe9QLq8YCizFN2TVWvlLjrvX |
|                   nosetests | http://pythontesting.net/framework/nose/nose-introduction/              |
|                contributing | https://www.youtube.com/watch?v=IXnNgLmd6BM                             |
|                             | http://openhatch.org/missions                                           |
|                             | http://opensource.com/resources/how-get-started-open-source             |
