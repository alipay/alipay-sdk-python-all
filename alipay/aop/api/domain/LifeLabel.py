#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Option import Option


class LifeLabel(object):

    def __init__(self):
        self._biz = None
        self._category = None
        self._data_type = None
        self._label_code = None
        self._label_id = None
        self._label_name = None
        self._operator = None
        self._options = None
        self._type = None

    @property
    def biz(self):
        return self._biz

    @biz.setter
    def biz(self, value):
        self._biz = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def label_code(self):
        return self._label_code

    @label_code.setter
    def label_code(self, value):
        self._label_code = value
    @property
    def label_id(self):
        return self._label_id

    @label_id.setter
    def label_id(self, value):
        self._label_id = value
    @property
    def label_name(self):
        return self._label_name

    @label_name.setter
    def label_name(self, value):
        self._label_name = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        if isinstance(value, list):
            self._options = list()
            for i in value:
                if isinstance(i, Option):
                    self._options.append(i)
                else:
                    self._options.append(Option.from_alipay_dict(i))
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz:
            if hasattr(self.biz, 'to_alipay_dict'):
                params['biz'] = self.biz.to_alipay_dict()
            else:
                params['biz'] = self.biz
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.label_code:
            if hasattr(self.label_code, 'to_alipay_dict'):
                params['label_code'] = self.label_code.to_alipay_dict()
            else:
                params['label_code'] = self.label_code
        if self.label_id:
            if hasattr(self.label_id, 'to_alipay_dict'):
                params['label_id'] = self.label_id.to_alipay_dict()
            else:
                params['label_id'] = self.label_id
        if self.label_name:
            if hasattr(self.label_name, 'to_alipay_dict'):
                params['label_name'] = self.label_name.to_alipay_dict()
            else:
                params['label_name'] = self.label_name
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.options:
            if isinstance(self.options, list):
                for i in range(0, len(self.options)):
                    element = self.options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.options[i] = element.to_alipay_dict()
            if hasattr(self.options, 'to_alipay_dict'):
                params['options'] = self.options.to_alipay_dict()
            else:
                params['options'] = self.options
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LifeLabel()
        if 'biz' in d:
            o.biz = d['biz']
        if 'category' in d:
            o.category = d['category']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'label_code' in d:
            o.label_code = d['label_code']
        if 'label_id' in d:
            o.label_id = d['label_id']
        if 'label_name' in d:
            o.label_name = d['label_name']
        if 'operator' in d:
            o.operator = d['operator']
        if 'options' in d:
            o.options = d['options']
        if 'type' in d:
            o.type = d['type']
        return o


