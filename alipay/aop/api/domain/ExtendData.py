#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtendData(object):

    def __init__(self):
        self._mi_settle_ext = None

    @property
    def mi_settle_ext(self):
        return self._mi_settle_ext

    @mi_settle_ext.setter
    def mi_settle_ext(self, value):
        self._mi_settle_ext = value


    def to_alipay_dict(self):
        params = dict()
        if self.mi_settle_ext:
            if hasattr(self.mi_settle_ext, 'to_alipay_dict'):
                params['mi_settle_ext'] = self.mi_settle_ext.to_alipay_dict()
            else:
                params['mi_settle_ext'] = self.mi_settle_ext
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExtendData()
        if 'mi_settle_ext' in d:
            o.mi_settle_ext = d['mi_settle_ext']
        return o


