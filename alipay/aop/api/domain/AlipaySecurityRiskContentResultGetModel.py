#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskContentResultGetModel(object):

    def __init__(self):
        self._app_scene = None
        self._app_scene_data_id = None
        self._event_id = None

    @property
    def app_scene(self):
        return self._app_scene

    @app_scene.setter
    def app_scene(self, value):
        self._app_scene = value
    @property
    def app_scene_data_id(self):
        return self._app_scene_data_id

    @app_scene_data_id.setter
    def app_scene_data_id(self, value):
        self._app_scene_data_id = value
    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_scene:
            if hasattr(self.app_scene, 'to_alipay_dict'):
                params['app_scene'] = self.app_scene.to_alipay_dict()
            else:
                params['app_scene'] = self.app_scene
        if self.app_scene_data_id:
            if hasattr(self.app_scene_data_id, 'to_alipay_dict'):
                params['app_scene_data_id'] = self.app_scene_data_id.to_alipay_dict()
            else:
                params['app_scene_data_id'] = self.app_scene_data_id
        if self.event_id:
            if hasattr(self.event_id, 'to_alipay_dict'):
                params['event_id'] = self.event_id.to_alipay_dict()
            else:
                params['event_id'] = self.event_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskContentResultGetModel()
        if 'app_scene' in d:
            o.app_scene = d['app_scene']
        if 'app_scene_data_id' in d:
            o.app_scene_data_id = d['app_scene_data_id']
        if 'event_id' in d:
            o.event_id = d['event_id']
        return o


