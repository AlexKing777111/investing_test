from investing_com_testing import SearchHelper


def test_investing_com(chrome_browser):
    investing_main_page = SearchHelper(chrome_browser)
    investing_main_page.go_to_site()
    investing_main_page.open_russian_stocks()
    investing_main_page.choice_stock_type()
    investing_main_page.choice_random_stock()
