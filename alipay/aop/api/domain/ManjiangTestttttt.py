#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ManjiangTestttttt(object):

    def __init__(self):
        self._oi = None

    @property
    def oi(self):
        return self._oi

    @oi.setter
    def oi(self, value):
        self._oi = value


    def to_alipay_dict(self):
        params = dict()
        if self.oi:
            if hasattr(self.oi, 'to_alipay_dict'):
                params['oi'] = self.oi.to_alipay_dict()
            else:
                params['oi'] = self.oi
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ManjiangTestttttt()
        if 'oi' in d:
            o.oi = d['oi']
        return o


