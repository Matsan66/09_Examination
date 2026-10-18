from behave import given, when, then
from playwright.sync_api import expect
from src.features.helpers import (get_base_page,
                                  get_catalog_page, get_add_book_page)


@when(u'jag klickar på knappen "Lägg till bok"')
def step_click_button_add_book(context):
    get_base_page(context)
    context.base_page.add_book_button.click(timeout=1000)


@then(u'ska formuläret för att lägga till en bok visas')
def step_check_add_book_form_visible(context):
    get_add_book_page(context)
    new_book_form = context.add_book_page.add_book_form
    expect(new_book_form).to_be_visible()


@then(u'textfältet titel visas')
def step_check_title_field_visible(context):
    title_field = context.add_book_page.title_field
    expect(title_field).to_be_visible()


@then(u'textfältet författare visas')
def step_check_author_field_visible(context):
    author_field = context.add_book_page.author_field
    expect(author_field).to_be_visible()


@given(u'att jag är i vyn för att lägga till en ny bok')
def step_goto_add_vew_book_view(context):
    get_base_page(context)
    context.base_page.navigate_to()
    context.base_page.add_book_button.click(timeout=1000)
    get_add_book_page(context)


@when(u'jag fyller i textfältet titel med "testbok"')
def step_fill_title_field(context):
    title_field = context.add_book_page.title_field
    title_field.fill(u'testbok')


@then(u'ska knappen ”Lägg till ny bok” förbli inaktiverad')
def step_check_submit_button_disabled(context):
    expect(context.add_book_page.add_new_book_button).to_be_disabled()


@when(u'jag fyller i textfältet författare med "John Doe"')
def step_fill_author_field(context):
    author_field = context.add_book_page.author_field
    author_field.fill(u'John Doe')


@then(u'ska knappen ”Lägg till ny bok” aktiveras')
def step_check_submit_button_enabled(context):
    expect(context.add_book_page.add_new_book_button).to_be_enabled()


@when(u'jag fyllt i formuläret med titel "testbok" och författare "John Doe"')
def step_fill_the_form(context):
    context.add_book_page.title_field.fill(u'testbok')
    context.add_book_page.author_field.fill(u'John Doe')


@when(u'jag klickar på knappen "Lägg till ny bok"')
def step_click_add_book_button(context):
    context.add_book_page.add_new_book_button.click(timeout=1000)


@then(u'ska formuläret tömmas')
def step_check_form_to_be_emptied(context):
    expect(context.add_book_page.title_field).to_be_empty()
    expect(context.add_book_page.author_field).to_be_empty()


@then(u'knappen "Lägg till ny bok" deaktiveras')
def step_check_add_book_button_disabled(context):
    expect(context.add_book_page.add_new_book_button).to_be_disabled()


@then(u'den nya boken visas i katalogen med rätt titel och författare')
def step_check_book_added_in_catalog(context):
    get_catalog_page(context)

    book = context.catalog_page.books.filter(
        has_text="testbok"
    ).filter(
        has_text="John Doe"
    )

    expect(book).to_be_visible()
