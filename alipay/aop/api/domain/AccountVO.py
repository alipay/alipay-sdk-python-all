#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccountVO(object):

    def __init__(self):
        self._account_name = None
        self._account_no = None
        self._category = None
        self._last_pay_fail = None
        self._offical_name = None
        self._offical_number = None
        self._status = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def last_pay_fail(self):
        return self._last_pay_fail

    @last_pay_fail.setter
    def last_pay_fail(self, value):
        self._last_pay_fail = value
    @property
    def offical_name(self):
        return self._offical_name

    @offical_name.setter
    def offical_name(self, value):
        self._offical_name = value
    @property
    def offical_number(self):
        return self._offical_number

    @offical_number.setter
    def offical_number(self, value):
        self._offical_number = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.last_pay_fail:
            if hasattr(self.last_pay_fail, 'to_alipay_dict'):
                params['last_pay_fail'] = self.last_pay_fail.to_alipay_dict()
            else:
                params['last_pay_fail'] = self.last_pay_fail
        if self.offical_name:
            if hasattr(self.offical_name, 'to_alipay_dict'):
                params['offical_name'] = self.offical_name.to_alipay_dict()
            else:
                params['offical_name'] = self.offical_name
        if self.offical_number:
            if hasattr(self.offical_number, 'to_alipay_dict'):
                params['offical_number'] = self.offical_number.to_alipay_dict()
            else:
                params['offical_number'] = self.offical_number
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccountVO()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'category' in d:
            o.category = d['category']
        if 'last_pay_fail' in d:
            o.last_pay_fail = d['last_pay_fail']
        if 'offical_name' in d:
            o.offical_name = d['offical_name']
        if 'offical_number' in d:
            o.offical_number = d['offical_number']
        if 'status' in d:
            o.status = d['status']
        return o


