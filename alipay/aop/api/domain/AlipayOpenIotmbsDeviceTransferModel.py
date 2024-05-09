#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsDeviceTransferModel(object):

    def __init__(self):
        self._new_owner_pid = None
        self._sn = None

    @property
    def new_owner_pid(self):
        return self._new_owner_pid

    @new_owner_pid.setter
    def new_owner_pid(self, value):
        self._new_owner_pid = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.new_owner_pid:
            if hasattr(self.new_owner_pid, 'to_alipay_dict'):
                params['new_owner_pid'] = self.new_owner_pid.to_alipay_dict()
            else:
                params['new_owner_pid'] = self.new_owner_pid
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsDeviceTransferModel()
        if 'new_owner_pid' in d:
            o.new_owner_pid = d['new_owner_pid']
        if 'sn' in d:
            o.sn = d['sn']
        return o


