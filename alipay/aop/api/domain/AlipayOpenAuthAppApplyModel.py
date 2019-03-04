#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAuthAppApplyModel(object):

    def __init__(self):
        self._auth_app_id = None
        self._auth_scene = None
        self._operator_user_id = None

    @property
    def auth_app_id(self):
        return self._auth_app_id

    @auth_app_id.setter
    def auth_app_id(self, value):
        self._auth_app_id = value
    @property
    def auth_scene(self):
        return self._auth_scene

    @auth_scene.setter
    def auth_scene(self, value):
        self._auth_scene = value
    @property
    def operator_user_id(self):
        return self._operator_user_id

    @operator_user_id.setter
    def operator_user_id(self, value):
        self._operator_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_app_id:
            if hasattr(self.auth_app_id, 'to_alipay_dict'):
                params['auth_app_id'] = self.auth_app_id.to_alipay_dict()
            else:
                params['auth_app_id'] = self.auth_app_id
        if self.auth_scene:
            if hasattr(self.auth_scene, 'to_alipay_dict'):
                params['auth_scene'] = self.auth_scene.to_alipay_dict()
            else:
                params['auth_scene'] = self.auth_scene
        if self.operator_user_id:
            if hasattr(self.operator_user_id, 'to_alipay_dict'):
                params['operator_user_id'] = self.operator_user_id.to_alipay_dict()
            else:
                params['operator_user_id'] = self.operator_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAuthAppApplyModel()
        if 'auth_app_id' in d:
            o.auth_app_id = d['auth_app_id']
        if 'auth_scene' in d:
            o.auth_scene = d['auth_scene']
        if 'operator_user_id' in d:
            o.operator_user_id = d['operator_user_id']
        return o


