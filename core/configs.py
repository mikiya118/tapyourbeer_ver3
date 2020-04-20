# -*- coding: utf-8 -*-
"""
URL設定
"""
HOME_PAGE_TITLE_URL = 'home/page_title.html'
HOME_MAIN_URL = 'home/main_content.html'
HOME_SUB_URL = 'home/sub_content.html'

BEER_PAGE_TITLE_URL = 'beer/page_title.html'
BEER_MAIN_URL = 'beer/main_content.html'
BEER_SUB_URL = 'beer/sub_content.html'

ADD_BEER_EVALUATION_PAGE_TITLE_URL = 'beer/add_page_title.html'
ADD_BEER_EVALUATION_MAIN_URL = 'beer/add_main_content.html'

BREWERY_PAGE_TITLE_URL = 'brewery/page_title.html'
BREWERY_MAIN_URL = 'brewery/main_content.html'
BREWERY_SUB_URL = 'brewery/sub_content.html'

LOGIN_PAGE_TITLE_URL = 'login/page_title.html'
LOGIN_MAIN_URL = 'login/main_content.html'
LOGIN_SUB_URL = 'login/sub_content.html'

MANAGER_PAGE_TITLE_URL = 'manager/page_title.html'
MANAGER_MAIN_URL = 'manager/main_content.html'
MANAGER_SUB_URL = 'manager/sub_content.html'

SEARCH_PAGE_TITLE_URL = 'search/page_title.html'
SEARCH_MAIN_URL = 'search/main_content.html'
SEARCH_SUB_URL = 'search/sub_content.html'

USER_PAGE_TITLE_URL = 'user/page_title.html'
USER_MAIN_URL = 'user/main_content.html'
USER_SUB_URL = 'user/sub_content.html'

VENUE_PAGE_TITLE_URL = 'venue/page_title.html'
VENUE_MAIN_URL = 'venue/main_content.html'
VENUE_SUB_URL = 'venue/sub_content.html'

TOP_URL = '/main/'
TOP_PAGE_TITLE = HOME_PAGE_TITLE_URL
TOP_CONTENT_MAIN = HOME_MAIN_URL
TOP_CONTENT_SUB = HOME_SUB_URL


"""
アクションの設定
"""
ACTION_LOGIN = 'login'
ACTION_HOME = 'home'
ACTION_BEER_DETAIL = 'beer_detail'
ACTION_ADD_BEER_EVALUATION = 'add_beer_evaluation'
ACTION_BREWERY_DETAIL = 'brewery_detail'
ACTION_MANAGER_ACCOUNT = 'manager_account'
ACTION_SEARCH_LIST = 'search_list'
ACTION_USER_ACCOUNT = 'user_account'
ACTION_VENUE_DETAIL = 'venue_detail'

ACTION_DICT = {
                'ACTION_HOME':ACTION_HOME,
                'ACTION_LOGIN':ACTION_LOGIN,
                'ACTION_BEER_DETAIL':ACTION_BEER_DETAIL,
                'ACTION_ADD_BEER_EVALUATION':ACTION_ADD_BEER_EVALUATION,
                'ACTION_BREWERY_DETAIL':ACTION_BREWERY_DETAIL,
                'ACTION_MANAGER_ACCOUNT':ACTION_MANAGER_ACCOUNT,
                'ACTION_SEARCH_LIST':ACTION_SEARCH_LIST,
                'ACTION_USER_ACCOUNT':ACTION_USER_ACCOUNT,
                'ACTION_VENUE_DETAIL':ACTION_VENUE_DETAIL,
               }
"""
コンテンツHTML
"""
PAGE_TITLE = '/page_title.html'
CONTENT_MAIN = '/main_content.html'
CONTENT_SUB = '/sub_content.html'

"""
HTMLタイトル
"""
HOME_HTML_TITLE = 'Home'
LOGIN_HTML_TITLE = 'Login'
BEER_HTML_TITLE = 'Beer'
ADD_BEER_EVALUATION_HTML_TITLE = 'Add Beer'
BREWERY_HTML_TITLE = 'Brewery'
MANAGER_HTML_TITLE = 'Manager'
USER_HTML_TITLE = 'User'
SEARCH_HTML_TITLE = 'Search'
VENUE_HTML_TITLE = 'Venue'
