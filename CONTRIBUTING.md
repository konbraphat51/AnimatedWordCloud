# Contributing to AnimatedWordCloud
Greetings, Thanks for your interest in contributing to AnimatedWordCloud.

Please see [Code of Conduct](CODE_OF_CONDUCT.md).

## Declear an issue before develop
We love your contributing, but there is a possibility that somebody else already doing your work, or your plan is unnecessary. Please make an issue and notice us before start developing.

## Code
### Writing Python
* Follow [PEP8](https://peps.python.org/pep-0008/), you can automatically do this by using [black](https://github.com/psf/black) with `--line-length = 99`

* Please follow this [naming convention](https://namingconvention.org/python/). For example, global constant variables must be in `ALL_CAPS`;
  <img src="https://i.stack.imgur.com/uBr10.png" />

* Variables, classes, modules names should be **nouns**, and functions, methods names should be **verb**.

* Write your test for your new features in `tests/` directory.
If the output is graphical, show the demonstrating output in the PR.
But also add a test code to see if there is an error.
* Get rid of commented out codes.
* All `#TODO` must be reported at issues.
* Comments cannot be too much. Write what you intended **in English**.
* One module's responsibility (to-do) should be only one. If you are trying to adding a method of another function, **make a new module**

### Commit message
Please clearify what you did.  
Verb at the very front will make easier to see.  
ex)
Refac: clearify commentation  
Add: rid duplication of words

### PR
Submit PR to `dev` branch (Not `main` branch!!).

If there is something pointed out from GitHub Actions, please fix it.
