#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReliableEnterpriseBaseInfoDTO(object):

    def __init__(self):
        self._auth_status = None
        self._enterprise_code = None
        self._enterprise_name = None

    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value
    @property
    def enterprise_code(self):
        return self._enterprise_code

    @enterprise_code.setter
    def enterprise_code(self, value):
        self._enterprise_code = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_status:
            if hasattr(self.auth_status, 'to_alipay_dict'):
                params['auth_status'] = self.auth_status.to_alipay_dict()
            else:
                params['auth_status'] = self.auth_status
        if self.enterprise_code:
            if hasattr(self.enterprise_code, 'to_alipay_dict'):
                params['enterprise_code'] = self.enterprise_code.to_alipay_dict()
            else:
                params['enterprise_code'] = self.enterprise_code
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReliableEnterpriseBaseInfoDTO()
        if 'auth_status' in d:
            o.auth_status = d['auth_status']
        if 'enterprise_code' in d:
            o.enterprise_code = d['enterprise_code']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        return o


