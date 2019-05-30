#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WaitRepaymentOrderInfo(object):

    def __init__(self):
        self._advance_order_id = None
        self._alipay_user_id = None
        self._biz_product = None
        self._orig_biz_order_id = None
        self._wait_repayment_amount = None

    @property
    def advance_order_id(self):
        return self._advance_order_id

    @advance_order_id.setter
    def advance_order_id(self, value):
        self._advance_order_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def orig_biz_order_id(self):
        return self._orig_biz_order_id

    @orig_biz_order_id.setter
    def orig_biz_order_id(self, value):
        self._orig_biz_order_id = value
    @property
    def wait_repayment_amount(self):
        return self._wait_repayment_amount

    @wait_repayment_amount.setter
    def wait_repayment_amount(self, value):
        self._wait_repayment_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.advance_order_id:
            if hasattr(self.advance_order_id, 'to_alipay_dict'):
                params['advance_order_id'] = self.advance_order_id.to_alipay_dict()
            else:
                params['advance_order_id'] = self.advance_order_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.orig_biz_order_id:
            if hasattr(self.orig_biz_order_id, 'to_alipay_dict'):
                params['orig_biz_order_id'] = self.orig_biz_order_id.to_alipay_dict()
            else:
                params['orig_biz_order_id'] = self.orig_biz_order_id
        if self.wait_repayment_amount:
            if hasattr(self.wait_repayment_amount, 'to_alipay_dict'):
                params['wait_repayment_amount'] = self.wait_repayment_amount.to_alipay_dict()
            else:
                params['wait_repayment_amount'] = self.wait_repayment_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WaitRepaymentOrderInfo()
        if 'advance_order_id' in d:
            o.advance_order_id = d['advance_order_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'orig_biz_order_id' in d:
            o.orig_biz_order_id = d['orig_biz_order_id']
        if 'wait_repayment_amount' in d:
            o.wait_repayment_amount = d['wait_repayment_amount']
        return o


