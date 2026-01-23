#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InteOpHtmlFiveInfo(object):

    def __init__(self):
        self._h_5_extra_pic = None
        self._h_5_home_screenshot = None
        self._h_5_item_screenshot = None
        self._h_5_memo = None
        self._h_5_pay_screenshot = None
        self._h_5_sites = None
        self._h_5_sites_loa = None
        self._h_5_status = None
        self._h_5_test_account = None
        self._h_5_test_account_password = None

    @property
    def h_5_extra_pic(self):
        return self._h_5_extra_pic

    @h_5_extra_pic.setter
    def h_5_extra_pic(self, value):
        self._h_5_extra_pic = value
    @property
    def h_5_home_screenshot(self):
        return self._h_5_home_screenshot

    @h_5_home_screenshot.setter
    def h_5_home_screenshot(self, value):
        self._h_5_home_screenshot = value
    @property
    def h_5_item_screenshot(self):
        return self._h_5_item_screenshot

    @h_5_item_screenshot.setter
    def h_5_item_screenshot(self, value):
        self._h_5_item_screenshot = value
    @property
    def h_5_memo(self):
        return self._h_5_memo

    @h_5_memo.setter
    def h_5_memo(self, value):
        self._h_5_memo = value
    @property
    def h_5_pay_screenshot(self):
        return self._h_5_pay_screenshot

    @h_5_pay_screenshot.setter
    def h_5_pay_screenshot(self, value):
        self._h_5_pay_screenshot = value
    @property
    def h_5_sites(self):
        return self._h_5_sites

    @h_5_sites.setter
    def h_5_sites(self, value):
        self._h_5_sites = value
    @property
    def h_5_sites_loa(self):
        return self._h_5_sites_loa

    @h_5_sites_loa.setter
    def h_5_sites_loa(self, value):
        self._h_5_sites_loa = value
    @property
    def h_5_status(self):
        return self._h_5_status

    @h_5_status.setter
    def h_5_status(self, value):
        self._h_5_status = value
    @property
    def h_5_test_account(self):
        return self._h_5_test_account

    @h_5_test_account.setter
    def h_5_test_account(self, value):
        self._h_5_test_account = value
    @property
    def h_5_test_account_password(self):
        return self._h_5_test_account_password

    @h_5_test_account_password.setter
    def h_5_test_account_password(self, value):
        self._h_5_test_account_password = value


    def to_alipay_dict(self):
        params = dict()
        if self.h_5_extra_pic:
            if hasattr(self.h_5_extra_pic, 'to_alipay_dict'):
                params['h_5_extra_pic'] = self.h_5_extra_pic.to_alipay_dict()
            else:
                params['h_5_extra_pic'] = self.h_5_extra_pic
        if self.h_5_home_screenshot:
            if hasattr(self.h_5_home_screenshot, 'to_alipay_dict'):
                params['h_5_home_screenshot'] = self.h_5_home_screenshot.to_alipay_dict()
            else:
                params['h_5_home_screenshot'] = self.h_5_home_screenshot
        if self.h_5_item_screenshot:
            if hasattr(self.h_5_item_screenshot, 'to_alipay_dict'):
                params['h_5_item_screenshot'] = self.h_5_item_screenshot.to_alipay_dict()
            else:
                params['h_5_item_screenshot'] = self.h_5_item_screenshot
        if self.h_5_memo:
            if hasattr(self.h_5_memo, 'to_alipay_dict'):
                params['h_5_memo'] = self.h_5_memo.to_alipay_dict()
            else:
                params['h_5_memo'] = self.h_5_memo
        if self.h_5_pay_screenshot:
            if hasattr(self.h_5_pay_screenshot, 'to_alipay_dict'):
                params['h_5_pay_screenshot'] = self.h_5_pay_screenshot.to_alipay_dict()
            else:
                params['h_5_pay_screenshot'] = self.h_5_pay_screenshot
        if self.h_5_sites:
            if hasattr(self.h_5_sites, 'to_alipay_dict'):
                params['h_5_sites'] = self.h_5_sites.to_alipay_dict()
            else:
                params['h_5_sites'] = self.h_5_sites
        if self.h_5_sites_loa:
            if hasattr(self.h_5_sites_loa, 'to_alipay_dict'):
                params['h_5_sites_loa'] = self.h_5_sites_loa.to_alipay_dict()
            else:
                params['h_5_sites_loa'] = self.h_5_sites_loa
        if self.h_5_status:
            if hasattr(self.h_5_status, 'to_alipay_dict'):
                params['h_5_status'] = self.h_5_status.to_alipay_dict()
            else:
                params['h_5_status'] = self.h_5_status
        if self.h_5_test_account:
            if hasattr(self.h_5_test_account, 'to_alipay_dict'):
                params['h_5_test_account'] = self.h_5_test_account.to_alipay_dict()
            else:
                params['h_5_test_account'] = self.h_5_test_account
        if self.h_5_test_account_password:
            if hasattr(self.h_5_test_account_password, 'to_alipay_dict'):
                params['h_5_test_account_password'] = self.h_5_test_account_password.to_alipay_dict()
            else:
                params['h_5_test_account_password'] = self.h_5_test_account_password
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InteOpHtmlFiveInfo()
        if 'h_5_extra_pic' in d:
            o.h_5_extra_pic = d['h_5_extra_pic']
        if 'h_5_home_screenshot' in d:
            o.h_5_home_screenshot = d['h_5_home_screenshot']
        if 'h_5_item_screenshot' in d:
            o.h_5_item_screenshot = d['h_5_item_screenshot']
        if 'h_5_memo' in d:
            o.h_5_memo = d['h_5_memo']
        if 'h_5_pay_screenshot' in d:
            o.h_5_pay_screenshot = d['h_5_pay_screenshot']
        if 'h_5_sites' in d:
            o.h_5_sites = d['h_5_sites']
        if 'h_5_sites_loa' in d:
            o.h_5_sites_loa = d['h_5_sites_loa']
        if 'h_5_status' in d:
            o.h_5_status = d['h_5_status']
        if 'h_5_test_account' in d:
            o.h_5_test_account = d['h_5_test_account']
        if 'h_5_test_account_password' in d:
            o.h_5_test_account_password = d['h_5_test_account_password']
        return o


