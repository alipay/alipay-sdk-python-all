#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantIndirectPromotaskTakeModel(object):

    def __init__(self):
        self._biz_scene = None
        self._group_mid = None
        self._source_pid = None
        self._take_time = None
        self._target_value = None
        self._task_code = None
        self._task_id = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def group_mid(self):
        return self._group_mid

    @group_mid.setter
    def group_mid(self, value):
        self._group_mid = value
    @property
    def source_pid(self):
        return self._source_pid

    @source_pid.setter
    def source_pid(self, value):
        self._source_pid = value
    @property
    def take_time(self):
        return self._take_time

    @take_time.setter
    def take_time(self, value):
        self._take_time = value
    @property
    def target_value(self):
        return self._target_value

    @target_value.setter
    def target_value(self, value):
        self._target_value = value
    @property
    def task_code(self):
        return self._task_code

    @task_code.setter
    def task_code(self, value):
        self._task_code = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.group_mid:
            if hasattr(self.group_mid, 'to_alipay_dict'):
                params['group_mid'] = self.group_mid.to_alipay_dict()
            else:
                params['group_mid'] = self.group_mid
        if self.source_pid:
            if hasattr(self.source_pid, 'to_alipay_dict'):
                params['source_pid'] = self.source_pid.to_alipay_dict()
            else:
                params['source_pid'] = self.source_pid
        if self.take_time:
            if hasattr(self.take_time, 'to_alipay_dict'):
                params['take_time'] = self.take_time.to_alipay_dict()
            else:
                params['take_time'] = self.take_time
        if self.target_value:
            if hasattr(self.target_value, 'to_alipay_dict'):
                params['target_value'] = self.target_value.to_alipay_dict()
            else:
                params['target_value'] = self.target_value
        if self.task_code:
            if hasattr(self.task_code, 'to_alipay_dict'):
                params['task_code'] = self.task_code.to_alipay_dict()
            else:
                params['task_code'] = self.task_code
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantIndirectPromotaskTakeModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'group_mid' in d:
            o.group_mid = d['group_mid']
        if 'source_pid' in d:
            o.source_pid = d['source_pid']
        if 'take_time' in d:
            o.take_time = d['take_time']
        if 'target_value' in d:
            o.target_value = d['target_value']
        if 'task_code' in d:
            o.task_code = d['task_code']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


