#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndustryInvoiceAdditionalElementInfo(object):

    def __init__(self):
        self._element_name = None
        self._element_type = None
        self._element_value = None

    @property
    def element_name(self):
        return self._element_name

    @element_name.setter
    def element_name(self, value):
        self._element_name = value
    @property
    def element_type(self):
        return self._element_type

    @element_type.setter
    def element_type(self, value):
        self._element_type = value
    @property
    def element_value(self):
        return self._element_value

    @element_value.setter
    def element_value(self, value):
        self._element_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.element_name:
            if hasattr(self.element_name, 'to_alipay_dict'):
                params['element_name'] = self.element_name.to_alipay_dict()
            else:
                params['element_name'] = self.element_name
        if self.element_type:
            if hasattr(self.element_type, 'to_alipay_dict'):
                params['element_type'] = self.element_type.to_alipay_dict()
            else:
                params['element_type'] = self.element_type
        if self.element_value:
            if hasattr(self.element_value, 'to_alipay_dict'):
                params['element_value'] = self.element_value.to_alipay_dict()
            else:
                params['element_value'] = self.element_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryInvoiceAdditionalElementInfo()
        if 'element_name' in d:
            o.element_name = d['element_name']
        if 'element_type' in d:
            o.element_type = d['element_type']
        if 'element_value' in d:
            o.element_value = d['element_value']
        return o


