#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenNppdUserpointQueryModel(object):

    def __init__(self):
        self._merchant_code = None
        self._merchant_exts = None
        self._open_id = None
        self._user_id = None

    @property
    def merchant_code(self):
        return self._merchant_code

    @merchant_code.setter
    def merchant_code(self, value):
        self._merchant_code = value
    @property
    def merchant_exts(self):
        return self._merchant_exts

    @merchant_exts.setter
    def merchant_exts(self, value):
        self._merchant_exts = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_code:
            if hasattr(self.merchant_code, 'to_alipay_dict'):
                params['merchant_code'] = self.merchant_code.to_alipay_dict()
            else:
                params['merchant_code'] = self.merchant_code
        if self.merchant_exts:
            if hasattr(self.merchant_exts, 'to_alipay_dict'):
                params['merchant_exts'] = self.merchant_exts.to_alipay_dict()
            else:
                params['merchant_exts'] = self.merchant_exts
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = AlipayOpenNppdUserpointQueryModel()
        if 'merchant_code' in d:
            o.merchant_code = d['merchant_code']
        if 'merchant_exts' in d:
            o.merchant_exts = d['merchant_exts']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


