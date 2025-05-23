#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OutOrderUserInfo(object):

    def __init__(self):
        self._user_name = None
        self._user_phone = None
        self._user_phone_type = None

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_phone(self):
        return self._user_phone

    @user_phone.setter
    def user_phone(self, value):
        self._user_phone = value
    @property
    def user_phone_type(self):
        return self._user_phone_type

    @user_phone_type.setter
    def user_phone_type(self, value):
        self._user_phone_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_phone:
            if hasattr(self.user_phone, 'to_alipay_dict'):
                params['user_phone'] = self.user_phone.to_alipay_dict()
            else:
                params['user_phone'] = self.user_phone
        if self.user_phone_type:
            if hasattr(self.user_phone_type, 'to_alipay_dict'):
                params['user_phone_type'] = self.user_phone_type.to_alipay_dict()
            else:
                params['user_phone_type'] = self.user_phone_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OutOrderUserInfo()
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_phone' in d:
            o.user_phone = d['user_phone']
        if 'user_phone_type' in d:
            o.user_phone_type = d['user_phone_type']
        return o


