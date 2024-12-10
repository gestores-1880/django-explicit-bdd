# def pytest_addhooks(bdd) -> None:
# import pytest_bdd as bdd

# bdd.scenarios('.')

# from . import _steps

# def pytest_bdd_before_scenario(request, feature, scenario):
    # """Hooking into pytest-bdd-defined hooks to capture feature name and scenario + its steps"""
#     item = request.node
#     item.user_properties.extend(
#         [
#             ("feature", dict(name=feature.name, description=feature.description)),
#             ("scenario", dict(name=scenario.name, steps=scenario.steps)),
#         ]
#     )

# def pytest_configure(config):
    # """Add this plugin's CSS to pytest-html's --css option (which is an array)"""
    # try:
    #     css: Path = config.getoption(BDD_HTML_CSS_OPTION)
    #     if not css.exists():
    #         css = BDD_HTML_CSS_DEFAULT
    #     config.option.css.append(css)
    # except:  # pylint:disable=bare-except
    #     pass
    # import pytest_bdd as bdd

    # bdd.scenarios('.')

    # from . import _steps
