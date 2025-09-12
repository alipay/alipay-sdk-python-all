#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiMerchantThirdactivityQueryModel(object):

    def __init__(self):
        self._goods_id = None
        self._invest_account = None
        self._order_amount = None

    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def invest_account(self):
        return self._invest_account

    @invest_account.setter
    def invest_account(self, value):
        self._invest_account = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.invest_account:
            if hasattr(self.invest_account, 'to_alipay_dict'):
                params['invest_account'] = self.invest_account.to_alipay_dict()
            else:
                params['invest_account'] = self.invest_account
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiMerchantThirdactivityQueryModel()
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'invest_account' in d:
            o.invest_account = d['invest_account']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        return o


