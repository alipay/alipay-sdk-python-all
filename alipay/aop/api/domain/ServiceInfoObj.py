#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceInfoObj(object):

    def __init__(self):
        self._service_category = None
        self._service_content = None
        self._service_type = None

    @property
    def service_category(self):
        return self._service_category

    @service_category.setter
    def service_category(self, value):
        self._service_category = value
    @property
    def service_content(self):
        return self._service_content

    @service_content.setter
    def service_content(self, value):
        self._service_content = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_category:
            if hasattr(self.service_category, 'to_alipay_dict'):
                params['service_category'] = self.service_category.to_alipay_dict()
            else:
                params['service_category'] = self.service_category
        if self.service_content:
            if hasattr(self.service_content, 'to_alipay_dict'):
                params['service_content'] = self.service_content.to_alipay_dict()
            else:
                params['service_content'] = self.service_content
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceInfoObj()
        if 'service_category' in d:
            o.service_category = d['service_category']
        if 'service_content' in d:
            o.service_content = d['service_content']
        if 'service_type' in d:
            o.service_type = d['service_type']
        return o


