#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCommissionRuleCreateModel(object):

    def __init__(self):
        self._ant_shop_id = None
        self._charged_account_login_id = None
        self._charged_account_name = None
        self._commission_ratio = None
        self._end_date = None
        self._start_date = None

    @property
    def ant_shop_id(self):
        return self._ant_shop_id

    @ant_shop_id.setter
    def ant_shop_id(self, value):
        self._ant_shop_id = value
    @property
    def charged_account_login_id(self):
        return self._charged_account_login_id

    @charged_account_login_id.setter
    def charged_account_login_id(self, value):
        self._charged_account_login_id = value
    @property
    def charged_account_name(self):
        return self._charged_account_name

    @charged_account_name.setter
    def charged_account_name(self, value):
        self._charged_account_name = value
    @property
    def commission_ratio(self):
        return self._commission_ratio

    @commission_ratio.setter
    def commission_ratio(self, value):
        self._commission_ratio = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_shop_id:
            if hasattr(self.ant_shop_id, 'to_alipay_dict'):
                params['ant_shop_id'] = self.ant_shop_id.to_alipay_dict()
            else:
                params['ant_shop_id'] = self.ant_shop_id
        if self.charged_account_login_id:
            if hasattr(self.charged_account_login_id, 'to_alipay_dict'):
                params['charged_account_login_id'] = self.charged_account_login_id.to_alipay_dict()
            else:
                params['charged_account_login_id'] = self.charged_account_login_id
        if self.charged_account_name:
            if hasattr(self.charged_account_name, 'to_alipay_dict'):
                params['charged_account_name'] = self.charged_account_name.to_alipay_dict()
            else:
                params['charged_account_name'] = self.charged_account_name
        if self.commission_ratio:
            if hasattr(self.commission_ratio, 'to_alipay_dict'):
                params['commission_ratio'] = self.commission_ratio.to_alipay_dict()
            else:
                params['commission_ratio'] = self.commission_ratio
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCommissionRuleCreateModel()
        if 'ant_shop_id' in d:
            o.ant_shop_id = d['ant_shop_id']
        if 'charged_account_login_id' in d:
            o.charged_account_login_id = d['charged_account_login_id']
        if 'charged_account_name' in d:
            o.charged_account_name = d['charged_account_name']
        if 'commission_ratio' in d:
            o.commission_ratio = d['commission_ratio']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


