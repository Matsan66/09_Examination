from behave import when, then
from playwright.sync_api import expect
import re
from src.features.helpers import (
    get_base_page, get_my_books_page, get_catalog_page, get_statistics_page)


@when(u'jag klickar på knappen "Statistik"')
def step_click_statistics_button(context):
    get_base_page(context)
    context.base_page.statistics_button.click(timeout=1000)
    get_statistics_page(context)


@then(u'ska vyn för statistik visas')
def step_check_navigation_to_statistics_view(context):
    expect(context.statistics_page.statistics_view).to_be_visible()


@then(u'ska texten med antalet böcker visas')
def step_check_number_of_books_text_visible(context):
    expect(context.statistics_page.book_count).to_be_visible()


@then(u'ska texten med antalet hjärtmarkerade böcker visas')
def step_check_number_of_heartmarked_text_visible(context):

    expect(context.statistics_page.stars_count).to_be_visible()


@when(u'jag kontrollerar antal böcker i katalogen')
def step_check_number_og_catalog_books(context):
    get_catalog_page(context)
    context.number_catalog_books = context.catalog_page.books.count()


@then(u'ska antalet böcker som visas överensstämma med antalet i katalogen')
def step_compare_number_catalog_books_and_statistics(context):
    find_number = re.search(r"\d+",
                            context.statistics_page.book_count.inner_text())
    number_statistics_books = int(find_number.group())

    assert context.number_catalog_books == number_statistics_books


@when(u'jag kontrollerar antal favoritböcker')
def step_check_number_of_favorite_books(context):
    get_my_books_page(context)
    context.number_my_books = (context.my_books_page.
                               book_list.locator("li").count())


@then(u'ska antalet favoriter som visas överensstämma '
      u'med antalet i Mina böcker')
def step_compare_number_of_my_books_and_statistics(context):
    find_number = re.search(r"\d+", context.
                            statistics_page.stars_count.inner_text())

    number_stars_books = int(find_number.group())

    assert context.number_my_books == number_stars_books
