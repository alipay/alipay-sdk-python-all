#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdTemplateBatchqueryModel(object):

    def __init__(self):
        self._emp_id = None
        self._source_system_id = None
        self._status = None
        self._template_codes = None
        self._template_lib_code = None
        self._template_name = None
        self._tenant = None

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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_codes(self):
        return self._template_codes

    @template_codes.setter
    def template_codes(self, value):
        if isinstance(value, list):
            self._template_codes = list()
            for i in value:
                self._template_codes.append(i)
    @property
    def template_lib_code(self):
        return self._template_lib_code

    @template_lib_code.setter
    def template_lib_code(self, value):
        self._template_lib_code = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_codes:
            if isinstance(self.template_codes, list):
                for i in range(0, len(self.template_codes)):
                    element = self.template_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.template_codes[i] = element.to_alipay_dict()
            if hasattr(self.template_codes, 'to_alipay_dict'):
                params['template_codes'] = self.template_codes.to_alipay_dict()
            else:
                params['template_codes'] = self.template_codes
        if self.template_lib_code:
            if hasattr(self.template_lib_code, 'to_alipay_dict'):
                params['template_lib_code'] = self.template_lib_code.to_alipay_dict()
            else:
                params['template_lib_code'] = self.template_lib_code
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdTemplateBatchqueryModel()
        if 'emp_id' in d:
            o.emp_id = d['emp_id']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'status' in d:
            o.status = d['status']
        if 'template_codes' in d:
            o.template_codes = d['template_codes']
        if 'template_lib_code' in d:
            o.template_lib_code = d['template_lib_code']
        if 'template_name' in d:
            o.template_name = d['template_name']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


