#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InteOpWebSiteInfo(object):

    def __init__(self):
        self._web_home_screenshot = None
        self._web_item_screenshot = None
        self._web_pay_screenshot = None
        self._web_sites = None
        self._web_sites_loa = None
        self._web_status = None
        self._web_test_account = None
        self._web_test_account_password = None

    @property
    def web_home_screenshot(self):
        return self._web_home_screenshot

    @web_home_screenshot.setter
    def web_home_screenshot(self, value):
        self._web_home_screenshot = value
    @property
    def web_item_screenshot(self):
        return self._web_item_screenshot

    @web_item_screenshot.setter
    def web_item_screenshot(self, value):
        self._web_item_screenshot = value
    @property
    def web_pay_screenshot(self):
        return self._web_pay_screenshot

    @web_pay_screenshot.setter
    def web_pay_screenshot(self, value):
        self._web_pay_screenshot = value
    @property
    def web_sites(self):
        return self._web_sites

    @web_sites.setter
    def web_sites(self, value):
        self._web_sites = value
    @property
    def web_sites_loa(self):
        return self._web_sites_loa

    @web_sites_loa.setter
    def web_sites_loa(self, value):
        self._web_sites_loa = value
    @property
    def web_status(self):
        return self._web_status

    @web_status.setter
    def web_status(self, value):
        self._web_status = value
    @property
    def web_test_account(self):
        return self._web_test_account

    @web_test_account.setter
    def web_test_account(self, value):
        self._web_test_account = value
    @property
    def web_test_account_password(self):
        return self._web_test_account_password

    @web_test_account_password.setter
    def web_test_account_password(self, value):
        self._web_test_account_password = value


    def to_alipay_dict(self):
        params = dict()
        if self.web_home_screenshot:
            if hasattr(self.web_home_screenshot, 'to_alipay_dict'):
                params['web_home_screenshot'] = self.web_home_screenshot.to_alipay_dict()
            else:
                params['web_home_screenshot'] = self.web_home_screenshot
        if self.web_item_screenshot:
            if hasattr(self.web_item_screenshot, 'to_alipay_dict'):
                params['web_item_screenshot'] = self.web_item_screenshot.to_alipay_dict()
            else:
                params['web_item_screenshot'] = self.web_item_screenshot
        if self.web_pay_screenshot:
            if hasattr(self.web_pay_screenshot, 'to_alipay_dict'):
                params['web_pay_screenshot'] = self.web_pay_screenshot.to_alipay_dict()
            else:
                params['web_pay_screenshot'] = self.web_pay_screenshot
        if self.web_sites:
            if hasattr(self.web_sites, 'to_alipay_dict'):
                params['web_sites'] = self.web_sites.to_alipay_dict()
            else:
                params['web_sites'] = self.web_sites
        if self.web_sites_loa:
            if hasattr(self.web_sites_loa, 'to_alipay_dict'):
                params['web_sites_loa'] = self.web_sites_loa.to_alipay_dict()
            else:
                params['web_sites_loa'] = self.web_sites_loa
        if self.web_status:
            if hasattr(self.web_status, 'to_alipay_dict'):
                params['web_status'] = self.web_status.to_alipay_dict()
            else:
                params['web_status'] = self.web_status
        if self.web_test_account:
            if hasattr(self.web_test_account, 'to_alipay_dict'):
                params['web_test_account'] = self.web_test_account.to_alipay_dict()
            else:
                params['web_test_account'] = self.web_test_account
        if self.web_test_account_password:
            if hasattr(self.web_test_account_password, 'to_alipay_dict'):
                params['web_test_account_password'] = self.web_test_account_password.to_alipay_dict()
            else:
                params['web_test_account_password'] = self.web_test_account_password
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InteOpWebSiteInfo()
        if 'web_home_screenshot' in d:
            o.web_home_screenshot = d['web_home_screenshot']
        if 'web_item_screenshot' in d:
            o.web_item_screenshot = d['web_item_screenshot']
        if 'web_pay_screenshot' in d:
            o.web_pay_screenshot = d['web_pay_screenshot']
        if 'web_sites' in d:
            o.web_sites = d['web_sites']
        if 'web_sites_loa' in d:
            o.web_sites_loa = d['web_sites_loa']
        if 'web_status' in d:
            o.web_status = d['web_status']
        if 'web_test_account' in d:
            o.web_test_account = d['web_test_account']
        if 'web_test_account_password' in d:
            o.web_test_account_password = d['web_test_account_password']
        return o


