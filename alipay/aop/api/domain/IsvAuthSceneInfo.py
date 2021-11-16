#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IsvAuthSceneInfo(object):

    def __init__(self):
        self._scene_code = None
        self._scene_permissions = None

    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def scene_permissions(self):
        return self._scene_permissions

    @scene_permissions.setter
    def scene_permissions(self, value):
        self._scene_permissions = value


    def to_alipay_dict(self):
        params = dict()
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.scene_permissions:
            if hasattr(self.scene_permissions, 'to_alipay_dict'):
                params['scene_permissions'] = self.scene_permissions.to_alipay_dict()
            else:
                params['scene_permissions'] = self.scene_permissions
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IsvAuthSceneInfo()
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'scene_permissions' in d:
            o.scene_permissions = d['scene_permissions']
        return o


