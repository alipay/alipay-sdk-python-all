#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TransportAuthStatusData(object):

    def __init__(self):
        self._auth_status = None
        self._user_id = None

    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_status:
            if hasattr(self.auth_status, 'to_alipay_dict'):
                params['auth_status'] = self.auth_status.to_alipay_dict()
            else:
                params['auth_status'] = self.auth_status
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
        o = TransportAuthStatusData()
        if 'auth_status' in d:
            o.auth_status = d['auth_status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


