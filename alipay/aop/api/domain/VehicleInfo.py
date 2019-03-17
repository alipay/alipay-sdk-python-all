#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehicleInfo(object):

    def __init__(self):
        self._company_id = None
        self._vehicle_code = None
        self._vehicle_subject_code = None

    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        self._company_id = value
    @property
    def vehicle_code(self):
        return self._vehicle_code

    @vehicle_code.setter
    def vehicle_code(self, value):
        self._vehicle_code = value
    @property
    def vehicle_subject_code(self):
        return self._vehicle_subject_code

    @vehicle_subject_code.setter
    def vehicle_subject_code(self, value):
        self._vehicle_subject_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_id:
            if hasattr(self.company_id, 'to_alipay_dict'):
                params['company_id'] = self.company_id.to_alipay_dict()
            else:
                params['company_id'] = self.company_id
        if self.vehicle_code:
            if hasattr(self.vehicle_code, 'to_alipay_dict'):
                params['vehicle_code'] = self.vehicle_code.to_alipay_dict()
            else:
                params['vehicle_code'] = self.vehicle_code
        if self.vehicle_subject_code:
            if hasattr(self.vehicle_subject_code, 'to_alipay_dict'):
                params['vehicle_subject_code'] = self.vehicle_subject_code.to_alipay_dict()
            else:
                params['vehicle_subject_code'] = self.vehicle_subject_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehicleInfo()
        if 'company_id' in d:
            o.company_id = d['company_id']
        if 'vehicle_code' in d:
            o.vehicle_code = d['vehicle_code']
        if 'vehicle_subject_code' in d:
            o.vehicle_subject_code = d['vehicle_subject_code']
        return o


