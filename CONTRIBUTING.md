# Contributing to AnimatedWordCloud
Greetings, Thanks for your interest in contributing to AnimatedWordCloud.

## Status of `dev` branch.
[![coveragePR](https://github.com/konbraphat51/AnimatedWordCloud/actions/workflows/python-coverage-PR.yml/badge.svg?branch=dev)](https://github.com/konbraphat51/AnimatedWordCloud/actions/workflows/python-coverage-PR.yml)
[![unit-test](https://github.com/konbraphat51/AnimatedWordCloud/actions/workflows/python-tester.yml/badge.svg?branch=dev)](https://github.com/konbraphat51/AnimatedWordCloud/actions/workflows/python-tester.yml)
[![Lint](https://github.com/konbraphat51/AnimatedWordCloud/actions/workflows/lint.yml/badge.svg)](https://github.com/konbraphat51/AnimatedWordCloud/actions/workflows/lint.yml)

## Declear an issue before develop
We love your contribution, but there is a possibility that somebody else already doing your work, or your plan is unnecessary. Please make an issue and notify us before starting to develop.

## Environment

You need to pip install this library (`dev`branch) and update submodules
```
git clone (your fork)
cd (your fork)
pip install -e .
git submodule init
git submodule update
```

## Code
### Writing Python
* Follow [PEP8](https://peps.python.org/pep-0008/), you can automatically do this by using [black](https://github.com/psf/black) with `--line-length = 79`

* Please follow this [naming convention](https://namingconvention.org/python/). For example, global constant variables must be in `ALL_CAPS`;
  <img src="https://i.stack.imgur.com/uBr10.png" />

* Variables, classes, modules names should be **nouns**, and functions, methods names should be **verb**.

* Write your test for your new features in `tests/` directory.
If the output is graphical, show the demonstrating output in the PR.
But also add a test code to see if there is an error.
* Get rid of commented out codes.
* All `#TODO` must be reported at issues.
* Comments cannot be too much. Write what you intended **in English**.
* One module's responsibility (to-do) should be only one. If you are trying to add a method of another functionality, **make a new module**

### Commit message
Please clarify what you did.  
Verb at the very front will make it easier to see.  
ex)
Refac: clarify commentation  
Add: rid duplication of words

### PR
Submit PR to `dev` branch (Not `main` branch!!).

Submit PR as **draft** for the first. The GitHub Actions will start analyzing your contribution.

If there is something pointed out from GitHub Actions, please fix it.

**If all problems are solved, turn your draft PR to open PR, and report as a comment that you are ready to get reviewed**

