#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceProvider(object):

    def __init__(self):
        self._avatar_url = None
        self._out_doctor_id = None
        self._provider_type = None
        self._service_provider_name = None

    @property
    def avatar_url(self):
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, value):
        self._avatar_url = value
    @property
    def out_doctor_id(self):
        return self._out_doctor_id

    @out_doctor_id.setter
    def out_doctor_id(self, value):
        self._out_doctor_id = value
    @property
    def provider_type(self):
        return self._provider_type

    @provider_type.setter
    def provider_type(self, value):
        self._provider_type = value
    @property
    def service_provider_name(self):
        return self._service_provider_name

    @service_provider_name.setter
    def service_provider_name(self, value):
        self._service_provider_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.avatar_url:
            if hasattr(self.avatar_url, 'to_alipay_dict'):
                params['avatar_url'] = self.avatar_url.to_alipay_dict()
            else:
                params['avatar_url'] = self.avatar_url
        if self.out_doctor_id:
            if hasattr(self.out_doctor_id, 'to_alipay_dict'):
                params['out_doctor_id'] = self.out_doctor_id.to_alipay_dict()
            else:
                params['out_doctor_id'] = self.out_doctor_id
        if self.provider_type:
            if hasattr(self.provider_type, 'to_alipay_dict'):
                params['provider_type'] = self.provider_type.to_alipay_dict()
            else:
                params['provider_type'] = self.provider_type
        if self.service_provider_name:
            if hasattr(self.service_provider_name, 'to_alipay_dict'):
                params['service_provider_name'] = self.service_provider_name.to_alipay_dict()
            else:
                params['service_provider_name'] = self.service_provider_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceProvider()
        if 'avatar_url' in d:
            o.avatar_url = d['avatar_url']
        if 'out_doctor_id' in d:
            o.out_doctor_id = d['out_doctor_id']
        if 'provider_type' in d:
            o.provider_type = d['provider_type']
        if 'service_provider_name' in d:
            o.service_provider_name = d['service_provider_name']
        return o


