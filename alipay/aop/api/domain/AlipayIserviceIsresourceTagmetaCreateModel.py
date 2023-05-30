#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsresourceTagmetaCreateModel(object):

    def __init__(self):
        self._name = None
        self._tag_code = None
        self._tag_level = None
        self._tenant_instance_id = None
        self._value_comment = None
        self._value_type = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def tag_code(self):
        return self._tag_code

    @tag_code.setter
    def tag_code(self, value):
        self._tag_code = value
    @property
    def tag_level(self):
        return self._tag_level

    @tag_level.setter
    def tag_level(self, value):
        self._tag_level = value
    @property
    def tenant_instance_id(self):
        return self._tenant_instance_id

    @tenant_instance_id.setter
    def tenant_instance_id(self, value):
        self._tenant_instance_id = value
    @property
    def value_comment(self):
        return self._value_comment

    @value_comment.setter
    def value_comment(self, value):
        self._value_comment = value
    @property
    def value_type(self):
        return self._value_type

    @value_type.setter
    def value_type(self, value):
        self._value_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.tag_code:
            if hasattr(self.tag_code, 'to_alipay_dict'):
                params['tag_code'] = self.tag_code.to_alipay_dict()
            else:
                params['tag_code'] = self.tag_code
        if self.tag_level:
            if hasattr(self.tag_level, 'to_alipay_dict'):
                params['tag_level'] = self.tag_level.to_alipay_dict()
            else:
                params['tag_level'] = self.tag_level
        if self.tenant_instance_id:
            if hasattr(self.tenant_instance_id, 'to_alipay_dict'):
                params['tenant_instance_id'] = self.tenant_instance_id.to_alipay_dict()
            else:
                params['tenant_instance_id'] = self.tenant_instance_id
        if self.value_comment:
            if hasattr(self.value_comment, 'to_alipay_dict'):
                params['value_comment'] = self.value_comment.to_alipay_dict()
            else:
                params['value_comment'] = self.value_comment
        if self.value_type:
            if hasattr(self.value_type, 'to_alipay_dict'):
                params['value_type'] = self.value_type.to_alipay_dict()
            else:
                params['value_type'] = self.value_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIsresourceTagmetaCreateModel()
        if 'name' in d:
            o.name = d['name']
        if 'tag_code' in d:
            o.tag_code = d['tag_code']
        if 'tag_level' in d:
            o.tag_level = d['tag_level']
        if 'tenant_instance_id' in d:
            o.tenant_instance_id = d['tenant_instance_id']
        if 'value_comment' in d:
            o.value_comment = d['value_comment']
        if 'value_type' in d:
            o.value_type = d['value_type']
        return o


