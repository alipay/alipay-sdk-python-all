#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAuthUserauthTokenCreateModel(object):

    def __init__(self):
        self._scopes = None
        self._user_id = None

    @property
    def scopes(self):
        return self._scopes

    @scopes.setter
    def scopes(self, value):
        self._scopes = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.scopes:
            if hasattr(self.scopes, 'to_alipay_dict'):
                params['scopes'] = self.scopes.to_alipay_dict()
            else:
                params['scopes'] = self.scopes
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
        o = AlipayOpenAuthUserauthTokenCreateModel()
        if 'scopes' in d:
            o.scopes = d['scopes']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


