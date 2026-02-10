#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RoboCarWindowInfo(object):

    def __init__(self):
        self._open_status = None
        self._window_ability = None

    @property
    def open_status(self):
        return self._open_status

    @open_status.setter
    def open_status(self, value):
        self._open_status = value
    @property
    def window_ability(self):
        return self._window_ability

    @window_ability.setter
    def window_ability(self, value):
        self._window_ability = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_status:
            if hasattr(self.open_status, 'to_alipay_dict'):
                params['open_status'] = self.open_status.to_alipay_dict()
            else:
                params['open_status'] = self.open_status
        if self.window_ability:
            if hasattr(self.window_ability, 'to_alipay_dict'):
                params['window_ability'] = self.window_ability.to_alipay_dict()
            else:
                params['window_ability'] = self.window_ability
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoboCarWindowInfo()
        if 'open_status' in d:
            o.open_status = d['open_status']
        if 'window_ability' in d:
            o.window_ability = d['window_ability']
        return o


