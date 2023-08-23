#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAccountZavatarAvatarQueryModel(object):

    def __init__(self):
        self._avatar_app_version = None
        self._device_level = None
        self._ext_param = None
        self._node_code = None
        self._scene_code = None

    @property
    def avatar_app_version(self):
        return self._avatar_app_version

    @avatar_app_version.setter
    def avatar_app_version(self, value):
        self._avatar_app_version = value
    @property
    def device_level(self):
        return self._device_level

    @device_level.setter
    def device_level(self, value):
        self._device_level = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def node_code(self):
        return self._node_code

    @node_code.setter
    def node_code(self, value):
        self._node_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.avatar_app_version:
            if hasattr(self.avatar_app_version, 'to_alipay_dict'):
                params['avatar_app_version'] = self.avatar_app_version.to_alipay_dict()
            else:
                params['avatar_app_version'] = self.avatar_app_version
        if self.device_level:
            if hasattr(self.device_level, 'to_alipay_dict'):
                params['device_level'] = self.device_level.to_alipay_dict()
            else:
                params['device_level'] = self.device_level
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.node_code:
            if hasattr(self.node_code, 'to_alipay_dict'):
                params['node_code'] = self.node_code.to_alipay_dict()
            else:
                params['node_code'] = self.node_code
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
        o = AlipayUserAccountZavatarAvatarQueryModel()
        if 'avatar_app_version' in d:
            o.avatar_app_version = d['avatar_app_version']
        if 'device_level' in d:
            o.device_level = d['device_level']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'node_code' in d:
            o.node_code = d['node_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


