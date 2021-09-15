# Sample Code for Graded Assignments in Coursera Labs

The files in this repo were part of my exploration of using the VS Code base image in Coursera Labs with a Configurable Grader. I was mainly interested in understanding the graded assignment creation process, so these examples are not instructionally interesting, nor is my autograder script particularly robust. My objective was to offer a working example that others could use as a starting point for their own course assignments.

## Usage

There are two main directories for instructor content:

- **learn**: directory for assignment README, starter files, etc. that are intended for use by learners
- **autograde**: directory for grader logic, tests, solution code, and other files used in assessing learner work. These files are not copied to the learner environment

### Image configuration

These samples use the [pytest framework](https://docs.pytest.org/) for test cases. To get `pytest` to work in the VS Code image, I added this Docker(file) configuration when setting up the image in Lab Manager:

```dockerfile
USER root
RUN python3 -m pip install pytest==6.2.4 pytest-mock==3.6.1
USER coder
```

Note that Coursera hopes to remove the need to switch users when installing packages in the future.
