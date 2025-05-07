from pprint import pprint

from proto_client.main import (
    get_proto,
    post_proto,
    put_proto,
    delete_proto,
)
from proto_client.proto_messages.messages import (
    Header,
    TestCase,
    TestCaseList,
    TestSuite,
    TestSuiteList,
)
BACKEND_BASE_URL = "http://127.0.0.1:10110"


def header_print(func):
    """Decorator to print the header of the test case."""

    def wrapper(*args, **kwargs):
        print(f"Testing {func.__name__} endpoint")
        result = func(*args, **kwargs)
        print('-'*40)
        return result

    return wrapper


@header_print
def test_case_list():
    """Test the test case list endpoint."""
    url = f'{BACKEND_BASE_URL}/database/test-case/list'
    result = get_proto(TestCaseList, url)
    pprint(result)


@header_print
def get_one_test_case():
    """Get one test case."""
    url = f'{BACKEND_BASE_URL}/database/test-case/5'
    result = get_proto(TestCase, url)
    pprint(result)


@header_print
def test_case_update_removing_position():
    """Test the test case update endpoint."""
    get_url = f'{BACKEND_BASE_URL}/database/test-case/5'
    url = f'{BACKEND_BASE_URL}/database/test-case/update/5'

    test_case: TestCase = get_proto(TestCase, get_url)

    robot_positions = test_case.moves_list

    robot_positions.pop(1)
    test_case.moves_list = robot_positions

    print('Object being sent to the server:')
    pprint(test_case)
    print('----------------------------------')
    result = put_proto(url, test_case, TestCase)
    print('Result from the server:')
    pprint(result)


@header_print
def test_case_update_adding_position():
    """Test the test case update endpoint."""
    get_url = f'{BACKEND_BASE_URL}/database/test-case/5'
    url = f'{BACKEND_BASE_URL}/database/test-case/update/5'

    test_case: TestCase = get_proto(TestCase, get_url)

    robot_positions = test_case.moves_list
    new_pos = Header(
        id=11,
        name='picture_variation_1',
    )
    robot_positions.append(new_pos)
    test_case.moves_list = robot_positions

    result = put_proto(url, test_case, TestCase)
    pprint(result)


@header_print
def test_case_update():
    """Test the test case update endpoint."""
    get_url = f'{BACKEND_BASE_URL}/database/test-case/1'
    url = f'{BACKEND_BASE_URL}/database/test-case/update/1'
    test_case: TestCase = get_proto(TestCase, get_url)

    robot_positions = [
        Header(
            id=11,
            name='picture_variation_1',
        ),
        Header(
            id=12,
            name='picture_variation_2',
        ),
    ]

    test_case.moves_list = robot_positions

    result = put_proto(url, test_case, TestCase)
    pprint(result)


@header_print
def test_suite_list():
    """Test the test suite list endpoint."""
    url = f'{BACKEND_BASE_URL}/database/suite/list'
    result = get_proto(TestSuiteList, url)
    pprint(result)


@header_print
def test_suite_create():
    """Test the test suite create endpoint."""
    url = f'{BACKEND_BASE_URL}/database/suite/create'
    test_suite = TestSuite()
    test_suite.name = 'Validation Test Suite'
    test_suite.tests_cases = [
        Header(
            id=5,
            name='CAM-main_MODE-photo_ASPECT_RATIO-916_FLASH-on_ZOOM-1.5',
        ),
        Header(
            id=6,
            name='CAM-main_MODE-portrait_ASPECT_RATIO-916_FLASH-on_ZOOM-2.0',
        ),
    ]
    result = post_proto(url, test_suite, TestSuite)
    pprint(result)


@header_print
def test_suite_update():
    """Test the test suite update endpoint."""
    get_url = f'{BACKEND_BASE_URL}/database/suite/1'
    url = f'{BACKEND_BASE_URL}/database/suite/update/1'
    test_suite: TestSuite = get_proto(TestSuite, get_url)

    # test_suite.name = 'Updated Test Suite Name'
    test_suite.tests_cases = [
        Header(
            id=5,
            name='CAM-main_MODE-photo_ASPECT_RATIO-916_FLASH-on_ZOOM-1.5',
        ),
        Header(
            id=4,
            name='Name doesnt matter',
        ),
    ]

    result = put_proto(url, test_suite, TestSuite)
    pprint(result)


@header_print
def test_suite_get_one():
    """Test the test suite get one endpoint."""
    url = f'{BACKEND_BASE_URL}/database/suite/1'
    result = get_proto(TestSuite, url)
    pprint(result)


def main():
    # test_case_list()
    # test_case_update_removing_position()
    # get_one_test_case()
    # test_case_update_adding_position()
    # get_one_test_case()
    # test_case_update()
    # test_suite_create()
    # test_suite_list()
    # test_suite_update()
    # test_suite_list()
    test_suite_get_one()


if __name__ == '__main__':
    main()
