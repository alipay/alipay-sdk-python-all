#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InteOpAppInfo(object):

    def __init__(self):
        self._app_auth_pic = None
        self._app_download_link = None
        self._app_home_screenshot = None
        self._app_item_screenshot = None
        self._app_market = None
        self._app_name = None
        self._app_pay_screenshot = None
        self._app_status = None
        self._app_test_account = None
        self._app_test_account_password = None
        self._app_type = None
        self._in_app_screenshot = None

    @property
    def app_auth_pic(self):
        return self._app_auth_pic

    @app_auth_pic.setter
    def app_auth_pic(self, value):
        self._app_auth_pic = value
    @property
    def app_download_link(self):
        return self._app_download_link

    @app_download_link.setter
    def app_download_link(self, value):
        self._app_download_link = value
    @property
    def app_home_screenshot(self):
        return self._app_home_screenshot

    @app_home_screenshot.setter
    def app_home_screenshot(self, value):
        self._app_home_screenshot = value
    @property
    def app_item_screenshot(self):
        return self._app_item_screenshot

    @app_item_screenshot.setter
    def app_item_screenshot(self, value):
        self._app_item_screenshot = value
    @property
    def app_market(self):
        return self._app_market

    @app_market.setter
    def app_market(self, value):
        if isinstance(value, list):
            self._app_market = list()
            for i in value:
                self._app_market.append(i)
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_pay_screenshot(self):
        return self._app_pay_screenshot

    @app_pay_screenshot.setter
    def app_pay_screenshot(self, value):
        self._app_pay_screenshot = value
    @property
    def app_status(self):
        return self._app_status

    @app_status.setter
    def app_status(self, value):
        self._app_status = value
    @property
    def app_test_account(self):
        return self._app_test_account

    @app_test_account.setter
    def app_test_account(self, value):
        self._app_test_account = value
    @property
    def app_test_account_password(self):
        return self._app_test_account_password

    @app_test_account_password.setter
    def app_test_account_password(self, value):
        self._app_test_account_password = value
    @property
    def app_type(self):
        return self._app_type

    @app_type.setter
    def app_type(self, value):
        self._app_type = value
    @property
    def in_app_screenshot(self):
        return self._in_app_screenshot

    @in_app_screenshot.setter
    def in_app_screenshot(self, value):
        self._in_app_screenshot = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_auth_pic:
            if hasattr(self.app_auth_pic, 'to_alipay_dict'):
                params['app_auth_pic'] = self.app_auth_pic.to_alipay_dict()
            else:
                params['app_auth_pic'] = self.app_auth_pic
        if self.app_download_link:
            if hasattr(self.app_download_link, 'to_alipay_dict'):
                params['app_download_link'] = self.app_download_link.to_alipay_dict()
            else:
                params['app_download_link'] = self.app_download_link
        if self.app_home_screenshot:
            if hasattr(self.app_home_screenshot, 'to_alipay_dict'):
                params['app_home_screenshot'] = self.app_home_screenshot.to_alipay_dict()
            else:
                params['app_home_screenshot'] = self.app_home_screenshot
        if self.app_item_screenshot:
            if hasattr(self.app_item_screenshot, 'to_alipay_dict'):
                params['app_item_screenshot'] = self.app_item_screenshot.to_alipay_dict()
            else:
                params['app_item_screenshot'] = self.app_item_screenshot
        if self.app_market:
            if isinstance(self.app_market, list):
                for i in range(0, len(self.app_market)):
                    element = self.app_market[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_market[i] = element.to_alipay_dict()
            if hasattr(self.app_market, 'to_alipay_dict'):
                params['app_market'] = self.app_market.to_alipay_dict()
            else:
                params['app_market'] = self.app_market
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_pay_screenshot:
            if hasattr(self.app_pay_screenshot, 'to_alipay_dict'):
                params['app_pay_screenshot'] = self.app_pay_screenshot.to_alipay_dict()
            else:
                params['app_pay_screenshot'] = self.app_pay_screenshot
        if self.app_status:
            if hasattr(self.app_status, 'to_alipay_dict'):
                params['app_status'] = self.app_status.to_alipay_dict()
            else:
                params['app_status'] = self.app_status
        if self.app_test_account:
            if hasattr(self.app_test_account, 'to_alipay_dict'):
                params['app_test_account'] = self.app_test_account.to_alipay_dict()
            else:
                params['app_test_account'] = self.app_test_account
        if self.app_test_account_password:
            if hasattr(self.app_test_account_password, 'to_alipay_dict'):
                params['app_test_account_password'] = self.app_test_account_password.to_alipay_dict()
            else:
                params['app_test_account_password'] = self.app_test_account_password
        if self.app_type:
            if hasattr(self.app_type, 'to_alipay_dict'):
                params['app_type'] = self.app_type.to_alipay_dict()
            else:
                params['app_type'] = self.app_type
        if self.in_app_screenshot:
            if hasattr(self.in_app_screenshot, 'to_alipay_dict'):
                params['in_app_screenshot'] = self.in_app_screenshot.to_alipay_dict()
            else:
                params['in_app_screenshot'] = self.in_app_screenshot
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InteOpAppInfo()
        if 'app_auth_pic' in d:
            o.app_auth_pic = d['app_auth_pic']
        if 'app_download_link' in d:
            o.app_download_link = d['app_download_link']
        if 'app_home_screenshot' in d:
            o.app_home_screenshot = d['app_home_screenshot']
        if 'app_item_screenshot' in d:
            o.app_item_screenshot = d['app_item_screenshot']
        if 'app_market' in d:
            o.app_market = d['app_market']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_pay_screenshot' in d:
            o.app_pay_screenshot = d['app_pay_screenshot']
        if 'app_status' in d:
            o.app_status = d['app_status']
        if 'app_test_account' in d:
            o.app_test_account = d['app_test_account']
        if 'app_test_account_password' in d:
            o.app_test_account_password = d['app_test_account_password']
        if 'app_type' in d:
            o.app_type = d['app_type']
        if 'in_app_screenshot' in d:
            o.in_app_screenshot = d['in_app_screenshot']
        return o


