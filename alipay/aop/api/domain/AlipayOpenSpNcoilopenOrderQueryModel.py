#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNcoilopenOrderQueryModel(object):

    def __init__(self):
        self._reference_id = None

    @property
    def reference_id(self):
        return self._reference_id

    @reference_id.setter
    def reference_id(self, value):
        self._reference_id = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayOpenSpNcoilopenOrderQueryModel()
        if 'reference_id' in d:
            o.reference_id = d['reference_id']
        return o


