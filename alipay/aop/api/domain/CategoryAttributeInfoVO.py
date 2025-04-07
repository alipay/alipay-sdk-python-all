#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AttributeValueInfo import AttributeValueInfo


class CategoryAttributeInfoVO(object):

    def __init__(self):
        self._attr_code = None
        self._attr_key = None
        self._attr_name = None
        self._attr_type = None
        self._attr_value_list = None
        self._attr_value_type = None
        self._category_id = None
        self._custom_input = None
        self._multi_select = None
        self._required = None
        self._status = None

    @property
    def attr_code(self):
        return self._attr_code

    @attr_code.setter
    def attr_code(self, value):
        self._attr_code = value
    @property
    def attr_key(self):
        return self._attr_key

    @attr_key.setter
    def attr_key(self, value):
        self._attr_key = value
    @property
    def attr_name(self):
        return self._attr_name

    @attr_name.setter
    def attr_name(self, value):
        self._attr_name = value
    @property
    def attr_type(self):
        return self._attr_type

    @attr_type.setter
    def attr_type(self, value):
        self._attr_type = value
    @property
    def attr_value_list(self):
        return self._attr_value_list

    @attr_value_list.setter
    def attr_value_list(self, value):
        if isinstance(value, list):
            self._attr_value_list = list()
            for i in value:
                if isinstance(i, AttributeValueInfo):
                    self._attr_value_list.append(i)
                else:
                    self._attr_value_list.append(AttributeValueInfo.from_alipay_dict(i))
    @property
    def attr_value_type(self):
        return self._attr_value_type

    @attr_value_type.setter
    def attr_value_type(self, value):
        self._attr_value_type = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def custom_input(self):
        return self._custom_input

    @custom_input.setter
    def custom_input(self, value):
        self._custom_input = value
    @property
    def multi_select(self):
        return self._multi_select

    @multi_select.setter
    def multi_select(self, value):
        self._multi_select = value
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.attr_code:
            if hasattr(self.attr_code, 'to_alipay_dict'):
                params['attr_code'] = self.attr_code.to_alipay_dict()
            else:
                params['attr_code'] = self.attr_code
        if self.attr_key:
            if hasattr(self.attr_key, 'to_alipay_dict'):
                params['attr_key'] = self.attr_key.to_alipay_dict()
            else:
                params['attr_key'] = self.attr_key
        if self.attr_name:
            if hasattr(self.attr_name, 'to_alipay_dict'):
                params['attr_name'] = self.attr_name.to_alipay_dict()
            else:
                params['attr_name'] = self.attr_name
        if self.attr_type:
            if hasattr(self.attr_type, 'to_alipay_dict'):
                params['attr_type'] = self.attr_type.to_alipay_dict()
            else:
                params['attr_type'] = self.attr_type
        if self.attr_value_list:
            if isinstance(self.attr_value_list, list):
                for i in range(0, len(self.attr_value_list)):
                    element = self.attr_value_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attr_value_list[i] = element.to_alipay_dict()
            if hasattr(self.attr_value_list, 'to_alipay_dict'):
                params['attr_value_list'] = self.attr_value_list.to_alipay_dict()
            else:
                params['attr_value_list'] = self.attr_value_list
        if self.attr_value_type:
            if hasattr(self.attr_value_type, 'to_alipay_dict'):
                params['attr_value_type'] = self.attr_value_type.to_alipay_dict()
            else:
                params['attr_value_type'] = self.attr_value_type
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.custom_input:
            if hasattr(self.custom_input, 'to_alipay_dict'):
                params['custom_input'] = self.custom_input.to_alipay_dict()
            else:
                params['custom_input'] = self.custom_input
        if self.multi_select:
            if hasattr(self.multi_select, 'to_alipay_dict'):
                params['multi_select'] = self.multi_select.to_alipay_dict()
            else:
                params['multi_select'] = self.multi_select
        if self.required:
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CategoryAttributeInfoVO()
        if 'attr_code' in d:
            o.attr_code = d['attr_code']
        if 'attr_key' in d:
            o.attr_key = d['attr_key']
        if 'attr_name' in d:
            o.attr_name = d['attr_name']
        if 'attr_type' in d:
            o.attr_type = d['attr_type']
        if 'attr_value_list' in d:
            o.attr_value_list = d['attr_value_list']
        if 'attr_value_type' in d:
            o.attr_value_type = d['attr_value_type']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'custom_input' in d:
            o.custom_input = d['custom_input']
        if 'multi_select' in d:
            o.multi_select = d['multi_select']
        if 'required' in d:
            o.required = d['required']
        if 'status' in d:
            o.status = d['status']
        return o


