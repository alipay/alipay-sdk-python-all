#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserElectronicidMerchantbarcodeCreateModel(object):

    def __init__(self):
        self._expire_time = None
        self._type = None
        self._unique_id = None

    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserElectronicidMerchantbarcodeCreateModel()
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'type' in d:
            o.type = d['type']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        return o


