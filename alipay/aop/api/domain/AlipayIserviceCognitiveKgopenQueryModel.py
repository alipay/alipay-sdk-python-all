#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MapParameter import MapParameter


class AlipayIserviceCognitiveKgopenQueryModel(object):

    def __init__(self):
        self._online_service_code = None
        self._params = None

    @property
    def online_service_code(self):
        return self._online_service_code

    @online_service_code.setter
    def online_service_code(self, value):
        self._online_service_code = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        if isinstance(value, list):
            self._params = list()
            for i in value:
                if isinstance(i, MapParameter):
                    self._params.append(i)
                else:
                    self._params.append(MapParameter.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.online_service_code:
            if hasattr(self.online_service_code, 'to_alipay_dict'):
                params['online_service_code'] = self.online_service_code.to_alipay_dict()
            else:
                params['online_service_code'] = self.online_service_code
        if self.params:
            if isinstance(self.params, list):
                for i in range(0, len(self.params)):
                    element = self.params[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.params[i] = element.to_alipay_dict()
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCognitiveKgopenQueryModel()
        if 'online_service_code' in d:
            o.online_service_code = d['online_service_code']
        if 'params' in d:
            o.params = d['params']
        return o


