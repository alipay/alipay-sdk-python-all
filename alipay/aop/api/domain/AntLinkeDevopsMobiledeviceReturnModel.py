#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntLinkeDevopsMobiledeviceReturnModel(object):

    def __init__(self):
        self._device_id = None
        self._remote_host = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def remote_host(self):
        return self._remote_host

    @remote_host.setter
    def remote_host(self, value):
        self._remote_host = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.remote_host:
            if hasattr(self.remote_host, 'to_alipay_dict'):
                params['remote_host'] = self.remote_host.to_alipay_dict()
            else:
                params['remote_host'] = self.remote_host
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntLinkeDevopsMobiledeviceReturnModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'remote_host' in d:
            o.remote_host = d['remote_host']
        return o


