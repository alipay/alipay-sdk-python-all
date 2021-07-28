#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantMrchsurpActivitysignupCreateModel(object):

    def __init__(self):
        self._activity_code = None
        self._umid_token = None
        self._user_id = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def umid_token(self):
        return self._umid_token

    @umid_token.setter
    def umid_token(self, value):
        self._umid_token = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.umid_token:
            if hasattr(self.umid_token, 'to_alipay_dict'):
                params['umid_token'] = self.umid_token.to_alipay_dict()
            else:
                params['umid_token'] = self.umid_token
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
        o = AlipayMerchantMrchsurpActivitysignupCreateModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'umid_token' in d:
            o.umid_token = d['umid_token']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


