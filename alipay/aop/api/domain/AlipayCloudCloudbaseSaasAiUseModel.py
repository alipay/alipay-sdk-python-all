#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseSaasAiUseModel(object):

    def __init__(self):
        self._app_name = None
        self._attribute = None
        self._field_name = None
        self._param = None
        self._service_code = None
        self._uri = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value
    @property
    def field_name(self):
        return self._field_name

    @field_name.setter
    def field_name(self, value):
        self._field_name = value
    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, value):
        self._param = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def uri(self):
        return self._uri

    @uri.setter
    def uri(self, value):
        self._uri = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.attribute:
            if hasattr(self.attribute, 'to_alipay_dict'):
                params['attribute'] = self.attribute.to_alipay_dict()
            else:
                params['attribute'] = self.attribute
        if self.field_name:
            if hasattr(self.field_name, 'to_alipay_dict'):
                params['field_name'] = self.field_name.to_alipay_dict()
            else:
                params['field_name'] = self.field_name
        if self.param:
            if hasattr(self.param, 'to_alipay_dict'):
                params['param'] = self.param.to_alipay_dict()
            else:
                params['param'] = self.param
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.uri:
            if hasattr(self.uri, 'to_alipay_dict'):
                params['uri'] = self.uri.to_alipay_dict()
            else:
                params['uri'] = self.uri
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseSaasAiUseModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'attribute' in d:
            o.attribute = d['attribute']
        if 'field_name' in d:
            o.field_name = d['field_name']
        if 'param' in d:
            o.param = d['param']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'uri' in d:
            o.uri = d['uri']
        return o


