#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppMembersDeleteModel(object):

    def __init__(self):
        self._role = None
        self._user_id = None

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppMembersDeleteModel()
        if 'role' in d:
            o.role = d['role']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


