#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SortField(object):

    def __init__(self):
        self._field_code = None
        self._ort_by = None

    @property
    def field_code(self):
        return self._field_code

    @field_code.setter
    def field_code(self, value):
        self._field_code = value
    @property
    def ort_by(self):
        return self._ort_by

    @ort_by.setter
    def ort_by(self, value):
        self._ort_by = value


    def to_alipay_dict(self):
        params = dict()
        if self.field_code:
            if hasattr(self.field_code, 'to_alipay_dict'):
                params['field_code'] = self.field_code.to_alipay_dict()
            else:
                params['field_code'] = self.field_code
        if self.ort_by:
            if hasattr(self.ort_by, 'to_alipay_dict'):
                params['ort_by'] = self.ort_by.to_alipay_dict()
            else:
                params['ort_by'] = self.ort_by
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SortField()
        if 'field_code' in d:
            o.field_code = d['field_code']
        if 'ort_by' in d:
            o.ort_by = d['ort_by']
        return o


