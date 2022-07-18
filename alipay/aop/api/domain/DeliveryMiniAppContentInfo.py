#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryMiniAppContentInfo(object):

    def __init__(self):
        self._mini_app_delivery_type = None
        self._mini_app_id = None
        self._service_code_list = None

    @property
    def mini_app_delivery_type(self):
        return self._mini_app_delivery_type

    @mini_app_delivery_type.setter
    def mini_app_delivery_type(self, value):
        self._mini_app_delivery_type = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def service_code_list(self):
        return self._service_code_list

    @service_code_list.setter
    def service_code_list(self, value):
        if isinstance(value, list):
            self._service_code_list = list()
            for i in value:
                self._service_code_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.mini_app_delivery_type:
            if hasattr(self.mini_app_delivery_type, 'to_alipay_dict'):
                params['mini_app_delivery_type'] = self.mini_app_delivery_type.to_alipay_dict()
            else:
                params['mini_app_delivery_type'] = self.mini_app_delivery_type
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.service_code_list:
            if isinstance(self.service_code_list, list):
                for i in range(0, len(self.service_code_list)):
                    element = self.service_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_code_list[i] = element.to_alipay_dict()
            if hasattr(self.service_code_list, 'to_alipay_dict'):
                params['service_code_list'] = self.service_code_list.to_alipay_dict()
            else:
                params['service_code_list'] = self.service_code_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryMiniAppContentInfo()
        if 'mini_app_delivery_type' in d:
            o.mini_app_delivery_type = d['mini_app_delivery_type']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'service_code_list' in d:
            o.service_code_list = d['service_code_list']
        return o


