#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeRepaybillQueryModel(object):

    def __init__(self):
        self._bill_no = None
        self._bill_product = None
        self._out_bill_no = None
        self._user_id = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def bill_product(self):
        return self._bill_product

    @bill_product.setter
    def bill_product(self, value):
        self._bill_product = value
    @property
    def out_bill_no(self):
        return self._out_bill_no

    @out_bill_no.setter
    def out_bill_no(self, value):
        self._out_bill_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.bill_product:
            if hasattr(self.bill_product, 'to_alipay_dict'):
                params['bill_product'] = self.bill_product.to_alipay_dict()
            else:
                params['bill_product'] = self.bill_product
        if self.out_bill_no:
            if hasattr(self.out_bill_no, 'to_alipay_dict'):
                params['out_bill_no'] = self.out_bill_no.to_alipay_dict()
            else:
                params['out_bill_no'] = self.out_bill_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeRepaybillQueryModel()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_product' in d:
            o.bill_product = d['bill_product']
        if 'out_bill_no' in d:
            o.out_bill_no = d['out_bill_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


