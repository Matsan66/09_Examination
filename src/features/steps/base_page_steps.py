from behave import given, then
from playwright.sync_api import expect
from src.features.helpers import get_base_page


@given(u'att jag är på startsidan')
def step_goto_startpage(context):
    base_page = get_base_page(context)
    context.base_page = base_page
    base_page.navigate_to()


@then(u'ska huvudrubriken "Läslistan" synas')
def step_check_main_heading_visible(context):
    main_heading = context.base_page.main_heading

    expect(main_heading).to_be_visible(timeout=5_000)


@then(u'ska rubriken "Välkommen!" synas')
def step_check_welcome_heading_visible(context):
    welcome_heading = context.base_page.welcome_heading

    expect(welcome_heading).to_be_visible(timeout=5_000)


@then(u'ska knappen "{button_name}" visas')
def step_check_buttons_visible(context, button_name):
    button = context.base_page.get_button_name(button_name)

    expect(button).to_be_visible(timeout=5_000)
