#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceConfig(object):

    def __init__(self):
        self._service_content = None
        self._service_id = None
        self._service_name = None
        self._service_type = None

    @property
    def service_content(self):
        return self._service_content

    @service_content.setter
    def service_content(self, value):
        self._service_content = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.service_content:
            if hasattr(self.service_content, 'to_alipay_dict'):
                params['service_content'] = self.service_content.to_alipay_dict()
            else:
                params['service_content'] = self.service_content
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceConfig()
        if 'service_content' in d:
            o.service_content = d['service_content']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_type' in d:
            o.service_type = d['service_type']
        return o


