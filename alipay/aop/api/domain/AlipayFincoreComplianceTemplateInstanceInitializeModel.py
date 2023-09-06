#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreComplianceTemplateInstanceInitializeModel(object):

    def __init__(self):
        self._biz_business_id = None
        self._biz_object_def_json = None
        self._idempotent = None
        self._need_file = None
        self._need_html = None
        self._source_system_id = None
        self._template_codes = None
        self._template_lib_code = None
        self._tenant = None

    @property
    def biz_business_id(self):
        return self._biz_business_id

    @biz_business_id.setter
    def biz_business_id(self, value):
        self._biz_business_id = value
    @property
    def biz_object_def_json(self):
        return self._biz_object_def_json

    @biz_object_def_json.setter
    def biz_object_def_json(self, value):
        self._biz_object_def_json = value
    @property
    def idempotent(self):
        return self._idempotent

    @idempotent.setter
    def idempotent(self, value):
        self._idempotent = value
    @property
    def need_file(self):
        return self._need_file

    @need_file.setter
    def need_file(self, value):
        self._need_file = value
    @property
    def need_html(self):
        return self._need_html

    @need_html.setter
    def need_html(self, value):
        self._need_html = value
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value
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
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_business_id:
            if hasattr(self.biz_business_id, 'to_alipay_dict'):
                params['biz_business_id'] = self.biz_business_id.to_alipay_dict()
            else:
                params['biz_business_id'] = self.biz_business_id
        if self.biz_object_def_json:
            if hasattr(self.biz_object_def_json, 'to_alipay_dict'):
                params['biz_object_def_json'] = self.biz_object_def_json.to_alipay_dict()
            else:
                params['biz_object_def_json'] = self.biz_object_def_json
        if self.idempotent:
            if hasattr(self.idempotent, 'to_alipay_dict'):
                params['idempotent'] = self.idempotent.to_alipay_dict()
            else:
                params['idempotent'] = self.idempotent
        if self.need_file:
            if hasattr(self.need_file, 'to_alipay_dict'):
                params['need_file'] = self.need_file.to_alipay_dict()
            else:
                params['need_file'] = self.need_file
        if self.need_html:
            if hasattr(self.need_html, 'to_alipay_dict'):
                params['need_html'] = self.need_html.to_alipay_dict()
            else:
                params['need_html'] = self.need_html
        if self.source_system_id:
            if hasattr(self.source_system_id, 'to_alipay_dict'):
                params['source_system_id'] = self.source_system_id.to_alipay_dict()
            else:
                params['source_system_id'] = self.source_system_id
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
        o = AlipayFincoreComplianceTemplateInstanceInitializeModel()
        if 'biz_business_id' in d:
            o.biz_business_id = d['biz_business_id']
        if 'biz_object_def_json' in d:
            o.biz_object_def_json = d['biz_object_def_json']
        if 'idempotent' in d:
            o.idempotent = d['idempotent']
        if 'need_file' in d:
            o.need_file = d['need_file']
        if 'need_html' in d:
            o.need_html = d['need_html']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'template_codes' in d:
            o.template_codes = d['template_codes']
        if 'template_lib_code' in d:
            o.template_lib_code = d['template_lib_code']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


