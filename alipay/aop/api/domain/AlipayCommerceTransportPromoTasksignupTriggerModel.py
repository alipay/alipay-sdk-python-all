#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportPromoTasksignupTriggerModel(object):

    def __init__(self):
        self._open_id = None
        self._task_scene = None
        self._task_source = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def task_scene(self):
        return self._task_scene

    @task_scene.setter
    def task_scene(self, value):
        self._task_scene = value
    @property
    def task_source(self):
        return self._task_source

    @task_source.setter
    def task_source(self, value):
        self._task_source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.task_scene:
            if hasattr(self.task_scene, 'to_alipay_dict'):
                params['task_scene'] = self.task_scene.to_alipay_dict()
            else:
                params['task_scene'] = self.task_scene
        if self.task_source:
            if hasattr(self.task_source, 'to_alipay_dict'):
                params['task_source'] = self.task_source.to_alipay_dict()
            else:
                params['task_source'] = self.task_source
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportPromoTasksignupTriggerModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'task_scene' in d:
            o.task_scene = d['task_scene']
        if 'task_source' in d:
            o.task_source = d['task_source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


