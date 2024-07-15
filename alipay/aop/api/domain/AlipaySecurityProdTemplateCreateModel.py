#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdTemplateCreateModel(object):

    def __init__(self):
        self._charge_name = None
        self._charge_no = None
        self._description = None
        self._emp_id = None
        self._file_address = None
        self._file_name = None
        self._participants = None
        self._source_system_id = None
        self._template_lib_code = None
        self._template_name = None
        self._tenant = None
        self._type = None

    @property
    def charge_name(self):
        return self._charge_name

    @charge_name.setter
    def charge_name(self, value):
        self._charge_name = value
    @property
    def charge_no(self):
        return self._charge_no

    @charge_no.setter
    def charge_no(self, value):
        self._charge_no = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        self._emp_id = value
    @property
    def file_address(self):
        return self._file_address

    @file_address.setter
    def file_address(self, value):
        self._file_address = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def participants(self):
        return self._participants

    @participants.setter
    def participants(self, value):
        if isinstance(value, list):
            self._participants = list()
            for i in value:
                self._participants.append(i)
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value
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
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.charge_name:
            if hasattr(self.charge_name, 'to_alipay_dict'):
                params['charge_name'] = self.charge_name.to_alipay_dict()
            else:
                params['charge_name'] = self.charge_name
        if self.charge_no:
            if hasattr(self.charge_no, 'to_alipay_dict'):
                params['charge_no'] = self.charge_no.to_alipay_dict()
            else:
                params['charge_no'] = self.charge_no
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.emp_id:
            if hasattr(self.emp_id, 'to_alipay_dict'):
                params['emp_id'] = self.emp_id.to_alipay_dict()
            else:
                params['emp_id'] = self.emp_id
        if self.file_address:
            if hasattr(self.file_address, 'to_alipay_dict'):
                params['file_address'] = self.file_address.to_alipay_dict()
            else:
                params['file_address'] = self.file_address
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.participants:
            if isinstance(self.participants, list):
                for i in range(0, len(self.participants)):
                    element = self.participants[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.participants[i] = element.to_alipay_dict()
            if hasattr(self.participants, 'to_alipay_dict'):
                params['participants'] = self.participants.to_alipay_dict()
            else:
                params['participants'] = self.participants
        if self.source_system_id:
            if hasattr(self.source_system_id, 'to_alipay_dict'):
                params['source_system_id'] = self.source_system_id.to_alipay_dict()
            else:
                params['source_system_id'] = self.source_system_id
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
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdTemplateCreateModel()
        if 'charge_name' in d:
            o.charge_name = d['charge_name']
        if 'charge_no' in d:
            o.charge_no = d['charge_no']
        if 'description' in d:
            o.description = d['description']
        if 'emp_id' in d:
            o.emp_id = d['emp_id']
        if 'file_address' in d:
            o.file_address = d['file_address']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'participants' in d:
            o.participants = d['participants']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'template_lib_code' in d:
            o.template_lib_code = d['template_lib_code']
        if 'template_name' in d:
            o.template_name = d['template_name']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'type' in d:
            o.type = d['type']
        return o


