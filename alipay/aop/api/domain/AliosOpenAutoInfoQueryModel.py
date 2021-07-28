#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AliosOpenAutoInfoQueryModel(object):

    def __init__(self):
        self._device_token = None
        self._user_id = None

    @property
    def device_token(self):
        return self._device_token

    @device_token.setter
    def device_token(self, value):
        self._device_token = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_token:
            if hasattr(self.device_token, 'to_alipay_dict'):
                params['device_token'] = self.device_token.to_alipay_dict()
            else:
                params['device_token'] = self.device_token
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
        o = AliosOpenAutoInfoQueryModel()
        if 'device_token' in d:
            o.device_token = d['device_token']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


