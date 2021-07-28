#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceInfo(object):

    def __init__(self):
        self._alipay_url = None
        self._audit_status = None
        self._biz_source = None
        self._detail_desc = None
        self._granularity_type = None
        self._key_words = None
        self._logo = None
        self._major_status = None
        self._ref_app_id = None
        self._ref_service_code = None
        self._service_code = None
        self._service_name = None
        self._simple_desc = None
        self._supplier_id = None
        self._supplier_type = None

    @property
    def alipay_url(self):
        return self._alipay_url

    @alipay_url.setter
    def alipay_url(self, value):
        self._alipay_url = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def biz_source(self):
        return self._biz_source

    @biz_source.setter
    def biz_source(self, value):
        self._biz_source = value
    @property
    def detail_desc(self):
        return self._detail_desc

    @detail_desc.setter
    def detail_desc(self, value):
        self._detail_desc = value
    @property
    def granularity_type(self):
        return self._granularity_type

    @granularity_type.setter
    def granularity_type(self, value):
        self._granularity_type = value
    @property
    def key_words(self):
        return self._key_words

    @key_words.setter
    def key_words(self, value):
        if isinstance(value, list):
            self._key_words = list()
            for i in value:
                self._key_words.append(i)
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def major_status(self):
        return self._major_status

    @major_status.setter
    def major_status(self, value):
        self._major_status = value
    @property
    def ref_app_id(self):
        return self._ref_app_id

    @ref_app_id.setter
    def ref_app_id(self, value):
        self._ref_app_id = value
    @property
    def ref_service_code(self):
        return self._ref_service_code

    @ref_service_code.setter
    def ref_service_code(self, value):
        self._ref_service_code = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def simple_desc(self):
        return self._simple_desc

    @simple_desc.setter
    def simple_desc(self, value):
        self._simple_desc = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def supplier_type(self):
        return self._supplier_type

    @supplier_type.setter
    def supplier_type(self, value):
        self._supplier_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_url:
            if hasattr(self.alipay_url, 'to_alipay_dict'):
                params['alipay_url'] = self.alipay_url.to_alipay_dict()
            else:
                params['alipay_url'] = self.alipay_url
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.biz_source:
            if hasattr(self.biz_source, 'to_alipay_dict'):
                params['biz_source'] = self.biz_source.to_alipay_dict()
            else:
                params['biz_source'] = self.biz_source
        if self.detail_desc:
            if hasattr(self.detail_desc, 'to_alipay_dict'):
                params['detail_desc'] = self.detail_desc.to_alipay_dict()
            else:
                params['detail_desc'] = self.detail_desc
        if self.granularity_type:
            if hasattr(self.granularity_type, 'to_alipay_dict'):
                params['granularity_type'] = self.granularity_type.to_alipay_dict()
            else:
                params['granularity_type'] = self.granularity_type
        if self.key_words:
            if isinstance(self.key_words, list):
                for i in range(0, len(self.key_words)):
                    element = self.key_words[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.key_words[i] = element.to_alipay_dict()
            if hasattr(self.key_words, 'to_alipay_dict'):
                params['key_words'] = self.key_words.to_alipay_dict()
            else:
                params['key_words'] = self.key_words
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.major_status:
            if hasattr(self.major_status, 'to_alipay_dict'):
                params['major_status'] = self.major_status.to_alipay_dict()
            else:
                params['major_status'] = self.major_status
        if self.ref_app_id:
            if hasattr(self.ref_app_id, 'to_alipay_dict'):
                params['ref_app_id'] = self.ref_app_id.to_alipay_dict()
            else:
                params['ref_app_id'] = self.ref_app_id
        if self.ref_service_code:
            if hasattr(self.ref_service_code, 'to_alipay_dict'):
                params['ref_service_code'] = self.ref_service_code.to_alipay_dict()
            else:
                params['ref_service_code'] = self.ref_service_code
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.simple_desc:
            if hasattr(self.simple_desc, 'to_alipay_dict'):
                params['simple_desc'] = self.simple_desc.to_alipay_dict()
            else:
                params['simple_desc'] = self.simple_desc
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.supplier_type:
            if hasattr(self.supplier_type, 'to_alipay_dict'):
                params['supplier_type'] = self.supplier_type.to_alipay_dict()
            else:
                params['supplier_type'] = self.supplier_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceInfo()
        if 'alipay_url' in d:
            o.alipay_url = d['alipay_url']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'biz_source' in d:
            o.biz_source = d['biz_source']
        if 'detail_desc' in d:
            o.detail_desc = d['detail_desc']
        if 'granularity_type' in d:
            o.granularity_type = d['granularity_type']
        if 'key_words' in d:
            o.key_words = d['key_words']
        if 'logo' in d:
            o.logo = d['logo']
        if 'major_status' in d:
            o.major_status = d['major_status']
        if 'ref_app_id' in d:
            o.ref_app_id = d['ref_app_id']
        if 'ref_service_code' in d:
            o.ref_service_code = d['ref_service_code']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'simple_desc' in d:
            o.simple_desc = d['simple_desc']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'supplier_type' in d:
            o.supplier_type = d['supplier_type']
        return o


