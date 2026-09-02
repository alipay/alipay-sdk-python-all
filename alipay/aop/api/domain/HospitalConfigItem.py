#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HospitalConfigItem(object):

    def __init__(self):
        self._code = None
        self._gray_config = None
        self._hospital_id = None
        self._org_id = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def gray_config(self):
        return self._gray_config

    @gray_config.setter
    def gray_config(self, value):
        self._gray_config = value
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.gray_config:
            if hasattr(self.gray_config, 'to_alipay_dict'):
                params['gray_config'] = self.gray_config.to_alipay_dict()
            else:
                params['gray_config'] = self.gray_config
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HospitalConfigItem()
        if 'code' in d:
            o.code = d['code']
        if 'gray_config' in d:
            o.gray_config = d['gray_config']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'org_id' in d:
            o.org_id = d['org_id']
        return o


