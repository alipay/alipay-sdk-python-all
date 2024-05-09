#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayInstUser(object):

    def __init__(self):
        self._mobile_sha_256 = None
        self._user_id = None

    @property
    def mobile_sha_256(self):
        return self._mobile_sha_256

    @mobile_sha_256.setter
    def mobile_sha_256(self, value):
        self._mobile_sha_256 = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.mobile_sha_256:
            if hasattr(self.mobile_sha_256, 'to_alipay_dict'):
                params['mobile_sha_256'] = self.mobile_sha_256.to_alipay_dict()
            else:
                params['mobile_sha_256'] = self.mobile_sha_256
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
        o = PayInstUser()
        if 'mobile_sha_256' in d:
            o.mobile_sha_256 = d['mobile_sha_256']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


