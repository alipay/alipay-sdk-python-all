#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoyagerEnvInfo(object):

    def __init__(self):
        self._client_ip = None
        self._os_type = None
        self._terminal_type = None

    @property
    def client_ip(self):
        return self._client_ip

    @client_ip.setter
    def client_ip(self, value):
        self._client_ip = value
    @property
    def os_type(self):
        return self._os_type

    @os_type.setter
    def os_type(self, value):
        self._os_type = value
    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_ip:
            if hasattr(self.client_ip, 'to_alipay_dict'):
                params['client_ip'] = self.client_ip.to_alipay_dict()
            else:
                params['client_ip'] = self.client_ip
        if self.os_type:
            if hasattr(self.os_type, 'to_alipay_dict'):
                params['os_type'] = self.os_type.to_alipay_dict()
            else:
                params['os_type'] = self.os_type
        if self.terminal_type:
            if hasattr(self.terminal_type, 'to_alipay_dict'):
                params['terminal_type'] = self.terminal_type.to_alipay_dict()
            else:
                params['terminal_type'] = self.terminal_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoyagerEnvInfo()
        if 'client_ip' in d:
            o.client_ip = d['client_ip']
        if 'os_type' in d:
            o.os_type = d['os_type']
        if 'terminal_type' in d:
            o.terminal_type = d['terminal_type']
        return o


