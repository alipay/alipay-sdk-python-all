#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SettleExtraParams(object):

    def __init__(self):
        self._quit_type = None

    @property
    def quit_type(self):
        return self._quit_type

    @quit_type.setter
    def quit_type(self, value):
        self._quit_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.quit_type:
            if hasattr(self.quit_type, 'to_alipay_dict'):
                params['quit_type'] = self.quit_type.to_alipay_dict()
            else:
                params['quit_type'] = self.quit_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettleExtraParams()
        if 'quit_type' in d:
            o.quit_type = d['quit_type']
        return o


