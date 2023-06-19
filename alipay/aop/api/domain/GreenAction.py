#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GreenAction(object):

    def __init__(self):
        self._biz_value = None
        self._second_scene = None

    @property
    def biz_value(self):
        return self._biz_value

    @biz_value.setter
    def biz_value(self, value):
        self._biz_value = value
    @property
    def second_scene(self):
        return self._second_scene

    @second_scene.setter
    def second_scene(self, value):
        self._second_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_value:
            if hasattr(self.biz_value, 'to_alipay_dict'):
                params['biz_value'] = self.biz_value.to_alipay_dict()
            else:
                params['biz_value'] = self.biz_value
        if self.second_scene:
            if hasattr(self.second_scene, 'to_alipay_dict'):
                params['second_scene'] = self.second_scene.to_alipay_dict()
            else:
                params['second_scene'] = self.second_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GreenAction()
        if 'biz_value' in d:
            o.biz_value = d['biz_value']
        if 'second_scene' in d:
            o.second_scene = d['second_scene']
        return o


