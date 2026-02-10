#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RoboCurrentLevel(object):

    def __init__(self):
        self._left = None
        self._right = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value
    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value


    def to_alipay_dict(self):
        params = dict()
        if self.left:
            if hasattr(self.left, 'to_alipay_dict'):
                params['left'] = self.left.to_alipay_dict()
            else:
                params['left'] = self.left
        if self.right:
            if hasattr(self.right, 'to_alipay_dict'):
                params['right'] = self.right.to_alipay_dict()
            else:
                params['right'] = self.right
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoboCurrentLevel()
        if 'left' in d:
            o.left = d['left']
        if 'right' in d:
            o.right = d['right']
        return o


