#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuthFieldSceneDTO(object):

    def __init__(self):
        self._scene_code = None
        self._scene_desc = None

    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def scene_desc(self):
        return self._scene_desc

    @scene_desc.setter
    def scene_desc(self, value):
        self._scene_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.scene_desc:
            if hasattr(self.scene_desc, 'to_alipay_dict'):
                params['scene_desc'] = self.scene_desc.to_alipay_dict()
            else:
                params['scene_desc'] = self.scene_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthFieldSceneDTO()
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'scene_desc' in d:
            o.scene_desc = d['scene_desc']
        return o


