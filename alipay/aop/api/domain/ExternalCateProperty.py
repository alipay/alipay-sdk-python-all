#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExternalCatePropertyValue import ExternalCatePropertyValue


class ExternalCateProperty(object):

    def __init__(self):
        self._condition_note = None
        self._config = None
        self._property_alias = None
        self._property_id = None
        self._property_name = None
        self._property_type = None
        self._property_value_list = None
        self._remark = None
        self._required = None
        self._value_type = None

    @property
    def condition_note(self):
        return self._condition_note

    @condition_note.setter
    def condition_note(self, value):
        self._condition_note = value
    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value
    @property
    def property_alias(self):
        return self._property_alias

    @property_alias.setter
    def property_alias(self, value):
        self._property_alias = value
    @property
    def property_id(self):
        return self._property_id

    @property_id.setter
    def property_id(self, value):
        self._property_id = value
    @property
    def property_name(self):
        return self._property_name

    @property_name.setter
    def property_name(self, value):
        self._property_name = value
    @property
    def property_type(self):
        return self._property_type

    @property_type.setter
    def property_type(self, value):
        self._property_type = value
    @property
    def property_value_list(self):
        return self._property_value_list

    @property_value_list.setter
    def property_value_list(self, value):
        if isinstance(value, list):
            self._property_value_list = list()
            for i in value:
                if isinstance(i, ExternalCatePropertyValue):
                    self._property_value_list.append(i)
                else:
                    self._property_value_list.append(ExternalCatePropertyValue.from_alipay_dict(i))
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value
    @property
    def value_type(self):
        return self._value_type

    @value_type.setter
    def value_type(self, value):
        self._value_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.condition_note:
            if hasattr(self.condition_note, 'to_alipay_dict'):
                params['condition_note'] = self.condition_note.to_alipay_dict()
            else:
                params['condition_note'] = self.condition_note
        if self.config:
            if hasattr(self.config, 'to_alipay_dict'):
                params['config'] = self.config.to_alipay_dict()
            else:
                params['config'] = self.config
        if self.property_alias:
            if hasattr(self.property_alias, 'to_alipay_dict'):
                params['property_alias'] = self.property_alias.to_alipay_dict()
            else:
                params['property_alias'] = self.property_alias
        if self.property_id:
            if hasattr(self.property_id, 'to_alipay_dict'):
                params['property_id'] = self.property_id.to_alipay_dict()
            else:
                params['property_id'] = self.property_id
        if self.property_name:
            if hasattr(self.property_name, 'to_alipay_dict'):
                params['property_name'] = self.property_name.to_alipay_dict()
            else:
                params['property_name'] = self.property_name
        if self.property_type:
            if hasattr(self.property_type, 'to_alipay_dict'):
                params['property_type'] = self.property_type.to_alipay_dict()
            else:
                params['property_type'] = self.property_type
        if self.property_value_list:
            if isinstance(self.property_value_list, list):
                for i in range(0, len(self.property_value_list)):
                    element = self.property_value_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.property_value_list[i] = element.to_alipay_dict()
            if hasattr(self.property_value_list, 'to_alipay_dict'):
                params['property_value_list'] = self.property_value_list.to_alipay_dict()
            else:
                params['property_value_list'] = self.property_value_list
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
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
        o = ExternalCateProperty()
        if 'condition_note' in d:
            o.condition_note = d['condition_note']
        if 'config' in d:
            o.config = d['config']
        if 'property_alias' in d:
            o.property_alias = d['property_alias']
        if 'property_id' in d:
            o.property_id = d['property_id']
        if 'property_name' in d:
            o.property_name = d['property_name']
        if 'property_type' in d:
            o.property_type = d['property_type']
        if 'property_value_list' in d:
            o.property_value_list = d['property_value_list']
        if 'remark' in d:
            o.remark = d['remark']
        if 'required' in d:
            o.required = d['required']
        if 'value_type' in d:
            o.value_type = d['value_type']
        return o


