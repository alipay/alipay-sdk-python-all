#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtEcmcoreDataarchivesCreateModel(object):

    def __init__(self):
        self._business_code = None
        self._checksum = None
        self._checksum_type = None
        self._data_desc = None
        self._data_id = None
        self._data_path = None
        self._system_code = None
        self._system_heading = None
        self._unit_code = None
        self._unit_heading = None

    @property
    def business_code(self):
        return self._business_code

    @business_code.setter
    def business_code(self, value):
        self._business_code = value
    @property
    def checksum(self):
        return self._checksum

    @checksum.setter
    def checksum(self, value):
        self._checksum = value
    @property
    def checksum_type(self):
        return self._checksum_type

    @checksum_type.setter
    def checksum_type(self, value):
        self._checksum_type = value
    @property
    def data_desc(self):
        return self._data_desc

    @data_desc.setter
    def data_desc(self, value):
        self._data_desc = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def data_path(self):
        return self._data_path

    @data_path.setter
    def data_path(self, value):
        self._data_path = value
    @property
    def system_code(self):
        return self._system_code

    @system_code.setter
    def system_code(self, value):
        self._system_code = value
    @property
    def system_heading(self):
        return self._system_heading

    @system_heading.setter
    def system_heading(self, value):
        self._system_heading = value
    @property
    def unit_code(self):
        return self._unit_code

    @unit_code.setter
    def unit_code(self, value):
        self._unit_code = value
    @property
    def unit_heading(self):
        return self._unit_heading

    @unit_heading.setter
    def unit_heading(self, value):
        self._unit_heading = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_code:
            if hasattr(self.business_code, 'to_alipay_dict'):
                params['business_code'] = self.business_code.to_alipay_dict()
            else:
                params['business_code'] = self.business_code
        if self.checksum:
            if hasattr(self.checksum, 'to_alipay_dict'):
                params['checksum'] = self.checksum.to_alipay_dict()
            else:
                params['checksum'] = self.checksum
        if self.checksum_type:
            if hasattr(self.checksum_type, 'to_alipay_dict'):
                params['checksum_type'] = self.checksum_type.to_alipay_dict()
            else:
                params['checksum_type'] = self.checksum_type
        if self.data_desc:
            if hasattr(self.data_desc, 'to_alipay_dict'):
                params['data_desc'] = self.data_desc.to_alipay_dict()
            else:
                params['data_desc'] = self.data_desc
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.data_path:
            if hasattr(self.data_path, 'to_alipay_dict'):
                params['data_path'] = self.data_path.to_alipay_dict()
            else:
                params['data_path'] = self.data_path
        if self.system_code:
            if hasattr(self.system_code, 'to_alipay_dict'):
                params['system_code'] = self.system_code.to_alipay_dict()
            else:
                params['system_code'] = self.system_code
        if self.system_heading:
            if hasattr(self.system_heading, 'to_alipay_dict'):
                params['system_heading'] = self.system_heading.to_alipay_dict()
            else:
                params['system_heading'] = self.system_heading
        if self.unit_code:
            if hasattr(self.unit_code, 'to_alipay_dict'):
                params['unit_code'] = self.unit_code.to_alipay_dict()
            else:
                params['unit_code'] = self.unit_code
        if self.unit_heading:
            if hasattr(self.unit_heading, 'to_alipay_dict'):
                params['unit_heading'] = self.unit_heading.to_alipay_dict()
            else:
                params['unit_heading'] = self.unit_heading
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtEcmcoreDataarchivesCreateModel()
        if 'business_code' in d:
            o.business_code = d['business_code']
        if 'checksum' in d:
            o.checksum = d['checksum']
        if 'checksum_type' in d:
            o.checksum_type = d['checksum_type']
        if 'data_desc' in d:
            o.data_desc = d['data_desc']
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'data_path' in d:
            o.data_path = d['data_path']
        if 'system_code' in d:
            o.system_code = d['system_code']
        if 'system_heading' in d:
            o.system_heading = d['system_heading']
        if 'unit_code' in d:
            o.unit_code = d['unit_code']
        if 'unit_heading' in d:
            o.unit_heading = d['unit_heading']
        return o


