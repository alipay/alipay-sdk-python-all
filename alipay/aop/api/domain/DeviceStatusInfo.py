#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceStatusInfo(object):

    def __init__(self):
        self._battery_percent = None
        self._sn = None
        self._status = None

    @property
    def battery_percent(self):
        return self._battery_percent

    @battery_percent.setter
    def battery_percent(self, value):
        self._battery_percent = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.battery_percent:
            if hasattr(self.battery_percent, 'to_alipay_dict'):
                params['battery_percent'] = self.battery_percent.to_alipay_dict()
            else:
                params['battery_percent'] = self.battery_percent
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceStatusInfo()
        if 'battery_percent' in d:
            o.battery_percent = d['battery_percent']
        if 'sn' in d:
            o.sn = d['sn']
        if 'status' in d:
            o.status = d['status']
        return o


