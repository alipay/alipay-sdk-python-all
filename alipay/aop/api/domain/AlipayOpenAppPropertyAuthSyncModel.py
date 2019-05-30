#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PropertyAuthInfo import PropertyAuthInfo


class AlipayOpenAppPropertyAuthSyncModel(object):

    def __init__(self):
        self._auth_info = None
        self._operator = None

    @property
    def auth_info(self):
        return self._auth_info

    @auth_info.setter
    def auth_info(self, value):
        if isinstance(value, list):
            self._auth_info = list()
            for i in value:
                if isinstance(i, PropertyAuthInfo):
                    self._auth_info.append(i)
                else:
                    self._auth_info.append(PropertyAuthInfo.from_alipay_dict(i))
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_info:
            if isinstance(self.auth_info, list):
                for i in range(0, len(self.auth_info)):
                    element = self.auth_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.auth_info[i] = element.to_alipay_dict()
            if hasattr(self.auth_info, 'to_alipay_dict'):
                params['auth_info'] = self.auth_info.to_alipay_dict()
            else:
                params['auth_info'] = self.auth_info
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppPropertyAuthSyncModel()
        if 'auth_info' in d:
            o.auth_info = d['auth_info']
        if 'operator' in d:
            o.operator = d['operator']
        return o


