#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OtherInfo(object):

    def __init__(self):
        self._medical_insurance = None

    @property
    def medical_insurance(self):
        return self._medical_insurance

    @medical_insurance.setter
    def medical_insurance(self, value):
        self._medical_insurance = value


    def to_alipay_dict(self):
        params = dict()
        if self.medical_insurance:
            if hasattr(self.medical_insurance, 'to_alipay_dict'):
                params['medical_insurance'] = self.medical_insurance.to_alipay_dict()
            else:
                params['medical_insurance'] = self.medical_insurance
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OtherInfo()
        if 'medical_insurance' in d:
            o.medical_insurance = d['medical_insurance']
        return o


