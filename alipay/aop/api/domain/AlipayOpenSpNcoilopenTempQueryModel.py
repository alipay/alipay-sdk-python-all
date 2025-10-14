#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNcoilopenTempQueryModel(object):

    def __init__(self):
        self._record_id = None
        self._reference_id = None

    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def reference_id(self):
        return self._reference_id

    @reference_id.setter
    def reference_id(self, value):
        self._reference_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.reference_id:
            if hasattr(self.reference_id, 'to_alipay_dict'):
                params['reference_id'] = self.reference_id.to_alipay_dict()
            else:
                params['reference_id'] = self.reference_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNcoilopenTempQueryModel()
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'reference_id' in d:
            o.reference_id = d['reference_id']
        return o


