#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportIndustryPromoConsultModel(object):

    def __init__(self):
        self._industry_scene = None
        self._open_id = None
        self._order_amount = None
        self._partner_code = None
        self._sub_merchant_id = None
        self._user_id = None

    @property
    def industry_scene(self):
        return self._industry_scene

    @industry_scene.setter
    def industry_scene(self, value):
        self._industry_scene = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def partner_code(self):
        return self._partner_code

    @partner_code.setter
    def partner_code(self, value):
        self._partner_code = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.industry_scene:
            if hasattr(self.industry_scene, 'to_alipay_dict'):
                params['industry_scene'] = self.industry_scene.to_alipay_dict()
            else:
                params['industry_scene'] = self.industry_scene
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.partner_code:
            if hasattr(self.partner_code, 'to_alipay_dict'):
                params['partner_code'] = self.partner_code.to_alipay_dict()
            else:
                params['partner_code'] = self.partner_code
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
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
        o = AlipayCommerceTransportIndustryPromoConsultModel()
        if 'industry_scene' in d:
            o.industry_scene = d['industry_scene']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'partner_code' in d:
            o.partner_code = d['partner_code']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


