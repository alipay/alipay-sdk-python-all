#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScenePayToken(object):

    def __init__(self):
        self._scene_pay_token = None
        self._scene_pay_token_type = None

    @property
    def scene_pay_token(self):
        return self._scene_pay_token

    @scene_pay_token.setter
    def scene_pay_token(self, value):
        self._scene_pay_token = value
    @property
    def scene_pay_token_type(self):
        return self._scene_pay_token_type

    @scene_pay_token_type.setter
    def scene_pay_token_type(self, value):
        self._scene_pay_token_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.scene_pay_token:
            if hasattr(self.scene_pay_token, 'to_alipay_dict'):
                params['scene_pay_token'] = self.scene_pay_token.to_alipay_dict()
            else:
                params['scene_pay_token'] = self.scene_pay_token
        if self.scene_pay_token_type:
            if hasattr(self.scene_pay_token_type, 'to_alipay_dict'):
                params['scene_pay_token_type'] = self.scene_pay_token_type.to_alipay_dict()
            else:
                params['scene_pay_token_type'] = self.scene_pay_token_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScenePayToken()
        if 'scene_pay_token' in d:
            o.scene_pay_token = d['scene_pay_token']
        if 'scene_pay_token_type' in d:
            o.scene_pay_token_type = d['scene_pay_token_type']
        return o


