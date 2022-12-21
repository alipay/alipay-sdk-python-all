#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantIndirectPromotaskSyncModel(object):

    def __init__(self):
        self._biz_scene = None
        self._group_mid = None
        self._source_pid = None
        self._task_code = None
        self._task_end_time = None
        self._task_id = None
        self._task_state = None

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
    def task_code(self):
        return self._task_code

    @task_code.setter
    def task_code(self, value):
        self._task_code = value
    @property
    def task_end_time(self):
        return self._task_end_time

    @task_end_time.setter
    def task_end_time(self, value):
        self._task_end_time = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_state(self):
        return self._task_state

    @task_state.setter
    def task_state(self, value):
        self._task_state = value


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
        if self.task_code:
            if hasattr(self.task_code, 'to_alipay_dict'):
                params['task_code'] = self.task_code.to_alipay_dict()
            else:
                params['task_code'] = self.task_code
        if self.task_end_time:
            if hasattr(self.task_end_time, 'to_alipay_dict'):
                params['task_end_time'] = self.task_end_time.to_alipay_dict()
            else:
                params['task_end_time'] = self.task_end_time
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.task_state:
            if hasattr(self.task_state, 'to_alipay_dict'):
                params['task_state'] = self.task_state.to_alipay_dict()
            else:
                params['task_state'] = self.task_state
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantIndirectPromotaskSyncModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'group_mid' in d:
            o.group_mid = d['group_mid']
        if 'source_pid' in d:
            o.source_pid = d['source_pid']
        if 'task_code' in d:
            o.task_code = d['task_code']
        if 'task_end_time' in d:
            o.task_end_time = d['task_end_time']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'task_state' in d:
            o.task_state = d['task_state']
        return o


