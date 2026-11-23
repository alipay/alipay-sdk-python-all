#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AiPayConsultBizOrderRequest import AiPayConsultBizOrderRequest
from alipay.aop.api.domain.UserIdentityData import UserIdentityData


class AlipayAipayPaymentPreconsultModel(object):

    def __init__(self):
        self._biz_identity = None
        self._biz_order_list = None
        self._biz_scene = None
        self._merchant_discount_amount = None
        self._order_amount = None
        self._user_identity = None

    @property
    def biz_identity(self):
        return self._biz_identity

    @biz_identity.setter
    def biz_identity(self, value):
        self._biz_identity = value
    @property
    def biz_order_list(self):
        return self._biz_order_list

    @biz_order_list.setter
    def biz_order_list(self, value):
        if isinstance(value, list):
            self._biz_order_list = list()
            for i in value:
                if isinstance(i, AiPayConsultBizOrderRequest):
                    self._biz_order_list.append(i)
                else:
                    self._biz_order_list.append(AiPayConsultBizOrderRequest.from_alipay_dict(i))
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def merchant_discount_amount(self):
        return self._merchant_discount_amount

    @merchant_discount_amount.setter
    def merchant_discount_amount(self, value):
        self._merchant_discount_amount = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def user_identity(self):
        return self._user_identity

    @user_identity.setter
    def user_identity(self, value):
        if isinstance(value, UserIdentityData):
            self._user_identity = value
        else:
            self._user_identity = UserIdentityData.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_identity:
            if hasattr(self.biz_identity, 'to_alipay_dict'):
                params['biz_identity'] = self.biz_identity.to_alipay_dict()
            else:
                params['biz_identity'] = self.biz_identity
        if self.biz_order_list:
            if isinstance(self.biz_order_list, list):
                for i in range(0, len(self.biz_order_list)):
                    element = self.biz_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_order_list[i] = element.to_alipay_dict()
            if hasattr(self.biz_order_list, 'to_alipay_dict'):
                params['biz_order_list'] = self.biz_order_list.to_alipay_dict()
            else:
                params['biz_order_list'] = self.biz_order_list
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.merchant_discount_amount:
            if hasattr(self.merchant_discount_amount, 'to_alipay_dict'):
                params['merchant_discount_amount'] = self.merchant_discount_amount.to_alipay_dict()
            else:
                params['merchant_discount_amount'] = self.merchant_discount_amount
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.user_identity:
            if hasattr(self.user_identity, 'to_alipay_dict'):
                params['user_identity'] = self.user_identity.to_alipay_dict()
            else:
                params['user_identity'] = self.user_identity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAipayPaymentPreconsultModel()
        if 'biz_identity' in d:
            o.biz_identity = d['biz_identity']
        if 'biz_order_list' in d:
            o.biz_order_list = d['biz_order_list']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'merchant_discount_amount' in d:
            o.merchant_discount_amount = d['merchant_discount_amount']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'user_identity' in d:
            o.user_identity = d['user_identity']
        return o


