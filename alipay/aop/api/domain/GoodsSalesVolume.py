#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodsSalesVolume(object):

    def __init__(self):
        self._period = None
        self._volume = None

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value


    def to_alipay_dict(self):
        params = dict()
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.volume:
            if hasattr(self.volume, 'to_alipay_dict'):
                params['volume'] = self.volume.to_alipay_dict()
            else:
                params['volume'] = self.volume
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodsSalesVolume()
        if 'period' in d:
            o.period = d['period']
        if 'volume' in d:
            o.volume = d['volume']
        return o


