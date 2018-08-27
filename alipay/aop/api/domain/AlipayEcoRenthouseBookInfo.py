#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoRenthouseBookInfo(object):

    def __init__(self):
        self._book_amount = None
        self._book_sale_amount = None
        self._latest_signing_date = None
        self._lease_begin_date = None
        self._lease_end_date = None
        self._remark = None

    @property
    def book_amount(self):
        return self._book_amount

    @book_amount.setter
    def book_amount(self, value):
        self._book_amount = value
    @property
    def book_sale_amount(self):
        return self._book_sale_amount

    @book_sale_amount.setter
    def book_sale_amount(self, value):
        self._book_sale_amount = value
    @property
    def latest_signing_date(self):
        return self._latest_signing_date

    @latest_signing_date.setter
    def latest_signing_date(self, value):
        self._latest_signing_date = value
    @property
    def lease_begin_date(self):
        return self._lease_begin_date

    @lease_begin_date.setter
    def lease_begin_date(self, value):
        self._lease_begin_date = value
    @property
    def lease_end_date(self):
        return self._lease_end_date

    @lease_end_date.setter
    def lease_end_date(self, value):
        self._lease_end_date = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.book_amount:
            if hasattr(self.book_amount, 'to_alipay_dict'):
                params['book_amount'] = self.book_amount.to_alipay_dict()
            else:
                params['book_amount'] = self.book_amount
        if self.book_sale_amount:
            if hasattr(self.book_sale_amount, 'to_alipay_dict'):
                params['book_sale_amount'] = self.book_sale_amount.to_alipay_dict()
            else:
                params['book_sale_amount'] = self.book_sale_amount
        if self.latest_signing_date:
            if hasattr(self.latest_signing_date, 'to_alipay_dict'):
                params['latest_signing_date'] = self.latest_signing_date.to_alipay_dict()
            else:
                params['latest_signing_date'] = self.latest_signing_date
        if self.lease_begin_date:
            if hasattr(self.lease_begin_date, 'to_alipay_dict'):
                params['lease_begin_date'] = self.lease_begin_date.to_alipay_dict()
            else:
                params['lease_begin_date'] = self.lease_begin_date
        if self.lease_end_date:
            if hasattr(self.lease_end_date, 'to_alipay_dict'):
                params['lease_end_date'] = self.lease_end_date.to_alipay_dict()
            else:
                params['lease_end_date'] = self.lease_end_date
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoRenthouseBookInfo()
        if 'book_amount' in d:
            o.book_amount = d['book_amount']
        if 'book_sale_amount' in d:
            o.book_sale_amount = d['book_sale_amount']
        if 'latest_signing_date' in d:
            o.latest_signing_date = d['latest_signing_date']
        if 'lease_begin_date' in d:
            o.lease_begin_date = d['lease_begin_date']
        if 'lease_end_date' in d:
            o.lease_end_date = d['lease_end_date']
        if 'remark' in d:
            o.remark = d['remark']
        return o


