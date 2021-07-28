#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoPrinterStatusNotifyModel(object):

    def __init__(self):
        self._eprint_sign = None
        self._machine_code = None
        self._oauth_type = None
        self._online = None
        self._push_time = None

    @property
    def eprint_sign(self):
        return self._eprint_sign

    @eprint_sign.setter
    def eprint_sign(self, value):
        self._eprint_sign = value
    @property
    def machine_code(self):
        return self._machine_code

    @machine_code.setter
    def machine_code(self, value):
        self._machine_code = value
    @property
    def oauth_type(self):
        return self._oauth_type

    @oauth_type.setter
    def oauth_type(self, value):
        self._oauth_type = value
    @property
    def online(self):
        return self._online

    @online.setter
    def online(self, value):
        self._online = value
    @property
    def push_time(self):
        return self._push_time

    @push_time.setter
    def push_time(self, value):
        self._push_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.eprint_sign:
            if hasattr(self.eprint_sign, 'to_alipay_dict'):
                params['eprint_sign'] = self.eprint_sign.to_alipay_dict()
            else:
                params['eprint_sign'] = self.eprint_sign
        if self.machine_code:
            if hasattr(self.machine_code, 'to_alipay_dict'):
                params['machine_code'] = self.machine_code.to_alipay_dict()
            else:
                params['machine_code'] = self.machine_code
        if self.oauth_type:
            if hasattr(self.oauth_type, 'to_alipay_dict'):
                params['oauth_type'] = self.oauth_type.to_alipay_dict()
            else:
                params['oauth_type'] = self.oauth_type
        if self.online:
            if hasattr(self.online, 'to_alipay_dict'):
                params['online'] = self.online.to_alipay_dict()
            else:
                params['online'] = self.online
        if self.push_time:
            if hasattr(self.push_time, 'to_alipay_dict'):
                params['push_time'] = self.push_time.to_alipay_dict()
            else:
                params['push_time'] = self.push_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoPrinterStatusNotifyModel()
        if 'eprint_sign' in d:
            o.eprint_sign = d['eprint_sign']
        if 'machine_code' in d:
            o.machine_code = d['machine_code']
        if 'oauth_type' in d:
            o.oauth_type = d['oauth_type']
        if 'online' in d:
            o.online = d['online']
        if 'push_time' in d:
            o.push_time = d['push_time']
        return o


