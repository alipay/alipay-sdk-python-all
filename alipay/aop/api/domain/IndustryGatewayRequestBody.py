#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SiData import SiData


class IndustryGatewayRequestBody(object):

    def __init__(self):
        self._biz_type = None
        self._city_code = None
        self._extend_params = None
        self._si_data = None
        self._sys_service_provider_id = None
        self._target_notify_time = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def si_data(self):
        return self._si_data

    @si_data.setter
    def si_data(self, value):
        if isinstance(value, list):
            self._si_data = list()
            for i in value:
                if isinstance(i, SiData):
                    self._si_data.append(i)
                else:
                    self._si_data.append(SiData.from_alipay_dict(i))
    @property
    def sys_service_provider_id(self):
        return self._sys_service_provider_id

    @sys_service_provider_id.setter
    def sys_service_provider_id(self, value):
        self._sys_service_provider_id = value
    @property
    def target_notify_time(self):
        return self._target_notify_time

    @target_notify_time.setter
    def target_notify_time(self, value):
        self._target_notify_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.si_data:
            if isinstance(self.si_data, list):
                for i in range(0, len(self.si_data)):
                    element = self.si_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.si_data[i] = element.to_alipay_dict()
            if hasattr(self.si_data, 'to_alipay_dict'):
                params['si_data'] = self.si_data.to_alipay_dict()
            else:
                params['si_data'] = self.si_data
        if self.sys_service_provider_id:
            if hasattr(self.sys_service_provider_id, 'to_alipay_dict'):
                params['sys_service_provider_id'] = self.sys_service_provider_id.to_alipay_dict()
            else:
                params['sys_service_provider_id'] = self.sys_service_provider_id
        if self.target_notify_time:
            if hasattr(self.target_notify_time, 'to_alipay_dict'):
                params['target_notify_time'] = self.target_notify_time.to_alipay_dict()
            else:
                params['target_notify_time'] = self.target_notify_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryGatewayRequestBody()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'si_data' in d:
            o.si_data = d['si_data']
        if 'sys_service_provider_id' in d:
            o.sys_service_provider_id = d['sys_service_provider_id']
        if 'target_notify_time' in d:
            o.target_notify_time = d['target_notify_time']
        return o


