#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TransportServiceRecommendValue import TransportServiceRecommendValue


class TransportServiceRecommendItem(object):

    def __init__(self):
        self._service_name = None
        self._service_type = None
        self._template_id = None
        self._value_list = None

    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def value_list(self):
        return self._value_list

    @value_list.setter
    def value_list(self, value):
        if isinstance(value, list):
            self._value_list = list()
            for i in value:
                if isinstance(i, TransportServiceRecommendValue):
                    self._value_list.append(i)
                else:
                    self._value_list.append(TransportServiceRecommendValue.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.value_list:
            if isinstance(self.value_list, list):
                for i in range(0, len(self.value_list)):
                    element = self.value_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.value_list[i] = element.to_alipay_dict()
            if hasattr(self.value_list, 'to_alipay_dict'):
                params['value_list'] = self.value_list.to_alipay_dict()
            else:
                params['value_list'] = self.value_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransportServiceRecommendItem()
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'value_list' in d:
            o.value_list = d['value_list']
        return o


