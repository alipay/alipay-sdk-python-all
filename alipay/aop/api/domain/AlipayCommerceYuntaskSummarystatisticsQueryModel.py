#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceYuntaskSummarystatisticsQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._hunter_id = None
        self._hunter_open_id = None
        self._merchant_pid = None
        self._shop_id = None
        self._task_template_id = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def hunter_id(self):
        return self._hunter_id

    @hunter_id.setter
    def hunter_id(self, value):
        self._hunter_id = value
    @property
    def hunter_open_id(self):
        return self._hunter_open_id

    @hunter_open_id.setter
    def hunter_open_id(self, value):
        self._hunter_open_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def task_template_id(self):
        return self._task_template_id

    @task_template_id.setter
    def task_template_id(self, value):
        self._task_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.hunter_id:
            if hasattr(self.hunter_id, 'to_alipay_dict'):
                params['hunter_id'] = self.hunter_id.to_alipay_dict()
            else:
                params['hunter_id'] = self.hunter_id
        if self.hunter_open_id:
            if hasattr(self.hunter_open_id, 'to_alipay_dict'):
                params['hunter_open_id'] = self.hunter_open_id.to_alipay_dict()
            else:
                params['hunter_open_id'] = self.hunter_open_id
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.task_template_id:
            if hasattr(self.task_template_id, 'to_alipay_dict'):
                params['task_template_id'] = self.task_template_id.to_alipay_dict()
            else:
                params['task_template_id'] = self.task_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceYuntaskSummarystatisticsQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'hunter_id' in d:
            o.hunter_id = d['hunter_id']
        if 'hunter_open_id' in d:
            o.hunter_open_id = d['hunter_open_id']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'task_template_id' in d:
            o.task_template_id = d['task_template_id']
        return o


