#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TemplateElementLinkDTO import TemplateElementLinkDTO


class AlipaySecurityProdTemplateVersioncontentSaveModel(object):

    def __init__(self):
        self._direct_publish = None
        self._emp_id = None
        self._file_key = None
        self._preview_address = None
        self._source_system_id = None
        self._template_code = None
        self._template_element_list = None
        self._tenant = None
        self._version_no = None

    @property
    def direct_publish(self):
        return self._direct_publish

    @direct_publish.setter
    def direct_publish(self, value):
        self._direct_publish = value
    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        self._emp_id = value
    @property
    def file_key(self):
        return self._file_key

    @file_key.setter
    def file_key(self, value):
        self._file_key = value
    @property
    def preview_address(self):
        return self._preview_address

    @preview_address.setter
    def preview_address(self, value):
        self._preview_address = value
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
    def template_element_list(self):
        return self._template_element_list

    @template_element_list.setter
    def template_element_list(self, value):
        if isinstance(value, list):
            self._template_element_list = list()
            for i in value:
                if isinstance(i, TemplateElementLinkDTO):
                    self._template_element_list.append(i)
                else:
                    self._template_element_list.append(TemplateElementLinkDTO.from_alipay_dict(i))
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.direct_publish:
            if hasattr(self.direct_publish, 'to_alipay_dict'):
                params['direct_publish'] = self.direct_publish.to_alipay_dict()
            else:
                params['direct_publish'] = self.direct_publish
        if self.emp_id:
            if hasattr(self.emp_id, 'to_alipay_dict'):
                params['emp_id'] = self.emp_id.to_alipay_dict()
            else:
                params['emp_id'] = self.emp_id
        if self.file_key:
            if hasattr(self.file_key, 'to_alipay_dict'):
                params['file_key'] = self.file_key.to_alipay_dict()
            else:
                params['file_key'] = self.file_key
        if self.preview_address:
            if hasattr(self.preview_address, 'to_alipay_dict'):
                params['preview_address'] = self.preview_address.to_alipay_dict()
            else:
                params['preview_address'] = self.preview_address
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
        if self.template_element_list:
            if isinstance(self.template_element_list, list):
                for i in range(0, len(self.template_element_list)):
                    element = self.template_element_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.template_element_list[i] = element.to_alipay_dict()
            if hasattr(self.template_element_list, 'to_alipay_dict'):
                params['template_element_list'] = self.template_element_list.to_alipay_dict()
            else:
                params['template_element_list'] = self.template_element_list
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        if self.version_no:
            if hasattr(self.version_no, 'to_alipay_dict'):
                params['version_no'] = self.version_no.to_alipay_dict()
            else:
                params['version_no'] = self.version_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdTemplateVersioncontentSaveModel()
        if 'direct_publish' in d:
            o.direct_publish = d['direct_publish']
        if 'emp_id' in d:
            o.emp_id = d['emp_id']
        if 'file_key' in d:
            o.file_key = d['file_key']
        if 'preview_address' in d:
            o.preview_address = d['preview_address']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'template_element_list' in d:
            o.template_element_list = d['template_element_list']
        if 'tenant' in d:
            o.tenant = d['tenant']
        if 'version_no' in d:
            o.version_no = d['version_no']
        return o


