#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SimpleHospitalInfo(object):

    def __init__(self):
        self._hospital_id = None
        self._hospital_name = None

    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SimpleHospitalInfo()
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        return o


