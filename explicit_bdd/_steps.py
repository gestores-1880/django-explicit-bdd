from django.core import mail
from pytest_bdd import step, parsers
import freezegun

# import ipdb; print('\a'); ipdb.sset_trace()
# @step(parsers.re(r'hoy es el "(?P<date>[^\"]+)"'))
@step(parsers.re(r'today is "(?P<date>[^\"]+)"'))
def freeeze(date):
    with freezegun.freeze_time(date):
        yield

# 'pytestbdd_stepdef_*_today is "(?P<date>[^\\"]+)"' = Decoratro(freeeze)


# @step("veo que se han enviado emails con los siguientes parametros")
# @step("I see that emails have been sent with the following parameters")
# def step_mpl(datatable):
#     datatable.test.assertEqual(len(mail.outbox), len(datatable.table.rows))
#     for row in datatable.table.rows:
#         mail_send = False
#         for email in mail.outbox:
#             mail_found = True
#             for key, value in row.as_dict().items():
#                 mail_found &= value == str(getattr(email, key))
#             mail_send |= mail_found
#         assert mail_send
#     # for row, email in zip(context.table.rows, mail.outbox):
#     #     for key, value in row.as_dict().items():
#     #         assert value == str(getattr(email, key)), f'{key} expected: {value} actual:{getattr(email, key)}'


# @step("veo que no se ha enviado email")
# @step("I see that no email has been sent")
# def step_mpl():
#     assert len(mail.outbox) == 0
