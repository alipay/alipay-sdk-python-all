#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbasePassinfoLogininfoQueryModel(object):

    def __init__(self):
        self._ob_auth_token = None
        self._renew = None
        self._role_type = None

    @property
    def ob_auth_token(self):
        return self._ob_auth_token

    @ob_auth_token.setter
    def ob_auth_token(self, value):
        self._ob_auth_token = value
    @property
    def renew(self):
        return self._renew

    @renew.setter
    def renew(self, value):
        self._renew = value
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ob_auth_token:
            if hasattr(self.ob_auth_token, 'to_alipay_dict'):
                params['ob_auth_token'] = self.ob_auth_token.to_alipay_dict()
            else:
                params['ob_auth_token'] = self.ob_auth_token
        if self.renew:
            if hasattr(self.renew, 'to_alipay_dict'):
                params['renew'] = self.renew.to_alipay_dict()
            else:
                params['renew'] = self.renew
        if self.role_type:
            if hasattr(self.role_type, 'to_alipay_dict'):
                params['role_type'] = self.role_type.to_alipay_dict()
            else:
                params['role_type'] = self.role_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbasePassinfoLogininfoQueryModel()
        if 'ob_auth_token' in d:
            o.ob_auth_token = d['ob_auth_token']
        if 'renew' in d:
            o.renew = d['renew']
        if 'role_type' in d:
            o.role_type = d['role_type']
        return o


