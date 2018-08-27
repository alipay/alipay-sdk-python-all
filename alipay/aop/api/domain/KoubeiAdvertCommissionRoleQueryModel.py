#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiAdvertCommissionRoleQueryModel(object):

    def __init__(self):
        self._role_code = None
        self._user_identify = None
        self._user_identify_type = None

    @property
    def role_code(self):
        return self._role_code

    @role_code.setter
    def role_code(self, value):
        self._role_code = value
    @property
    def user_identify(self):
        return self._user_identify

    @user_identify.setter
    def user_identify(self, value):
        self._user_identify = value
    @property
    def user_identify_type(self):
        return self._user_identify_type

    @user_identify_type.setter
    def user_identify_type(self, value):
        self._user_identify_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.role_code:
            if hasattr(self.role_code, 'to_alipay_dict'):
                params['role_code'] = self.role_code.to_alipay_dict()
            else:
                params['role_code'] = self.role_code
        if self.user_identify:
            if hasattr(self.user_identify, 'to_alipay_dict'):
                params['user_identify'] = self.user_identify.to_alipay_dict()
            else:
                params['user_identify'] = self.user_identify
        if self.user_identify_type:
            if hasattr(self.user_identify_type, 'to_alipay_dict'):
                params['user_identify_type'] = self.user_identify_type.to_alipay_dict()
            else:
                params['user_identify_type'] = self.user_identify_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiAdvertCommissionRoleQueryModel()
        if 'role_code' in d:
            o.role_code = d['role_code']
        if 'user_identify' in d:
            o.user_identify = d['user_identify']
        if 'user_identify_type' in d:
            o.user_identify_type = d['user_identify_type']
        return o


