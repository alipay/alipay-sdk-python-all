#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateFormFields(object):

    def __init__(self):
        self._optional = None
        self._required = None

    @property
    def optional(self):
        return self._optional

    @optional.setter
    def optional(self, value):
        if isinstance(value, list):
            self._optional = list()
            for i in value:
                self._optional.append(i)
    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        if isinstance(value, list):
            self._required = list()
            for i in value:
                self._required.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.optional:
            if isinstance(self.optional, list):
                for i in range(0, len(self.optional)):
                    element = self.optional[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.optional[i] = element.to_alipay_dict()
            if hasattr(self.optional, 'to_alipay_dict'):
                params['optional'] = self.optional.to_alipay_dict()
            else:
                params['optional'] = self.optional
        if self.required:
            if isinstance(self.required, list):
                for i in range(0, len(self.required)):
                    element = self.required[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.required[i] = element.to_alipay_dict()
            if hasattr(self.required, 'to_alipay_dict'):
                params['required'] = self.required.to_alipay_dict()
            else:
                params['required'] = self.required
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateFormFields()
        if 'optional' in d:
            o.optional = d['optional']
        if 'required' in d:
            o.required = d['required']
        return o


