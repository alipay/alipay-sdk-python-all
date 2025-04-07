#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsTokenWaybillQueryModel(object):

    def __init__(self):
        self._info_token = None
        self._token_scene = None

    @property
    def info_token(self):
        return self._info_token

    @info_token.setter
    def info_token(self, value):
        self._info_token = value
    @property
    def token_scene(self):
        return self._token_scene

    @token_scene.setter
    def token_scene(self, value):
        self._token_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.info_token:
            if hasattr(self.info_token, 'to_alipay_dict'):
                params['info_token'] = self.info_token.to_alipay_dict()
            else:
                params['info_token'] = self.info_token
        if self.token_scene:
            if hasattr(self.token_scene, 'to_alipay_dict'):
                params['token_scene'] = self.token_scene.to_alipay_dict()
            else:
                params['token_scene'] = self.token_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsTokenWaybillQueryModel()
        if 'info_token' in d:
            o.info_token = d['info_token']
        if 'token_scene' in d:
            o.token_scene = d['token_scene']
        return o


