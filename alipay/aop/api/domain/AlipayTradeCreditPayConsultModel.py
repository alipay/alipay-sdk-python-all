#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeCreditPayConsultModel(object):

    def __init__(self):
        self._buyer_credit_source = None
        self._credit_scene = None
        self._merchant_credit_source = None
        self._trade_amount = None
        self._trade_buyer_id = None
        self._trade_seller_id = None

    @property
    def buyer_credit_source(self):
        return self._buyer_credit_source

    @buyer_credit_source.setter
    def buyer_credit_source(self, value):
        self._buyer_credit_source = value
    @property
    def credit_scene(self):
        return self._credit_scene

    @credit_scene.setter
    def credit_scene(self, value):
        self._credit_scene = value
    @property
    def merchant_credit_source(self):
        return self._merchant_credit_source

    @merchant_credit_source.setter
    def merchant_credit_source(self, value):
        self._merchant_credit_source = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_buyer_id(self):
        return self._trade_buyer_id

    @trade_buyer_id.setter
    def trade_buyer_id(self, value):
        self._trade_buyer_id = value
    @property
    def trade_seller_id(self):
        return self._trade_seller_id

    @trade_seller_id.setter
    def trade_seller_id(self, value):
        self._trade_seller_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_credit_source:
            if hasattr(self.buyer_credit_source, 'to_alipay_dict'):
                params['buyer_credit_source'] = self.buyer_credit_source.to_alipay_dict()
            else:
                params['buyer_credit_source'] = self.buyer_credit_source
        if self.credit_scene:
            if hasattr(self.credit_scene, 'to_alipay_dict'):
                params['credit_scene'] = self.credit_scene.to_alipay_dict()
            else:
                params['credit_scene'] = self.credit_scene
        if self.merchant_credit_source:
            if hasattr(self.merchant_credit_source, 'to_alipay_dict'):
                params['merchant_credit_source'] = self.merchant_credit_source.to_alipay_dict()
            else:
                params['merchant_credit_source'] = self.merchant_credit_source
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        if self.trade_buyer_id:
            if hasattr(self.trade_buyer_id, 'to_alipay_dict'):
                params['trade_buyer_id'] = self.trade_buyer_id.to_alipay_dict()
            else:
                params['trade_buyer_id'] = self.trade_buyer_id
        if self.trade_seller_id:
            if hasattr(self.trade_seller_id, 'to_alipay_dict'):
                params['trade_seller_id'] = self.trade_seller_id.to_alipay_dict()
            else:
                params['trade_seller_id'] = self.trade_seller_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeCreditPayConsultModel()
        if 'buyer_credit_source' in d:
            o.buyer_credit_source = d['buyer_credit_source']
        if 'credit_scene' in d:
            o.credit_scene = d['credit_scene']
        if 'merchant_credit_source' in d:
            o.merchant_credit_source = d['merchant_credit_source']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_buyer_id' in d:
            o.trade_buyer_id = d['trade_buyer_id']
        if 'trade_seller_id' in d:
            o.trade_seller_id = d['trade_seller_id']
        return o


