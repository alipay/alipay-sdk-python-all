#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreComplianceSignStatusQueryModel(object):

    def __init__(self):
        self._business_id = None
        self._file_code = None
        self._source_system_id = None

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def file_code(self):
        return self._file_code

    @file_code.setter
    def file_code(self, value):
        self._file_code = value
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.file_code:
            if hasattr(self.file_code, 'to_alipay_dict'):
                params['file_code'] = self.file_code.to_alipay_dict()
            else:
                params['file_code'] = self.file_code
        if self.source_system_id:
            if hasattr(self.source_system_id, 'to_alipay_dict'):
                params['source_system_id'] = self.source_system_id.to_alipay_dict()
            else:
                params['source_system_id'] = self.source_system_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceSignStatusQueryModel()
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'file_code' in d:
            o.file_code = d['file_code']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        return o


