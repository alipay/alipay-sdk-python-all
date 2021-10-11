#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StockPositionVO(object):

    def __init__(self):
        self._is_show = None
        self._position_code = None

    @property
    def is_show(self):
        return self._is_show

    @is_show.setter
    def is_show(self, value):
        self._is_show = value
    @property
    def position_code(self):
        return self._position_code

    @position_code.setter
    def position_code(self, value):
        self._position_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_show:
            if hasattr(self.is_show, 'to_alipay_dict'):
                params['is_show'] = self.is_show.to_alipay_dict()
            else:
                params['is_show'] = self.is_show
        if self.position_code:
            if hasattr(self.position_code, 'to_alipay_dict'):
                params['position_code'] = self.position_code.to_alipay_dict()
            else:
                params['position_code'] = self.position_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StockPositionVO()
        if 'is_show' in d:
            o.is_show = d['is_show']
        if 'position_code' in d:
            o.position_code = d['position_code']
        return o


