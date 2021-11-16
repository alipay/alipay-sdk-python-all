#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReferenceId(object):

    def __init__(self):
        self._reference_id = None
        self._reference_id_type = None

    @property
    def reference_id(self):
        return self._reference_id

    @reference_id.setter
    def reference_id(self, value):
        self._reference_id = value
    @property
    def reference_id_type(self):
        return self._reference_id_type

    @reference_id_type.setter
    def reference_id_type(self, value):
        self._reference_id_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.reference_id:
            if hasattr(self.reference_id, 'to_alipay_dict'):
                params['reference_id'] = self.reference_id.to_alipay_dict()
            else:
                params['reference_id'] = self.reference_id
        if self.reference_id_type:
            if hasattr(self.reference_id_type, 'to_alipay_dict'):
                params['reference_id_type'] = self.reference_id_type.to_alipay_dict()
            else:
                params['reference_id_type'] = self.reference_id_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReferenceId()
        if 'reference_id' in d:
            o.reference_id = d['reference_id']
        if 'reference_id_type' in d:
            o.reference_id_type = d['reference_id_type']
        return o


