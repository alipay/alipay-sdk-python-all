#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndirectIsvTerminalInfo(object):

    def __init__(self):
        self._terminal_brand = None
        self._terminal_id = None

    @property
    def terminal_brand(self):
        return self._terminal_brand

    @terminal_brand.setter
    def terminal_brand(self, value):
        self._terminal_brand = value
    @property
    def terminal_id(self):
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, value):
        self._terminal_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.terminal_brand:
            if hasattr(self.terminal_brand, 'to_alipay_dict'):
                params['terminal_brand'] = self.terminal_brand.to_alipay_dict()
            else:
                params['terminal_brand'] = self.terminal_brand
        if self.terminal_id:
            if hasattr(self.terminal_id, 'to_alipay_dict'):
                params['terminal_id'] = self.terminal_id.to_alipay_dict()
            else:
                params['terminal_id'] = self.terminal_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndirectIsvTerminalInfo()
        if 'terminal_brand' in d:
            o.terminal_brand = d['terminal_brand']
        if 'terminal_id' in d:
            o.terminal_id = d['terminal_id']
        return o


