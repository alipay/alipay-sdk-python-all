#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HospitalDTO(object):

    def __init__(self):
        self._hospital_id = None
        self._hospital_name = None
        self._level = None
        self._ownership = None

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
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def ownership(self):
        return self._ownership

    @ownership.setter
    def ownership(self, value):
        self._ownership = value


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
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.ownership:
            if hasattr(self.ownership, 'to_alipay_dict'):
                params['ownership'] = self.ownership.to_alipay_dict()
            else:
                params['ownership'] = self.ownership
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HospitalDTO()
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'level' in d:
            o.level = d['level']
        if 'ownership' in d:
            o.ownership = d['ownership']
        return o


