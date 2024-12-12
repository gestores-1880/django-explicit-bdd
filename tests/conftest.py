# pytest_plugins = "pytester"
import explicit_bdd._steps

# from pytest_bdd import step, parsers

for attr in dir(explicit_bdd._steps):
    if attr.startswith("pytestbdd_stepdef_"):
        locals()[attr] = getattr(explicit_bdd._steps, attr)


# import ipdb; print('\a'); ipdb.sset_trace()
# @step(parsers.re(r'hoy es el "(?P<date>[^\"]+)"'))
# @step(parsers.re(r'today is "(?P<date>[^\"]+)"'))
# def freeeze(freezer, date):
#     freezer.move_to(date)


# ipdb> pytest.fixture(name=fixture_step_name)(step_function_marker)
# <function step.<locals>.decorator.<locals>.step_function_marker at 0x7ffffbf6bd80>
# ipdb> fixture_step_name
# 'pytestbdd_stepdef_*_today is "(?P<date>[^\\"]+)"'
# 'pytestbdd_stepdef_*_today is "(?P<date>[^\\"]+)"'
# ipdb> step_function_marker
# <function step.<locals>.decorator.<locals>.step_function_marker at 0x7ffffbf68c20>
