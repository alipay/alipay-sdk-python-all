#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantIndirectPromotaskQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._group_mid = None
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
        o = AlipayMerchantIndirectPromotaskQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'group_mid' in d:
            o.group_mid = d['group_mid']
        if 'task_code' in d:
            o.task_code = d['task_code']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


