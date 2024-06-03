#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderTagInfo(object):

    def __init__(self):
        self._of_hold = None

    @property
    def of_hold(self):
        return self._of_hold

    @of_hold.setter
    def of_hold(self, value):
        self._of_hold = value


    def to_alipay_dict(self):
        params = dict()
        if self.of_hold:
            if hasattr(self.of_hold, 'to_alipay_dict'):
                params['of_hold'] = self.of_hold.to_alipay_dict()
            else:
                params['of_hold'] = self.of_hold
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderTagInfo()
        if 'of_hold' in d:
            o.of_hold = d['of_hold']
        return o


