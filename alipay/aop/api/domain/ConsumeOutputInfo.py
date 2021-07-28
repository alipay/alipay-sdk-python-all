#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsumeOutputInfo(object):

    def __init__(self):
        self._bill_no = None
        self._category_name = None
        self._consume_amount = None
        self._consume_date = None
        self._consume_title = None
        self._payee_name = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def consume_amount(self):
        return self._consume_amount

    @consume_amount.setter
    def consume_amount(self, value):
        self._consume_amount = value
    @property
    def consume_date(self):
        return self._consume_date

    @consume_date.setter
    def consume_date(self, value):
        self._consume_date = value
    @property
    def consume_title(self):
        return self._consume_title

    @consume_title.setter
    def consume_title(self, value):
        self._consume_title = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.consume_amount:
            if hasattr(self.consume_amount, 'to_alipay_dict'):
                params['consume_amount'] = self.consume_amount.to_alipay_dict()
            else:
                params['consume_amount'] = self.consume_amount
        if self.consume_date:
            if hasattr(self.consume_date, 'to_alipay_dict'):
                params['consume_date'] = self.consume_date.to_alipay_dict()
            else:
                params['consume_date'] = self.consume_date
        if self.consume_title:
            if hasattr(self.consume_title, 'to_alipay_dict'):
                params['consume_title'] = self.consume_title.to_alipay_dict()
            else:
                params['consume_title'] = self.consume_title
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = self.payee_name.to_alipay_dict()
            else:
                params['payee_name'] = self.payee_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumeOutputInfo()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'consume_amount' in d:
            o.consume_amount = d['consume_amount']
        if 'consume_date' in d:
            o.consume_date = d['consume_date']
        if 'consume_title' in d:
            o.consume_title = d['consume_title']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        return o


