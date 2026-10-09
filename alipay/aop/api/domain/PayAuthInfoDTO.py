#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayAuthInfoDTO(object):

    def __init__(self):
        self._auth_pid = None
        self._auth_status = None

    @property
    def auth_pid(self):
        return self._auth_pid

    @auth_pid.setter
    def auth_pid(self, value):
        self._auth_pid = value
    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_pid:
            if hasattr(self.auth_pid, 'to_alipay_dict'):
                params['auth_pid'] = self.auth_pid.to_alipay_dict()
            else:
                params['auth_pid'] = self.auth_pid
        if self.auth_status:
            if hasattr(self.auth_status, 'to_alipay_dict'):
                params['auth_status'] = self.auth_status.to_alipay_dict()
            else:
                params['auth_status'] = self.auth_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayAuthInfoDTO()
        if 'auth_pid' in d:
            o.auth_pid = d['auth_pid']
        if 'auth_status' in d:
            o.auth_status = d['auth_status']
        return o


