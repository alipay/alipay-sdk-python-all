#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuthExtendParams(object):

    def __init__(self):
        self._sys_service_provider_id = None

    @property
    def sys_service_provider_id(self):
        return self._sys_service_provider_id

    @sys_service_provider_id.setter
    def sys_service_provider_id(self, value):
        self._sys_service_provider_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.sys_service_provider_id:
            if hasattr(self.sys_service_provider_id, 'to_alipay_dict'):
                params['sys_service_provider_id'] = self.sys_service_provider_id.to_alipay_dict()
            else:
                params['sys_service_provider_id'] = self.sys_service_provider_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthExtendParams()
        if 'sys_service_provider_id' in d:
            o.sys_service_provider_id = d['sys_service_provider_id']
        return o


