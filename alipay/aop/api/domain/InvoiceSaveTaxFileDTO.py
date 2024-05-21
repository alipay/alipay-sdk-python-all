#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceSaveTaxFileDTO(object):

    def __init__(self):
        self._file_name = None
        self._file_size = None
        self._resource_id = None

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value
    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_size:
            if hasattr(self.file_size, 'to_alipay_dict'):
                params['file_size'] = self.file_size.to_alipay_dict()
            else:
                params['file_size'] = self.file_size
        if self.resource_id:
            if hasattr(self.resource_id, 'to_alipay_dict'):
                params['resource_id'] = self.resource_id.to_alipay_dict()
            else:
                params['resource_id'] = self.resource_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceSaveTaxFileDTO()
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_size' in d:
            o.file_size = d['file_size']
        if 'resource_id' in d:
            o.resource_id = d['resource_id']
        return o


