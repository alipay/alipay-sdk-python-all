#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ValidationRule import ValidationRule


class InputFieldModel(object):

    def __init__(self):
        self._default_value = None
        self._field_name = None
        self._field_tips = None
        self._field_title = None
        self._field_type = None
        self._priority = None
        self._regexp_rule_list = None

    @property
    def default_value(self):
        return self._default_value

    @default_value.setter
    def default_value(self, value):
        self._default_value = value
    @property
    def field_name(self):
        return self._field_name

    @field_name.setter
    def field_name(self, value):
        self._field_name = value
    @property
    def field_tips(self):
        return self._field_tips

    @field_tips.setter
    def field_tips(self, value):
        self._field_tips = value
    @property
    def field_title(self):
        return self._field_title

    @field_title.setter
    def field_title(self, value):
        self._field_title = value
    @property
    def field_type(self):
        return self._field_type

    @field_type.setter
    def field_type(self, value):
        self._field_type = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def regexp_rule_list(self):
        return self._regexp_rule_list

    @regexp_rule_list.setter
    def regexp_rule_list(self, value):
        if isinstance(value, list):
            self._regexp_rule_list = list()
            for i in value:
                if isinstance(i, ValidationRule):
                    self._regexp_rule_list.append(i)
                else:
                    self._regexp_rule_list.append(ValidationRule.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.default_value:
            if hasattr(self.default_value, 'to_alipay_dict'):
                params['default_value'] = self.default_value.to_alipay_dict()
            else:
                params['default_value'] = self.default_value
        if self.field_name:
            if hasattr(self.field_name, 'to_alipay_dict'):
                params['field_name'] = self.field_name.to_alipay_dict()
            else:
                params['field_name'] = self.field_name
        if self.field_tips:
            if hasattr(self.field_tips, 'to_alipay_dict'):
                params['field_tips'] = self.field_tips.to_alipay_dict()
            else:
                params['field_tips'] = self.field_tips
        if self.field_title:
            if hasattr(self.field_title, 'to_alipay_dict'):
                params['field_title'] = self.field_title.to_alipay_dict()
            else:
                params['field_title'] = self.field_title
        if self.field_type:
            if hasattr(self.field_type, 'to_alipay_dict'):
                params['field_type'] = self.field_type.to_alipay_dict()
            else:
                params['field_type'] = self.field_type
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.regexp_rule_list:
            if isinstance(self.regexp_rule_list, list):
                for i in range(0, len(self.regexp_rule_list)):
                    element = self.regexp_rule_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.regexp_rule_list[i] = element.to_alipay_dict()
            if hasattr(self.regexp_rule_list, 'to_alipay_dict'):
                params['regexp_rule_list'] = self.regexp_rule_list.to_alipay_dict()
            else:
                params['regexp_rule_list'] = self.regexp_rule_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InputFieldModel()
        if 'default_value' in d:
            o.default_value = d['default_value']
        if 'field_name' in d:
            o.field_name = d['field_name']
        if 'field_tips' in d:
            o.field_tips = d['field_tips']
        if 'field_title' in d:
            o.field_title = d['field_title']
        if 'field_type' in d:
            o.field_type = d['field_type']
        if 'priority' in d:
            o.priority = d['priority']
        if 'regexp_rule_list' in d:
            o.regexp_rule_list = d['regexp_rule_list']
        return o


