#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AuthenticationScene import AuthenticationScene


class AlipaySecurityRiskAuthenticationCancelModel(object):

    def __init__(self):
        self._authentication_scene = None
        self._biz_id = None
        self._biz_info = None
        self._token_id = None

    @property
    def authentication_scene(self):
        return self._authentication_scene

    @authentication_scene.setter
    def authentication_scene(self, value):
        if isinstance(value, AuthenticationScene):
            self._authentication_scene = value
        else:
            self._authentication_scene = AuthenticationScene.from_alipay_dict(value)
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        self._biz_info = value
    @property
    def token_id(self):
        return self._token_id

    @token_id.setter
    def token_id(self, value):
        self._token_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.authentication_scene:
            if hasattr(self.authentication_scene, 'to_alipay_dict'):
                params['authentication_scene'] = self.authentication_scene.to_alipay_dict()
            else:
                params['authentication_scene'] = self.authentication_scene
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.token_id:
            if hasattr(self.token_id, 'to_alipay_dict'):
                params['token_id'] = self.token_id.to_alipay_dict()
            else:
                params['token_id'] = self.token_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskAuthenticationCancelModel()
        if 'authentication_scene' in d:
            o.authentication_scene = d['authentication_scene']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'token_id' in d:
            o.token_id = d['token_id']
        return o


