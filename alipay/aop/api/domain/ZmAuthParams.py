#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmAuthParams(object):

    def __init__(self):
        self._buckle_app_id = None
        self._buckle_merchant_id = None

    @property
    def buckle_app_id(self):
        return self._buckle_app_id

    @buckle_app_id.setter
    def buckle_app_id(self, value):
        self._buckle_app_id = value
    @property
    def buckle_merchant_id(self):
        return self._buckle_merchant_id

    @buckle_merchant_id.setter
    def buckle_merchant_id(self, value):
        self._buckle_merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.buckle_app_id:
            if hasattr(self.buckle_app_id, 'to_alipay_dict'):
                params['buckle_app_id'] = self.buckle_app_id.to_alipay_dict()
            else:
                params['buckle_app_id'] = self.buckle_app_id
        if self.buckle_merchant_id:
            if hasattr(self.buckle_merchant_id, 'to_alipay_dict'):
                params['buckle_merchant_id'] = self.buckle_merchant_id.to_alipay_dict()
            else:
                params['buckle_merchant_id'] = self.buckle_merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmAuthParams()
        if 'buckle_app_id' in d:
            o.buckle_app_id = d['buckle_app_id']
        if 'buckle_merchant_id' in d:
            o.buckle_merchant_id = d['buckle_merchant_id']
        return o


