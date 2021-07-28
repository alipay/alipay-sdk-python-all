#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConversionDetail(object):

    def __init__(self):
        self._conversion_id = None
        self._conversion_name = None
        self._conversion_type = None
        self._conversion_type_name = None
        self._status = None

    @property
    def conversion_id(self):
        return self._conversion_id

    @conversion_id.setter
    def conversion_id(self, value):
        self._conversion_id = value
    @property
    def conversion_name(self):
        return self._conversion_name

    @conversion_name.setter
    def conversion_name(self, value):
        self._conversion_name = value
    @property
    def conversion_type(self):
        return self._conversion_type

    @conversion_type.setter
    def conversion_type(self, value):
        self._conversion_type = value
    @property
    def conversion_type_name(self):
        return self._conversion_type_name

    @conversion_type_name.setter
    def conversion_type_name(self, value):
        self._conversion_type_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.conversion_id:
            if hasattr(self.conversion_id, 'to_alipay_dict'):
                params['conversion_id'] = self.conversion_id.to_alipay_dict()
            else:
                params['conversion_id'] = self.conversion_id
        if self.conversion_name:
            if hasattr(self.conversion_name, 'to_alipay_dict'):
                params['conversion_name'] = self.conversion_name.to_alipay_dict()
            else:
                params['conversion_name'] = self.conversion_name
        if self.conversion_type:
            if hasattr(self.conversion_type, 'to_alipay_dict'):
                params['conversion_type'] = self.conversion_type.to_alipay_dict()
            else:
                params['conversion_type'] = self.conversion_type
        if self.conversion_type_name:
            if hasattr(self.conversion_type_name, 'to_alipay_dict'):
                params['conversion_type_name'] = self.conversion_type_name.to_alipay_dict()
            else:
                params['conversion_type_name'] = self.conversion_type_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConversionDetail()
        if 'conversion_id' in d:
            o.conversion_id = d['conversion_id']
        if 'conversion_name' in d:
            o.conversion_name = d['conversion_name']
        if 'conversion_type' in d:
            o.conversion_type = d['conversion_type']
        if 'conversion_type_name' in d:
            o.conversion_type_name = d['conversion_type_name']
        if 'status' in d:
            o.status = d['status']
        return o


