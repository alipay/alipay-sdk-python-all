#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderLogisticsExtInfo(object):

    def __init__(self):
        self._gmt_end = None
        self._gmt_start = None

    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderLogisticsExtInfo()
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        return o


