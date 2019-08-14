#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RegionState(object):

    def __init__(self):
        self._floor = None
        self._left_max = None
        self._left_min = None
        self._left_push = None

    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, value):
        self._floor = value
    @property
    def left_max(self):
        return self._left_max

    @left_max.setter
    def left_max(self, value):
        self._left_max = value
    @property
    def left_min(self):
        return self._left_min

    @left_min.setter
    def left_min(self, value):
        self._left_min = value
    @property
    def left_push(self):
        return self._left_push

    @left_push.setter
    def left_push(self, value):
        self._left_push = value


    def to_alipay_dict(self):
        params = dict()
        if self.floor:
            if hasattr(self.floor, 'to_alipay_dict'):
                params['floor'] = self.floor.to_alipay_dict()
            else:
                params['floor'] = self.floor
        if self.left_max:
            if hasattr(self.left_max, 'to_alipay_dict'):
                params['left_max'] = self.left_max.to_alipay_dict()
            else:
                params['left_max'] = self.left_max
        if self.left_min:
            if hasattr(self.left_min, 'to_alipay_dict'):
                params['left_min'] = self.left_min.to_alipay_dict()
            else:
                params['left_min'] = self.left_min
        if self.left_push:
            if hasattr(self.left_push, 'to_alipay_dict'):
                params['left_push'] = self.left_push.to_alipay_dict()
            else:
                params['left_push'] = self.left_push
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegionState()
        if 'floor' in d:
            o.floor = d['floor']
        if 'left_max' in d:
            o.left_max = d['left_max']
        if 'left_min' in d:
            o.left_min = d['left_min']
        if 'left_push' in d:
            o.left_push = d['left_push']
        return o


