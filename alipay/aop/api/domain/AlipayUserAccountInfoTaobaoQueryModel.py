#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAccountInfoTaobaoQueryModel(object):

    def __init__(self):
        self._target = None
        self._user_token = None

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value
    @property
    def user_token(self):
        return self._user_token

    @user_token.setter
    def user_token(self, value):
        self._user_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.target:
            if hasattr(self.target, 'to_alipay_dict'):
                params['target'] = self.target.to_alipay_dict()
            else:
                params['target'] = self.target
        if self.user_token:
            if hasattr(self.user_token, 'to_alipay_dict'):
                params['user_token'] = self.user_token.to_alipay_dict()
            else:
                params['user_token'] = self.user_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAccountInfoTaobaoQueryModel()
        if 'target' in d:
            o.target = d['target']
        if 'user_token' in d:
            o.user_token = d['user_token']
        return o


