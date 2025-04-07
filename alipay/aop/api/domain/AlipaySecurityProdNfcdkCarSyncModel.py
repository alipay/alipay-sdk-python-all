#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdNfcdkCarSyncModel(object):

    def __init__(self):
        self._car_info = None
        self._time_stamp = None
        self._tuid = None

    @property
    def car_info(self):
        return self._car_info

    @car_info.setter
    def car_info(self, value):
        self._car_info = value
    @property
    def time_stamp(self):
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, value):
        self._time_stamp = value
    @property
    def tuid(self):
        return self._tuid

    @tuid.setter
    def tuid(self, value):
        self._tuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_info:
            if hasattr(self.car_info, 'to_alipay_dict'):
                params['car_info'] = self.car_info.to_alipay_dict()
            else:
                params['car_info'] = self.car_info
        if self.time_stamp:
            if hasattr(self.time_stamp, 'to_alipay_dict'):
                params['time_stamp'] = self.time_stamp.to_alipay_dict()
            else:
                params['time_stamp'] = self.time_stamp
        if self.tuid:
            if hasattr(self.tuid, 'to_alipay_dict'):
                params['tuid'] = self.tuid.to_alipay_dict()
            else:
                params['tuid'] = self.tuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdNfcdkCarSyncModel()
        if 'car_info' in d:
            o.car_info = d['car_info']
        if 'time_stamp' in d:
            o.time_stamp = d['time_stamp']
        if 'tuid' in d:
            o.tuid = d['tuid']
        return o


