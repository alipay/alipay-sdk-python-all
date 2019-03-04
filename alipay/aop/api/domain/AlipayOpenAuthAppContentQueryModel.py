#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAuthAppContentQueryModel(object):

    def __init__(self):
        self._auth_scene = None

    @property
    def auth_scene(self):
        return self._auth_scene

    @auth_scene.setter
    def auth_scene(self, value):
        self._auth_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_scene:
            if hasattr(self.auth_scene, 'to_alipay_dict'):
                params['auth_scene'] = self.auth_scene.to_alipay_dict()
            else:
                params['auth_scene'] = self.auth_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAuthAppContentQueryModel()
        if 'auth_scene' in d:
            o.auth_scene = d['auth_scene']
        return o


