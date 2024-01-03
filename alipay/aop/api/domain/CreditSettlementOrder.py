#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditSettlementOrder(object):

    def __init__(self):
        self._credit_biz_order_id = None
        self._origin_amount = None
        self._settle_amount = None
        self._target_order = None

    @property
    def credit_biz_order_id(self):
        return self._credit_biz_order_id

    @credit_biz_order_id.setter
    def credit_biz_order_id(self, value):
        self._credit_biz_order_id = value
    @property
    def origin_amount(self):
        return self._origin_amount

    @origin_amount.setter
    def origin_amount(self, value):
        self._origin_amount = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
    @property
    def target_order(self):
        return self._target_order

    @target_order.setter
    def target_order(self, value):
        self._target_order = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_biz_order_id:
            if hasattr(self.credit_biz_order_id, 'to_alipay_dict'):
                params['credit_biz_order_id'] = self.credit_biz_order_id.to_alipay_dict()
            else:
                params['credit_biz_order_id'] = self.credit_biz_order_id
        if self.origin_amount:
            if hasattr(self.origin_amount, 'to_alipay_dict'):
                params['origin_amount'] = self.origin_amount.to_alipay_dict()
            else:
                params['origin_amount'] = self.origin_amount
        if self.settle_amount:
            if hasattr(self.settle_amount, 'to_alipay_dict'):
                params['settle_amount'] = self.settle_amount.to_alipay_dict()
            else:
                params['settle_amount'] = self.settle_amount
        if self.target_order:
            if hasattr(self.target_order, 'to_alipay_dict'):
                params['target_order'] = self.target_order.to_alipay_dict()
            else:
                params['target_order'] = self.target_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditSettlementOrder()
        if 'credit_biz_order_id' in d:
            o.credit_biz_order_id = d['credit_biz_order_id']
        if 'origin_amount' in d:
            o.origin_amount = d['origin_amount']
        if 'settle_amount' in d:
            o.settle_amount = d['settle_amount']
        if 'target_order' in d:
            o.target_order = d['target_order']
        return o


