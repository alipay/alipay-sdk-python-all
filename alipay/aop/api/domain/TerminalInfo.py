#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TerminalInfo(object):

    def __init__(self):
        self._pickup_time_desc = None
        self._terminal_code = None
        self._terminal_name = None

    @property
    def pickup_time_desc(self):
        return self._pickup_time_desc

    @pickup_time_desc.setter
    def pickup_time_desc(self, value):
        self._pickup_time_desc = value
    @property
    def terminal_code(self):
        return self._terminal_code

    @terminal_code.setter
    def terminal_code(self, value):
        self._terminal_code = value
    @property
    def terminal_name(self):
        return self._terminal_name

    @terminal_name.setter
    def terminal_name(self, value):
        self._terminal_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.pickup_time_desc:
            if hasattr(self.pickup_time_desc, 'to_alipay_dict'):
                params['pickup_time_desc'] = self.pickup_time_desc.to_alipay_dict()
            else:
                params['pickup_time_desc'] = self.pickup_time_desc
        if self.terminal_code:
            if hasattr(self.terminal_code, 'to_alipay_dict'):
                params['terminal_code'] = self.terminal_code.to_alipay_dict()
            else:
                params['terminal_code'] = self.terminal_code
        if self.terminal_name:
            if hasattr(self.terminal_name, 'to_alipay_dict'):
                params['terminal_name'] = self.terminal_name.to_alipay_dict()
            else:
                params['terminal_name'] = self.terminal_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TerminalInfo()
        if 'pickup_time_desc' in d:
            o.pickup_time_desc = d['pickup_time_desc']
        if 'terminal_code' in d:
            o.terminal_code = d['terminal_code']
        if 'terminal_name' in d:
            o.terminal_name = d['terminal_name']
        return o


