#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayAppPocketmoneyAuthQueryModel(object):

    def __init__(self):
        self._device_id = None
        self._vendor_parent_id = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def vendor_parent_id(self):
        return self._vendor_parent_id

    @vendor_parent_id.setter
    def vendor_parent_id(self, value):
        self._vendor_parent_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.vendor_parent_id:
            if hasattr(self.vendor_parent_id, 'to_alipay_dict'):
                params['vendor_parent_id'] = self.vendor_parent_id.to_alipay_dict()
            else:
                params['vendor_parent_id'] = self.vendor_parent_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayAppPocketmoneyAuthQueryModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'vendor_parent_id' in d:
            o.vendor_parent_id = d['vendor_parent_id']
        return o


