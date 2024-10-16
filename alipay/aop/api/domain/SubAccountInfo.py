#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubAccountInfo(object):

    def __init__(self):
        self._sub_merchant_id = None
        self._sub_merchant_type = None

    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value
    @property
    def sub_merchant_type(self):
        return self._sub_merchant_type

    @sub_merchant_type.setter
    def sub_merchant_type(self, value):
        self._sub_merchant_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        if self.sub_merchant_type:
            if hasattr(self.sub_merchant_type, 'to_alipay_dict'):
                params['sub_merchant_type'] = self.sub_merchant_type.to_alipay_dict()
            else:
                params['sub_merchant_type'] = self.sub_merchant_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubAccountInfo()
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        if 'sub_merchant_type' in d:
            o.sub_merchant_type = d['sub_merchant_type']
        return o


