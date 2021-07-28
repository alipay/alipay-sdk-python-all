#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenContentIotCouponQueryModel(object):

    def __init__(self):
        self._activity_id = None
        self._auth_pid = None
        self._ftoken = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def auth_pid(self):
        return self._auth_pid

    @auth_pid.setter
    def auth_pid(self, value):
        self._auth_pid = value
    @property
    def ftoken(self):
        return self._ftoken

    @ftoken.setter
    def ftoken(self, value):
        self._ftoken = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.auth_pid:
            if hasattr(self.auth_pid, 'to_alipay_dict'):
                params['auth_pid'] = self.auth_pid.to_alipay_dict()
            else:
                params['auth_pid'] = self.auth_pid
        if self.ftoken:
            if hasattr(self.ftoken, 'to_alipay_dict'):
                params['ftoken'] = self.ftoken.to_alipay_dict()
            else:
                params['ftoken'] = self.ftoken
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenContentIotCouponQueryModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'auth_pid' in d:
            o.auth_pid = d['auth_pid']
        if 'ftoken' in d:
            o.ftoken = d['ftoken']
        return o


