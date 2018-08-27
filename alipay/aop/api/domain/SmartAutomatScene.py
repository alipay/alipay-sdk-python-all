#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SmartAutomatScene(object):

    def __init__(self):
        self._level_1 = None
        self._level_2 = None

    @property
    def level_1(self):
        return self._level_1

    @level_1.setter
    def level_1(self, value):
        self._level_1 = value
    @property
    def level_2(self):
        return self._level_2

    @level_2.setter
    def level_2(self, value):
        self._level_2 = value


    def to_alipay_dict(self):
        params = dict()
        if self.level_1:
            if hasattr(self.level_1, 'to_alipay_dict'):
                params['level_1'] = self.level_1.to_alipay_dict()
            else:
                params['level_1'] = self.level_1
        if self.level_2:
            if hasattr(self.level_2, 'to_alipay_dict'):
                params['level_2'] = self.level_2.to_alipay_dict()
            else:
                params['level_2'] = self.level_2
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SmartAutomatScene()
        if 'level_1' in d:
            o.level_1 = d['level_1']
        if 'level_2' in d:
            o.level_2 = d['level_2']
        return o


