# Contributing to AnimatedWordCloud

Greetings, Thanks for your interest in contributing to AnimatedWordCloud.

## Status of `dev` branch.

<a href="https://codeclimate.com/github/konbraphat51/AnimatedWordCloud/maintainability"><img src="https://api.codeclimate.com/v1/badges/7a03252f77e7af46dc0f/maintainability" /></a>
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/20a71da0d9d841a2af236f6362a08ae7)](https://app.codacy.com/gh/konbraphat51/AnimatedWordCloud/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![unit-test](https://github.com/konbraphat51/AnimatedWordCloud/actions/workflows/python-tester.yml/badge.svg?branch=dev)](https://github.com/konbraphat51/AnimatedWordCloud/actions/workflows/python-tester.yml)
[![Lint](https://github.com/konbraphat51/AnimatedWordCloud/actions/workflows/lint.yml/badge.svg)](https://github.com/konbraphat51/AnimatedWordCloud/actions/workflows/lint.yml)
[![codecov](https://codecov.io/gh/konbraphat51/AnimatedWordCloud/graph/badge.svg?token=4OOX0GSJDJ)](https://codecov.io/gh/konbraphat51/AnimatedWordCloud)

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

- Follow [PEP8](https://peps.python.org/pep-0008/), you can automatically do this by using [black](https://github.com/psf/black) with `--line-length = 79`

- Please follow this [naming convention](https://namingconvention.org/python/). For example, global constant variables must be in `ALL_CAPS`;
  <img src="https://i.stack.imgur.com/uBr10.png" />

- Variables, classes, modules names should be **nouns**, and functions, methods names should be **verb**.

- Write your test for your new features in `tests/` directory.
  If the output is graphical, show the demonstrating output in the PR.
  But also add a test code to see if there is an error.
- Get rid of commented out codes.
- All `#TODO` must be reported at issues.
- Comments cannot be too much. Write what you intended **in English**.
- One module's responsibility (to-do) should be only one. If you are trying to add a method of another functionality, **make a new module**

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

## Updating Pypi

**Only for maintainers**

1. Update version of `README.md` & `setup.py` [[Example Commit]](https://github.com/konbraphat51/AnimatedWordCloud/commit/c886f593d590ebe990cd451c219df3d2733a5a48)
2. Commit 1. as "UpVer: [version]" to `dev`
3. Merge to `main`
4. Access to [Releases](https://github.com/konbraphat51/AnimatedWordCloud/releases) and make a new release with configuration below:
  - new tag: vX.X.X (new version)
  - Target branch: main
  - Release title: version X.X.X(new version)
  - Description: what changed
   ![image](https://github.com/konbraphat51/AnimatedWordCloud/assets/101827492/1bc79398-5458-4a8b-b03f-26efd51917fe)

5. GitHub Actions automatically upload the newest version to PyPI

