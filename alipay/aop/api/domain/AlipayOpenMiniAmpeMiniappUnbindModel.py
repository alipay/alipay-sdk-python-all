#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniAmpeMiniappUnbindModel(object):

    def __init__(self):
        self._mini_app_id = None
        self._mobile_app_id = None
        self._scene_code = None

    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mobile_app_id(self):
        return self._mobile_app_id

    @mobile_app_id.setter
    def mobile_app_id(self, value):
        self._mobile_app_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mobile_app_id:
            if hasattr(self.mobile_app_id, 'to_alipay_dict'):
                params['mobile_app_id'] = self.mobile_app_id.to_alipay_dict()
            else:
                params['mobile_app_id'] = self.mobile_app_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniAmpeMiniappUnbindModel()
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mobile_app_id' in d:
            o.mobile_app_id = d['mobile_app_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


