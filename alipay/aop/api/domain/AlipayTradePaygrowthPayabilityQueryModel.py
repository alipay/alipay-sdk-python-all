#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradePaygrowthPayabilityQueryModel(object):

    def __init__(self):
        self._biz_identity = None
        self._real_pay_amount = None
        self._request_from = None
        self._user_id = None

    @property
    def biz_identity(self):
        return self._biz_identity

    @biz_identity.setter
    def biz_identity(self, value):
        self._biz_identity = value
    @property
    def real_pay_amount(self):
        return self._real_pay_amount

    @real_pay_amount.setter
    def real_pay_amount(self, value):
        self._real_pay_amount = value
    @property
    def request_from(self):
        return self._request_from

    @request_from.setter
    def request_from(self, value):
        self._request_from = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_identity:
            if hasattr(self.biz_identity, 'to_alipay_dict'):
                params['biz_identity'] = self.biz_identity.to_alipay_dict()
            else:
                params['biz_identity'] = self.biz_identity
        if self.real_pay_amount:
            if hasattr(self.real_pay_amount, 'to_alipay_dict'):
                params['real_pay_amount'] = self.real_pay_amount.to_alipay_dict()
            else:
                params['real_pay_amount'] = self.real_pay_amount
        if self.request_from:
            if hasattr(self.request_from, 'to_alipay_dict'):
                params['request_from'] = self.request_from.to_alipay_dict()
            else:
                params['request_from'] = self.request_from
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
        o = AlipayTradePaygrowthPayabilityQueryModel()
        if 'biz_identity' in d:
            o.biz_identity = d['biz_identity']
        if 'real_pay_amount' in d:
            o.real_pay_amount = d['real_pay_amount']
        if 'request_from' in d:
            o.request_from = d['request_from']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


