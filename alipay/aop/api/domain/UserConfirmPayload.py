#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserConfirmPayload(object):

    def __init__(self):
        self._scene = None
        self._user_token = None

    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def user_token(self):
        return self._user_token

    @user_token.setter
    def user_token(self, value):
        self._user_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
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
        o = UserConfirmPayload()
        if 'scene' in d:
            o.scene = d['scene']
        if 'user_token' in d:
            o.user_token = d['user_token']
        return o


