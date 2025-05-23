#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayAppPocketmoneyAuthExpireModel(object):

    def __init__(self):
        self._device_id = None
        self._extra_device_id = None
        self._solution_vendor = None
        self._vendor_parent_id = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def extra_device_id(self):
        return self._extra_device_id

    @extra_device_id.setter
    def extra_device_id(self, value):
        self._extra_device_id = value
    @property
    def solution_vendor(self):
        return self._solution_vendor

    @solution_vendor.setter
    def solution_vendor(self, value):
        self._solution_vendor = value
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
        if self.extra_device_id:
            if hasattr(self.extra_device_id, 'to_alipay_dict'):
                params['extra_device_id'] = self.extra_device_id.to_alipay_dict()
            else:
                params['extra_device_id'] = self.extra_device_id
        if self.solution_vendor:
            if hasattr(self.solution_vendor, 'to_alipay_dict'):
                params['solution_vendor'] = self.solution_vendor.to_alipay_dict()
            else:
                params['solution_vendor'] = self.solution_vendor
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
        o = AlipayPayAppPocketmoneyAuthExpireModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'extra_device_id' in d:
            o.extra_device_id = d['extra_device_id']
        if 'solution_vendor' in d:
            o.solution_vendor = d['solution_vendor']
        if 'vendor_parent_id' in d:
            o.vendor_parent_id = d['vendor_parent_id']
        return o


