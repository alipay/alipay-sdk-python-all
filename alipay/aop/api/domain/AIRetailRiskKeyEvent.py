#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AIRetailRiskKeyEvent(object):

    def __init__(self):
        self._actions = None
        self._camera_id = None
        self._start_ts = None

    @property
    def actions(self):
        return self._actions

    @actions.setter
    def actions(self, value):
        if isinstance(value, list):
            self._actions = list()
            for i in value:
                self._actions.append(i)
    @property
    def camera_id(self):
        return self._camera_id

    @camera_id.setter
    def camera_id(self, value):
        self._camera_id = value
    @property
    def start_ts(self):
        return self._start_ts

    @start_ts.setter
    def start_ts(self, value):
        self._start_ts = value


    def to_alipay_dict(self):
        params = dict()
        if self.actions:
            if isinstance(self.actions, list):
                for i in range(0, len(self.actions)):
                    element = self.actions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.actions[i] = element.to_alipay_dict()
            if hasattr(self.actions, 'to_alipay_dict'):
                params['actions'] = self.actions.to_alipay_dict()
            else:
                params['actions'] = self.actions
        if self.camera_id:
            if hasattr(self.camera_id, 'to_alipay_dict'):
                params['camera_id'] = self.camera_id.to_alipay_dict()
            else:
                params['camera_id'] = self.camera_id
        if self.start_ts:
            if hasattr(self.start_ts, 'to_alipay_dict'):
                params['start_ts'] = self.start_ts.to_alipay_dict()
            else:
                params['start_ts'] = self.start_ts
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AIRetailRiskKeyEvent()
        if 'actions' in d:
            o.actions = d['actions']
        if 'camera_id' in d:
            o.camera_id = d['camera_id']
        if 'start_ts' in d:
            o.start_ts = d['start_ts']
        return o


