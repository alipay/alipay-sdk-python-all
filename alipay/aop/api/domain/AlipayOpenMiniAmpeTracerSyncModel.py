#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniAmpeTracerSyncModel(object):

    def __init__(self):
        self._device_id = None
        self._product_id = None
        self._spm_a = None
        self._spm_b = None
        self._spm_c = None
        self._spm_d = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def spm_a(self):
        return self._spm_a

    @spm_a.setter
    def spm_a(self, value):
        self._spm_a = value
    @property
    def spm_b(self):
        return self._spm_b

    @spm_b.setter
    def spm_b(self, value):
        self._spm_b = value
    @property
    def spm_c(self):
        return self._spm_c

    @spm_c.setter
    def spm_c(self, value):
        self._spm_c = value
    @property
    def spm_d(self):
        return self._spm_d

    @spm_d.setter
    def spm_d(self, value):
        self._spm_d = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.spm_a:
            if hasattr(self.spm_a, 'to_alipay_dict'):
                params['spm_a'] = self.spm_a.to_alipay_dict()
            else:
                params['spm_a'] = self.spm_a
        if self.spm_b:
            if hasattr(self.spm_b, 'to_alipay_dict'):
                params['spm_b'] = self.spm_b.to_alipay_dict()
            else:
                params['spm_b'] = self.spm_b
        if self.spm_c:
            if hasattr(self.spm_c, 'to_alipay_dict'):
                params['spm_c'] = self.spm_c.to_alipay_dict()
            else:
                params['spm_c'] = self.spm_c
        if self.spm_d:
            if hasattr(self.spm_d, 'to_alipay_dict'):
                params['spm_d'] = self.spm_d.to_alipay_dict()
            else:
                params['spm_d'] = self.spm_d
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniAmpeTracerSyncModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'spm_a' in d:
            o.spm_a = d['spm_a']
        if 'spm_b' in d:
            o.spm_b = d['spm_b']
        if 'spm_c' in d:
            o.spm_c = d['spm_c']
        if 'spm_d' in d:
            o.spm_d = d['spm_d']
        return o


