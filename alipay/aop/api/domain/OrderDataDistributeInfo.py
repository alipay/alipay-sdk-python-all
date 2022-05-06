#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderDataDistributeInfo(object):

    def __init__(self):
        self._not_distribute_reason = None
        self._scene_code = None
        self._scene_name = None

    @property
    def not_distribute_reason(self):
        return self._not_distribute_reason

    @not_distribute_reason.setter
    def not_distribute_reason(self, value):
        self._not_distribute_reason = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def scene_name(self):
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        self._scene_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.not_distribute_reason:
            if hasattr(self.not_distribute_reason, 'to_alipay_dict'):
                params['not_distribute_reason'] = self.not_distribute_reason.to_alipay_dict()
            else:
                params['not_distribute_reason'] = self.not_distribute_reason
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.scene_name:
            if hasattr(self.scene_name, 'to_alipay_dict'):
                params['scene_name'] = self.scene_name.to_alipay_dict()
            else:
                params['scene_name'] = self.scene_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderDataDistributeInfo()
        if 'not_distribute_reason' in d:
            o.not_distribute_reason = d['not_distribute_reason']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'scene_name' in d:
            o.scene_name = d['scene_name']
        return o


