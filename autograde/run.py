#!/usr/bin/python3
import json
import os
import re
import sys
from os.path import isfile, join
from xml.etree import ElementTree
from shutil import copy2
import pytest


def grade():
    copy_submission()
    assignment = find_assignment()
    # Report written to an XML file (`--junitxml` flag), which you can parse
    result = pytest.main([f'autograde/tests/test_{assignment}', '--junitxml=/grader/log.xml'])
    if result == pytest.ExitCode.OK:
        write_feedback(1.0, "You've passed this assignment! You're ready to move on to the next topic.")
    elif result == pytest.ExitCode.TESTS_FAILED:
        # Lots of room for improvement here. You could:
        # * give partial credit
        # * differentiate critical failures from 'room for improvement'
        # * use Jinja templates for fancy feedback
        # * etc.
        write_feedback(0.0, get_failure_message())
    else:
        write_feedback(0.0, "We were unable to grade your submission. Please reach out to us in the forums.")


def copy_submission():
    # Coursera recommends copying submissions out of '/shared/submission'
    # before attempting to assess them.
    submit_path = '/shared/submission'
    os.mkdir('/grader')
    # Note that I'm not recursing into a directory of files.
    # You will need a different solution if the assignment uses multiple files.
    files = [f for f in os.listdir(submit_path) if isfile(join(submit_path, f))]
    for file in files:
        copy2(join(submit_path, file), join('/grader', file))
    sys.path.append('/grader')


def find_assignment():
    assign_path = '/grader'
    files = [f for f in os.listdir(assign_path) if isfile(join(assign_path, f))]
    for file in files:
        # My favorite Twitter joke this week:
        # the name for a group of regexes is 'regrets'
        if re.match(r'assign\d\d?\.py', file):
            return file


def get_failure_message():
    # Only grabbing the first failure in the report.
    # You could certainly offer a full report to learners.
    doc = ElementTree.parse('/grader/log.xml')
    root = doc.getroot()
    for failure in root.iter('failure'):
        message = failure.get('message')
        break_index = message.find('\n')
        if break_index >= 0:
            message = message[:break_index]
        return message[16:] if 'AssertionError' in message else message


def write_feedback(score, message):
    document = {'fractionalScore': score, 'feedback': message}
    with open('/shared/feedback.json', 'w') as feedback:
        json.dump(document, feedback)


def test_solutions():
    sys.path.append(os.path.join(os.path.dirname(__file__), 'solutions'))
    pytest.main(['-rA', 'autograde/tests/'])


if __name__ == "__main__":
    workspace = os.environ.get('WORKSPACE_TYPE')
    if workspace is None:
        # Variable not set when running in autograder environment.
        # Run grading script on learner submission.
        grade()
    elif workspace == 'instructor':
        test_solutions()
