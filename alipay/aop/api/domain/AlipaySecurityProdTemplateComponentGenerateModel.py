#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdTemplateComponentGenerateModel(object):

    def __init__(self):
        self._component_category = None
        self._component_type = None
        self._emp_id = None
        self._enable_edit = None
        self._placeholder = None
        self._required = None
        self._source_system_id = None
        self._template_code = None
        self._template_version = None
        self._tenant = None

    @property
    def component_category(self):
        return self._component_category

    @component_category.setter
    def component_category(self, value):
        self._component_category = value
    @property
    def component_type(self):
        return self._component_type

    @component_type.setter
    def component_type(self, value):
        self._component_type = value
    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        self._emp_id = value
    @property
    def enable_edit(self):
        return self._enable_edit

    @enable_edit.setter
    def enable_edit(self, value):
        self._enable_edit = value
    @property
    def placeholder(self):
        return self._placeholder

    @placeholder.setter
    def placeholder(self, value):
        self._placeholder = value
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def template_version(self):
        return self._template_version

    @template_version.setter
    def template_version(self, value):
        self._template_version = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.component_category:
            if hasattr(self.component_category, 'to_alipay_dict'):
                params['component_category'] = self.component_category.to_alipay_dict()
            else:
                params['component_category'] = self.component_category
        if self.component_type:
            if hasattr(self.component_type, 'to_alipay_dict'):
                params['component_type'] = self.component_type.to_alipay_dict()
            else:
                params['component_type'] = self.component_type
        if self.emp_id:
            if hasattr(self.emp_id, 'to_alipay_dict'):
                params['emp_id'] = self.emp_id.to_alipay_dict()
            else:
                params['emp_id'] = self.emp_id
        if self.enable_edit:
            if hasattr(self.enable_edit, 'to_alipay_dict'):
                params['enable_edit'] = self.enable_edit.to_alipay_dict()
            else:
                params['enable_edit'] = self.enable_edit
        if self.placeholder:
            if hasattr(self.placeholder, 'to_alipay_dict'):
                params['placeholder'] = self.placeholder.to_alipay_dict()
            else:
                params['placeholder'] = self.placeholder
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        if self.source_system_id:
            if hasattr(self.source_system_id, 'to_alipay_dict'):
                params['source_system_id'] = self.source_system_id.to_alipay_dict()
            else:
                params['source_system_id'] = self.source_system_id
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.template_version:
            if hasattr(self.template_version, 'to_alipay_dict'):
                params['template_version'] = self.template_version.to_alipay_dict()
            else:
                params['template_version'] = self.template_version
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
        o = AlipaySecurityProdTemplateComponentGenerateModel()
        if 'component_category' in d:
            o.component_category = d['component_category']
        if 'component_type' in d:
            o.component_type = d['component_type']
        if 'emp_id' in d:
            o.emp_id = d['emp_id']
        if 'enable_edit' in d:
            o.enable_edit = d['enable_edit']
        if 'placeholder' in d:
            o.placeholder = d['placeholder']
        if 'required' in d:
            o.required = d['required']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'template_version' in d:
            o.template_version = d['template_version']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


