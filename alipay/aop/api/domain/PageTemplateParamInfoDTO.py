#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PageTemplateParamInfoDTO(object):

    def __init__(self):
        self._allow_user_input = None
        self._code = None
        self._ext_info = None
        self._front_render_type = None
        self._label = None
        self._required = None
        self._type = None
        self._value = None

    @property
    def allow_user_input(self):
        return self._allow_user_input

    @allow_user_input.setter
    def allow_user_input(self, value):
        self._allow_user_input = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def front_render_type(self):
        return self._front_render_type

    @front_render_type.setter
    def front_render_type(self, value):
        self._front_render_type = value
    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.allow_user_input:
            if hasattr(self.allow_user_input, 'to_alipay_dict'):
                params['allow_user_input'] = self.allow_user_input.to_alipay_dict()
            else:
                params['allow_user_input'] = self.allow_user_input
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.front_render_type:
            if hasattr(self.front_render_type, 'to_alipay_dict'):
                params['front_render_type'] = self.front_render_type.to_alipay_dict()
            else:
                params['front_render_type'] = self.front_render_type
        if self.label:
            if hasattr(self.label, 'to_alipay_dict'):
                params['label'] = self.label.to_alipay_dict()
            else:
                params['label'] = self.label
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PageTemplateParamInfoDTO()
        if 'allow_user_input' in d:
            o.allow_user_input = d['allow_user_input']
        if 'code' in d:
            o.code = d['code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'front_render_type' in d:
            o.front_render_type = d['front_render_type']
        if 'label' in d:
            o.label = d['label']
        if 'required' in d:
            o.required = d['required']
        if 'type' in d:
            o.type = d['type']
        if 'value' in d:
            o.value = d['value']
        return o


