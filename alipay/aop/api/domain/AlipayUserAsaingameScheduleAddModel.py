#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAsaingameScheduleAddModel(object):

    def __init__(self):
        self._daily_schedule_id = None
        self._scene = None
        self._step_data = None

    @property
    def daily_schedule_id(self):
        return self._daily_schedule_id

    @daily_schedule_id.setter
    def daily_schedule_id(self, value):
        self._daily_schedule_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def step_data(self):
        return self._step_data

    @step_data.setter
    def step_data(self, value):
        self._step_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.daily_schedule_id:
            if hasattr(self.daily_schedule_id, 'to_alipay_dict'):
                params['daily_schedule_id'] = self.daily_schedule_id.to_alipay_dict()
            else:
                params['daily_schedule_id'] = self.daily_schedule_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.step_data:
            if hasattr(self.step_data, 'to_alipay_dict'):
                params['step_data'] = self.step_data.to_alipay_dict()
            else:
                params['step_data'] = self.step_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAsaingameScheduleAddModel()
        if 'daily_schedule_id' in d:
            o.daily_schedule_id = d['daily_schedule_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'step_data' in d:
            o.step_data = d['step_data']
        return o


