#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserLevelInfo(object):

    def __init__(self):
        self._login_id = None
        self._user_id = None
        self._user_level = None

    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_level(self):
        return self._user_level

    @user_level.setter
    def user_level(self, value):
        self._user_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_level:
            if hasattr(self.user_level, 'to_alipay_dict'):
                params['user_level'] = self.user_level.to_alipay_dict()
            else:
                params['user_level'] = self.user_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserLevelInfo()
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_level' in d:
            o.user_level = d['user_level']
        return o


