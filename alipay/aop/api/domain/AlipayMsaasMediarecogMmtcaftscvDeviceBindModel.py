#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogMmtcaftscvDeviceBindModel(object):

    def __init__(self):
        self._device_id = None
        self._isv_pid = None
        self._isv_tid = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def isv_tid(self):
        return self._isv_tid

    @isv_tid.setter
    def isv_tid(self, value):
        self._isv_tid = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.isv_tid:
            if hasattr(self.isv_tid, 'to_alipay_dict'):
                params['isv_tid'] = self.isv_tid.to_alipay_dict()
            else:
                params['isv_tid'] = self.isv_tid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmtcaftscvDeviceBindModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'isv_tid' in d:
            o.isv_tid = d['isv_tid']
        return o


