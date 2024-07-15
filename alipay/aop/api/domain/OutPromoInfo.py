#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OutPromoInfo(object):

    def __init__(self):
        self._out_scene = None

    @property
    def out_scene(self):
        return self._out_scene

    @out_scene.setter
    def out_scene(self, value):
        self._out_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_scene:
            if hasattr(self.out_scene, 'to_alipay_dict'):
                params['out_scene'] = self.out_scene.to_alipay_dict()
            else:
                params['out_scene'] = self.out_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OutPromoInfo()
        if 'out_scene' in d:
            o.out_scene = d['out_scene']
        return o


