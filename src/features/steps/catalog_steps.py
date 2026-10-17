from behave import given, when, then
from playwright.sync_api import expect
from src.features.helpers import get_catalog_page


@given(u'en annan vy än "Katalog" är vald')
def step_impl(context):

    context.base_page.add_book_button.click(timeout=1000)


@when(u'jag klickar på knappen "Katalog"')
def step_click_catalog_button(context):

    context.base_page.catalog_button.click(timeout=1000)


@then(u'ska rubriken "Sidan för dig som gillar att läsa. Välj dina favoriter." visas')
def step_check_view_descriptor(context):

    catalog_page = get_catalog_page(context)

    catalog_description = catalog_page.catalog_description

    expect(catalog_description).to_be_visible()


@then(u'listan med böcker ska visas')
def step_check_catalog_list(context):

    catalog_page = get_catalog_page(context)

    catalog_list =  catalog_page.catalog

    expect(catalog_list).to_be_visible()


@then(u'ska minst en bok visas i boklistan')
def step_control_book_exist(context):

    catalog_page = get_catalog_page(context)

    books =  catalog_page.books

    expect(books.first).to_be_visible()


@then(u'ska alla böcker i katalogen visas')
def step_control_all_books_exists(context):

    catalog_page = get_catalog_page(context)

    books = catalog_page.books

    for i in range(books.count()):
        book = books.nth(i)
        expect(book).to_be_visible()


@when(u'jag klickar på hjärt-ikonen för en bok')
def step_select_favorite_book(context):

    catalog_page = get_catalog_page(context)

    context.favorite_button = catalog_page.favorite_buttons.first
    context.favorite_button.click(timeout=1000)


@then(u'ska boken markeras som favorit')
def step_control_favorite_set(context):

    expect(context.favorite_button).to_have_class("star selected")


@given(u'en bok är markerad som favorit')
def step_mark_a_book_as_favorite(context):
    catalog_page = get_catalog_page(context)

    context.favorite_button = catalog_page.favorite_buttons.first
    context.favorite_button.click(timeout=1000)


@when(u'jag klickar på hjärt-ikonen för en favoritmarkerad bok')
def step_click_favorite_mark(context):

    context.favorite_button.click(timeout=1000)



@then(u'ska boken inte längre vara markerad som favorit')
def step_control_book_not_favorite(context):
    expect(context.favorite_button).to_have_class("star")
