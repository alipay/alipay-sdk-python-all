#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppServiceMiniappnearbypoiQueryModel(object):

    def __init__(self):
        self._poi_code_list = None
        self._service_code = None

    @property
    def poi_code_list(self):
        return self._poi_code_list

    @poi_code_list.setter
    def poi_code_list(self, value):
        if isinstance(value, list):
            self._poi_code_list = list()
            for i in value:
                self._poi_code_list.append(i)
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.poi_code_list:
            if isinstance(self.poi_code_list, list):
                for i in range(0, len(self.poi_code_list)):
                    element = self.poi_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.poi_code_list[i] = element.to_alipay_dict()
            if hasattr(self.poi_code_list, 'to_alipay_dict'):
                params['poi_code_list'] = self.poi_code_list.to_alipay_dict()
            else:
                params['poi_code_list'] = self.poi_code_list
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppServiceMiniappnearbypoiQueryModel()
        if 'poi_code_list' in d:
            o.poi_code_list = d['poi_code_list']
        if 'service_code' in d:
            o.service_code = d['service_code']
        return o


