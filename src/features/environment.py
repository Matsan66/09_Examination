from playwright.sync_api import sync_playwright


# Runs before any scenarios
def before_all(context):
    # Start Playwright and the browser - close it in after_all
    context.playwright = sync_playwright().start()
    context.browser_type = context.playwright.chromium
    context.browser = context.browser_type.launch(headless=True)


# Runs at the start of each scenario
def before_scenario(context, scenario):
    # Open a new page, to prevent cookies to leak between tests.
    # # Set default timeout.
    context.page = context.browser.new_page()
    context.page.set_default_timeout(100)
    context.base_url = "https://tap-vt26-testautomatisering.github.io/exam/"


# Runs directly after each scenario
# Clean up to avoid memory leaks
def after_scenario(context, scenario):
    if context.page:
        context.page.close()


# Runs after all scenarios have finished
# Clean up
def after_all(context):
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()
