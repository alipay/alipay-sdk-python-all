#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CollectionFileDTO(object):

    def __init__(self):
        self._file_addr = None
        self._file_id = None
        self._file_should_save = None
        self._name = None
        self._operator = None
        self._prove_type = None
        self._source_sys = None
        self._tenant = None
        self._upload_time = None

    @property
    def file_addr(self):
        return self._file_addr

    @file_addr.setter
    def file_addr(self, value):
        self._file_addr = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_should_save(self):
        return self._file_should_save

    @file_should_save.setter
    def file_should_save(self, value):
        self._file_should_save = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def prove_type(self):
        return self._prove_type

    @prove_type.setter
    def prove_type(self, value):
        self._prove_type = value
    @property
    def source_sys(self):
        return self._source_sys

    @source_sys.setter
    def source_sys(self, value):
        self._source_sys = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
    @property
    def upload_time(self):
        return self._upload_time

    @upload_time.setter
    def upload_time(self, value):
        self._upload_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_addr:
            if hasattr(self.file_addr, 'to_alipay_dict'):
                params['file_addr'] = self.file_addr.to_alipay_dict()
            else:
                params['file_addr'] = self.file_addr
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.file_should_save:
            if hasattr(self.file_should_save, 'to_alipay_dict'):
                params['file_should_save'] = self.file_should_save.to_alipay_dict()
            else:
                params['file_should_save'] = self.file_should_save
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.prove_type:
            if hasattr(self.prove_type, 'to_alipay_dict'):
                params['prove_type'] = self.prove_type.to_alipay_dict()
            else:
                params['prove_type'] = self.prove_type
        if self.source_sys:
            if hasattr(self.source_sys, 'to_alipay_dict'):
                params['source_sys'] = self.source_sys.to_alipay_dict()
            else:
                params['source_sys'] = self.source_sys
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        if self.upload_time:
            if hasattr(self.upload_time, 'to_alipay_dict'):
                params['upload_time'] = self.upload_time.to_alipay_dict()
            else:
                params['upload_time'] = self.upload_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CollectionFileDTO()
        if 'file_addr' in d:
            o.file_addr = d['file_addr']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'file_should_save' in d:
            o.file_should_save = d['file_should_save']
        if 'name' in d:
            o.name = d['name']
        if 'operator' in d:
            o.operator = d['operator']
        if 'prove_type' in d:
            o.prove_type = d['prove_type']
        if 'source_sys' in d:
            o.source_sys = d['source_sys']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'upload_time' in d:
            o.upload_time = d['upload_time']
        return o


