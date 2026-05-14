#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneApplyRecord(object):

    def __init__(self):
        self._effective_time = None
        self._scene_name = None
        self._scene_status = None

    @property
    def effective_time(self):
        return self._effective_time

    @effective_time.setter
    def effective_time(self, value):
        self._effective_time = value
    @property
    def scene_name(self):
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        self._scene_name = value
    @property
    def scene_status(self):
        return self._scene_status

    @scene_status.setter
    def scene_status(self, value):
        self._scene_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.effective_time:
            if hasattr(self.effective_time, 'to_alipay_dict'):
                params['effective_time'] = self.effective_time.to_alipay_dict()
            else:
                params['effective_time'] = self.effective_time
        if self.scene_name:
            if hasattr(self.scene_name, 'to_alipay_dict'):
                params['scene_name'] = self.scene_name.to_alipay_dict()
            else:
                params['scene_name'] = self.scene_name
        if self.scene_status:
            if hasattr(self.scene_status, 'to_alipay_dict'):
                params['scene_status'] = self.scene_status.to_alipay_dict()
            else:
                params['scene_status'] = self.scene_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneApplyRecord()
        if 'effective_time' in d:
            o.effective_time = d['effective_time']
        if 'scene_name' in d:
            o.scene_name = d['scene_name']
        if 'scene_status' in d:
            o.scene_status = d['scene_status']
        return o


