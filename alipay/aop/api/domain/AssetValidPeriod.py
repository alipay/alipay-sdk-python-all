#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetValidPeriod(object):

    def __init__(self):
        self._end_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetValidPeriod()
        if 'end_time' in d:
            o.end_time = d['end_time']
        return o


