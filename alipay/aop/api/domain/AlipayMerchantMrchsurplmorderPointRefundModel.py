#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantMrchsurplmorderPointRefundModel(object):

    def __init__(self):
        self._biz_id = None
        self._deducted_request_id = None
        self._lm_order_id = None
        self._request_id = None
        self._user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def deducted_request_id(self):
        return self._deducted_request_id

    @deducted_request_id.setter
    def deducted_request_id(self, value):
        self._deducted_request_id = value
    @property
    def lm_order_id(self):
        return self._lm_order_id

    @lm_order_id.setter
    def lm_order_id(self, value):
        self._lm_order_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.deducted_request_id:
            if hasattr(self.deducted_request_id, 'to_alipay_dict'):
                params['deducted_request_id'] = self.deducted_request_id.to_alipay_dict()
            else:
                params['deducted_request_id'] = self.deducted_request_id
        if self.lm_order_id:
            if hasattr(self.lm_order_id, 'to_alipay_dict'):
                params['lm_order_id'] = self.lm_order_id.to_alipay_dict()
            else:
                params['lm_order_id'] = self.lm_order_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
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
        o = AlipayMerchantMrchsurplmorderPointRefundModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'deducted_request_id' in d:
            o.deducted_request_id = d['deducted_request_id']
        if 'lm_order_id' in d:
            o.lm_order_id = d['lm_order_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


