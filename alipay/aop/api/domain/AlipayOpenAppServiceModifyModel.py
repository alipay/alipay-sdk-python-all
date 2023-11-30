#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppServiceModifyModel(object):

    def __init__(self):
        self._schema_version = None
        self._service_code = None
        self._service_xml = None
        self._template_type = None
        self._user_service_delivery_type = None

    @property
    def schema_version(self):
        return self._schema_version

    @schema_version.setter
    def schema_version(self, value):
        self._schema_version = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_xml(self):
        return self._service_xml

    @service_xml.setter
    def service_xml(self, value):
        self._service_xml = value
    @property
    def template_type(self):
        return self._template_type

    @template_type.setter
    def template_type(self, value):
        self._template_type = value
    @property
    def user_service_delivery_type(self):
        return self._user_service_delivery_type

    @user_service_delivery_type.setter
    def user_service_delivery_type(self, value):
        self._user_service_delivery_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.schema_version:
            if hasattr(self.schema_version, 'to_alipay_dict'):
                params['schema_version'] = self.schema_version.to_alipay_dict()
            else:
                params['schema_version'] = self.schema_version
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_xml:
            if hasattr(self.service_xml, 'to_alipay_dict'):
                params['service_xml'] = self.service_xml.to_alipay_dict()
            else:
                params['service_xml'] = self.service_xml
        if self.template_type:
            if hasattr(self.template_type, 'to_alipay_dict'):
                params['template_type'] = self.template_type.to_alipay_dict()
            else:
                params['template_type'] = self.template_type
        if self.user_service_delivery_type:
            if hasattr(self.user_service_delivery_type, 'to_alipay_dict'):
                params['user_service_delivery_type'] = self.user_service_delivery_type.to_alipay_dict()
            else:
                params['user_service_delivery_type'] = self.user_service_delivery_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppServiceModifyModel()
        if 'schema_version' in d:
            o.schema_version = d['schema_version']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_xml' in d:
            o.service_xml = d['service_xml']
        if 'template_type' in d:
            o.template_type = d['template_type']
        if 'user_service_delivery_type' in d:
            o.user_service_delivery_type = d['user_service_delivery_type']
        return o


