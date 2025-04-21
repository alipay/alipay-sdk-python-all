#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrescriptionIdRelation(object):

    def __init__(self):
        self._prescription_code = None
        self._prescription_id = None

    @property
    def prescription_code(self):
        return self._prescription_code

    @prescription_code.setter
    def prescription_code(self, value):
        self._prescription_code = value
    @property
    def prescription_id(self):
        return self._prescription_id

    @prescription_id.setter
    def prescription_id(self, value):
        self._prescription_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.prescription_code:
            if hasattr(self.prescription_code, 'to_alipay_dict'):
                params['prescription_code'] = self.prescription_code.to_alipay_dict()
            else:
                params['prescription_code'] = self.prescription_code
        if self.prescription_id:
            if hasattr(self.prescription_id, 'to_alipay_dict'):
                params['prescription_id'] = self.prescription_id.to_alipay_dict()
            else:
                params['prescription_id'] = self.prescription_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrescriptionIdRelation()
        if 'prescription_code' in d:
            o.prescription_code = d['prescription_code']
        if 'prescription_id' in d:
            o.prescription_id = d['prescription_id']
        return o


