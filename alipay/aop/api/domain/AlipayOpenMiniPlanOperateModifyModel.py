#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniPlanOperateModifyModel(object):

    def __init__(self):
        self._scene = None
        self._type_list = None

    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def type_list(self):
        return self._type_list

    @type_list.setter
    def type_list(self, value):
        self._type_list = value


    def to_alipay_dict(self):
        params = dict()
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.type_list:
            if hasattr(self.type_list, 'to_alipay_dict'):
                params['type_list'] = self.type_list.to_alipay_dict()
            else:
                params['type_list'] = self.type_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniPlanOperateModifyModel()
        if 'scene' in d:
            o.scene = d['scene']
        if 'type_list' in d:
            o.type_list = d['type_list']
        return o


