import textwrap


def _test_freezer(pytester):
    pytester.makefile(
        ".feature",
        parent=textwrap.dedent(
            """\
            Feature: Parent
                Scenario: Parenting is easy
                    Given I have a parent fixture
                    And I have an overridable fixture
            """
        ),
    )
    result = pytester.runpytest()
    result.assert_outcomes(passed=1)
