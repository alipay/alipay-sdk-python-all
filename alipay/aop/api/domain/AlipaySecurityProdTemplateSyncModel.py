#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdTemplateSyncModel(object):

    def __init__(self):
        self._emp_id = None
        self._source_system_id = None
        self._source_template_code = None
        self._source_template_lib_code = None
        self._tenant = None
        self._tgt_template_code = None
        self._tgt_template_lib_code = None
        self._tgt_template_name = None

    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        self._emp_id = value
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value
    @property
    def source_template_code(self):
        return self._source_template_code

    @source_template_code.setter
    def source_template_code(self, value):
        self._source_template_code = value
    @property
    def source_template_lib_code(self):
        return self._source_template_lib_code

    @source_template_lib_code.setter
    def source_template_lib_code(self, value):
        self._source_template_lib_code = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
    @property
    def tgt_template_code(self):
        return self._tgt_template_code

    @tgt_template_code.setter
    def tgt_template_code(self, value):
        self._tgt_template_code = value
    @property
    def tgt_template_lib_code(self):
        return self._tgt_template_lib_code

    @tgt_template_lib_code.setter
    def tgt_template_lib_code(self, value):
        self._tgt_template_lib_code = value
    @property
    def tgt_template_name(self):
        return self._tgt_template_name

    @tgt_template_name.setter
    def tgt_template_name(self, value):
        self._tgt_template_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.emp_id:
            if hasattr(self.emp_id, 'to_alipay_dict'):
                params['emp_id'] = self.emp_id.to_alipay_dict()
            else:
                params['emp_id'] = self.emp_id
        if self.source_system_id:
            if hasattr(self.source_system_id, 'to_alipay_dict'):
                params['source_system_id'] = self.source_system_id.to_alipay_dict()
            else:
                params['source_system_id'] = self.source_system_id
        if self.source_template_code:
            if hasattr(self.source_template_code, 'to_alipay_dict'):
                params['source_template_code'] = self.source_template_code.to_alipay_dict()
            else:
                params['source_template_code'] = self.source_template_code
        if self.source_template_lib_code:
            if hasattr(self.source_template_lib_code, 'to_alipay_dict'):
                params['source_template_lib_code'] = self.source_template_lib_code.to_alipay_dict()
            else:
                params['source_template_lib_code'] = self.source_template_lib_code
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        if self.tgt_template_code:
            if hasattr(self.tgt_template_code, 'to_alipay_dict'):
                params['tgt_template_code'] = self.tgt_template_code.to_alipay_dict()
            else:
                params['tgt_template_code'] = self.tgt_template_code
        if self.tgt_template_lib_code:
            if hasattr(self.tgt_template_lib_code, 'to_alipay_dict'):
                params['tgt_template_lib_code'] = self.tgt_template_lib_code.to_alipay_dict()
            else:
                params['tgt_template_lib_code'] = self.tgt_template_lib_code
        if self.tgt_template_name:
            if hasattr(self.tgt_template_name, 'to_alipay_dict'):
                params['tgt_template_name'] = self.tgt_template_name.to_alipay_dict()
            else:
                params['tgt_template_name'] = self.tgt_template_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdTemplateSyncModel()
        if 'emp_id' in d:
            o.emp_id = d['emp_id']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'source_template_code' in d:
            o.source_template_code = d['source_template_code']
        if 'source_template_lib_code' in d:
            o.source_template_lib_code = d['source_template_lib_code']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'tgt_template_code' in d:
            o.tgt_template_code = d['tgt_template_code']
        if 'tgt_template_lib_code' in d:
            o.tgt_template_lib_code = d['tgt_template_lib_code']
        if 'tgt_template_name' in d:
            o.tgt_template_name = d['tgt_template_name']
        return o


