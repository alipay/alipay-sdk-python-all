#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdConversionJoinWindow(object):

    def __init__(self):
        self._join_window_code = None
        self._join_window_name = None

    @property
    def join_window_code(self):
        return self._join_window_code

    @join_window_code.setter
    def join_window_code(self, value):
        self._join_window_code = value
    @property
    def join_window_name(self):
        return self._join_window_name

    @join_window_name.setter
    def join_window_name(self, value):
        self._join_window_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.join_window_code:
            if hasattr(self.join_window_code, 'to_alipay_dict'):
                params['join_window_code'] = self.join_window_code.to_alipay_dict()
            else:
                params['join_window_code'] = self.join_window_code
        if self.join_window_name:
            if hasattr(self.join_window_name, 'to_alipay_dict'):
                params['join_window_name'] = self.join_window_name.to_alipay_dict()
            else:
                params['join_window_name'] = self.join_window_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdConversionJoinWindow()
        if 'join_window_code' in d:
            o.join_window_code = d['join_window_code']
        if 'join_window_name' in d:
            o.join_window_name = d['join_window_name']
        return o


