#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DevicePushPayload(object):

    def __init__(self):
        self._device_id = None
        self._notify_params = None
        self._scene = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def notify_params(self):
        return self._notify_params

    @notify_params.setter
    def notify_params(self, value):
        self._notify_params = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.notify_params:
            if hasattr(self.notify_params, 'to_alipay_dict'):
                params['notify_params'] = self.notify_params.to_alipay_dict()
            else:
                params['notify_params'] = self.notify_params
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DevicePushPayload()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'notify_params' in d:
            o.notify_params = d['notify_params']
        if 'scene' in d:
            o.scene = d['scene']
        return o


