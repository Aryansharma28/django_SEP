# Report for Assignment 1 - Group 10

## Project chosen

Name: **Django**

URL: **https://github.com/django/django**

Number of lines of code and the tool used to count it: we used Lizard to count the number of lines and the number of lines is 383659. However, excluding all other directories like `tests` and `docs`, by only focusing on the `django` directory and setting `-l python` in the Lizard arguments, the number of lines comes down to **112389**.
```bash
# The following assumes that we are currently in the root directory of the Django repository.
lizard django/ -l python
```

Programming language: **Python**

## Testing Framework
We have added this small section to the report, in order to provide some basic information of how the Django Test Suite functions.

Django provides a test suite that is used to test the Django codebase. The test suite is located in the `tests` directory of the Django repository. The test suite is run using the `runtests.py` script, which is located in the `tests` directory, and contains the hashbang to run with the default Python installation of the system.

The test suite supports options such as a `--settings` argument, which allows the user to pass some default settings for the Django environment. In our case, we are using the default settings provided by Django, `test_sqlite.py`, which include using an SQLite database, among others.

The test suite also supports a `--parallel` argument, which allows the user to set how many tests are set in parallel. The default value is calculated based on the available cores, however in some cases we have chosen to set this to `1`, due to conflicts with our custom coverage instrumentation. This will be mentioned explicitly, where used.

Finally, passing the name of a test module will run only the tests in that module. This is useful for running specific tests, as running the entire test suite can take time. For example, if one of us is working on the `mail` module, we can run only the tests in that module by running `./runtests.py mail --settings=test_sqlite`.

## Coverage measurement

### Existing tool

We used **coverage.py** to check the coverage of the repository, and it turned out to be 78%.

We ran the following commands, as mentioned in the [Django Unit Test Documentation for Contributors](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/#code-coverage):
```bash
# The following assumes that we are currently in the root directory of the Django repository, and in the created virtual environment.
cd tests
pip install coverage
pip install -e ..
pip install -r requirements/py3.txt
coverage run ./runtests.py --settings=test_sqlite # Runs the tests with coverage and using the SQLite adapter.
coverage combine # Combines the coverage data from all the test runs.
coverage html # Generates the HTML coverage report.
```
[//]: # (<Show the coverage results provided by the existing tool with a screenshot>)


The above yields the following coverage report, accessible at tests/coverage_html/index.html:
![Coverage Results](vu-docs-res/coverage-html.png)

### Your own coverage tool

<The following is supposed to be repeated for each group member>

#### Group Member Name (VUnet ID)

##### /path/to/function/file/function1_name

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

<Provide a screenshot of the coverage results output by the instrumentation>

##### /path/to/function/file/function2_name

<Provide the same kind of information provided for Function 1>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

#### Group Member Name (VUnet ID)

##### /path/to/test/file/test1_name

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

##### /path/to/test/file/test2_name

<Provide the same kind of information provided for Test 1>

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>
