#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCityfacilitatorIotbspFwjnfcUnbindModel(object):

    def __init__(self):
        self._open_id = None
        self._pid = None
        self._upper_sn = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def upper_sn(self):
        return self._upper_sn

    @upper_sn.setter
    def upper_sn(self, value):
        self._upper_sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.upper_sn:
            if hasattr(self.upper_sn, 'to_alipay_dict'):
                params['upper_sn'] = self.upper_sn.to_alipay_dict()
            else:
                params['upper_sn'] = self.upper_sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCityfacilitatorIotbspFwjnfcUnbindModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'upper_sn' in d:
            o.upper_sn = d['upper_sn']
        return o


