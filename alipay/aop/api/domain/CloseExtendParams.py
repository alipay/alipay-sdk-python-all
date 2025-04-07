#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CloseExtendParams(object):

    def __init__(self):
        self._is_fulfilled = None

    @property
    def is_fulfilled(self):
        return self._is_fulfilled

    @is_fulfilled.setter
    def is_fulfilled(self, value):
        self._is_fulfilled = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_fulfilled:
            if hasattr(self.is_fulfilled, 'to_alipay_dict'):
                params['is_fulfilled'] = self.is_fulfilled.to_alipay_dict()
            else:
                params['is_fulfilled'] = self.is_fulfilled
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloseExtendParams()
        if 'is_fulfilled' in d:
            o.is_fulfilled = d['is_fulfilled']
        return o


