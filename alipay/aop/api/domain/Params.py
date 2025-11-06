#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Params(object):

    def __init__(self):
        self._callback_type = None
        self._out_string = None
        self._provider_application_id = None
        self._provider_id = None
        self._regist_alipay_schema = None
        self._regist_mode = None
        self._template_id = None

    @property
    def callback_type(self):
        return self._callback_type

    @callback_type.setter
    def callback_type(self, value):
        self._callback_type = value
    @property
    def out_string(self):
        return self._out_string

    @out_string.setter
    def out_string(self, value):
        self._out_string = value
    @property
    def provider_application_id(self):
        return self._provider_application_id

    @provider_application_id.setter
    def provider_application_id(self, value):
        self._provider_application_id = value
    @property
    def provider_id(self):
        return self._provider_id

    @provider_id.setter
    def provider_id(self, value):
        self._provider_id = value
    @property
    def regist_alipay_schema(self):
        return self._regist_alipay_schema

    @regist_alipay_schema.setter
    def regist_alipay_schema(self, value):
        self._regist_alipay_schema = value
    @property
    def regist_mode(self):
        return self._regist_mode

    @regist_mode.setter
    def regist_mode(self, value):
        self._regist_mode = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.callback_type:
            if hasattr(self.callback_type, 'to_alipay_dict'):
                params['callback_type'] = self.callback_type.to_alipay_dict()
            else:
                params['callback_type'] = self.callback_type
        if self.out_string:
            if hasattr(self.out_string, 'to_alipay_dict'):
                params['out_string'] = self.out_string.to_alipay_dict()
            else:
                params['out_string'] = self.out_string
        if self.provider_application_id:
            if hasattr(self.provider_application_id, 'to_alipay_dict'):
                params['provider_application_id'] = self.provider_application_id.to_alipay_dict()
            else:
                params['provider_application_id'] = self.provider_application_id
        if self.provider_id:
            if hasattr(self.provider_id, 'to_alipay_dict'):
                params['provider_id'] = self.provider_id.to_alipay_dict()
            else:
                params['provider_id'] = self.provider_id
        if self.regist_alipay_schema:
            if hasattr(self.regist_alipay_schema, 'to_alipay_dict'):
                params['regist_alipay_schema'] = self.regist_alipay_schema.to_alipay_dict()
            else:
                params['regist_alipay_schema'] = self.regist_alipay_schema
        if self.regist_mode:
            if hasattr(self.regist_mode, 'to_alipay_dict'):
                params['regist_mode'] = self.regist_mode.to_alipay_dict()
            else:
                params['regist_mode'] = self.regist_mode
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Params()
        if 'callback_type' in d:
            o.callback_type = d['callback_type']
        if 'out_string' in d:
            o.out_string = d['out_string']
        if 'provider_application_id' in d:
            o.provider_application_id = d['provider_application_id']
        if 'provider_id' in d:
            o.provider_id = d['provider_id']
        if 'regist_alipay_schema' in d:
            o.regist_alipay_schema = d['regist_alipay_schema']
        if 'regist_mode' in d:
            o.regist_mode = d['regist_mode']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


