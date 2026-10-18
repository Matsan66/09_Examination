from behave import given, when, then
from playwright.sync_api import expect
import re
from src.features.helpers import get_my_books_page, get_catalog_page


@when(u'jag klickar på knappen "Mina böcker"')
def step_click_my_books_button(context):
    context.base_page.my_books_button.click(timeout=1000)
    get_my_books_page(context)


@then(u'ska vyn för Mina böcker visas')
def step_check_my_books_view_navigation(context):
    expect(context.my_books_page.my_books_view).to_be_visible()


@given(u'inga böcker är valda som favoriter')
def step_check_favorites_empty(context):
    get_my_books_page(context)
    expect(context.my_books_page.book_list.locator("li")).to_have_count(0)


@then(u'ska meddelandet ”När du valt, '
      u'kommer dina favoritböcker att visas här.” visas')
def step_check_empty_favorites_message(context):
    expect(context.my_books_page.empty_list_message).to_be_visible()


@when(u'jag klickar på favoritknappen på en bok')
def step_select_a_book_as_favorite(context):
    get_catalog_page(context)
    context.selected_book = context.catalog_page.books.nth(0)

    pattern = re.compile(r'"([^"]+)"')
    context.selected_book_title = pattern.search(
        context.selected_book.inner_text()).group(1)

    context.selected_book.locator(".star").click(timeout=1000)


@then(u'ska den valda boken visas i Mina böckers boklista')
def step_check_seleted_book_visible_in_favorite_list(context):
    favorite_book = context.my_books_page.book_list.filter(
        has_text=context.selected_book_title
    )

    expect(favorite_book).to_be_visible()


@when(u'jag klickar på favoritknappen på den favoritmarkerade boken')
def step_click_favorite_button_marked_book(context):
    context.selected_book.locator(".star").click(timeout=1000)


@then(u'ska den avmarkerade boken inte visas i Mina böckers boklista')
def step_check_unmarked_book_not_remain(context):
    expect(context.my_books_page.book_list.filter(
        has_text=context.selected_book_title
    )).to_have_count(0)
