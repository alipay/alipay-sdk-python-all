#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NbInput(object):

    def __init__(self):
        self._label = None
        self._max_length = None
        self._options = None
        self._required = None
        self._type = None
        self._variable = None
        self._weight = None

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value
    @property
    def max_length(self):
        return self._max_length

    @max_length.setter
    def max_length(self, value):
        self._max_length = value
    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        if isinstance(value, list):
            self._options = list()
            for i in value:
                self._options.append(i)
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
    def variable(self):
        return self._variable

    @variable.setter
    def variable(self, value):
        self._variable = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.label:
            if hasattr(self.label, 'to_alipay_dict'):
                params['label'] = self.label.to_alipay_dict()
            else:
                params['label'] = self.label
        if self.max_length:
            if hasattr(self.max_length, 'to_alipay_dict'):
                params['max_length'] = self.max_length.to_alipay_dict()
            else:
                params['max_length'] = self.max_length
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
        if self.variable:
            if hasattr(self.variable, 'to_alipay_dict'):
                params['variable'] = self.variable.to_alipay_dict()
            else:
                params['variable'] = self.variable
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NbInput()
        if 'label' in d:
            o.label = d['label']
        if 'max_length' in d:
            o.max_length = d['max_length']
        if 'options' in d:
            o.options = d['options']
        if 'required' in d:
            o.required = d['required']
        if 'type' in d:
            o.type = d['type']
        if 'variable' in d:
            o.variable = d['variable']
        if 'weight' in d:
            o.weight = d['weight']
        return o


