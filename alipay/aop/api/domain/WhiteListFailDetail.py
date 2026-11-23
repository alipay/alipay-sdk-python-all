#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WhiteListFailDetail(object):

    def __init__(self):
        self._device_sn = None
        self._fail_msg = None

    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def fail_msg(self):
        return self._fail_msg

    @fail_msg.setter
    def fail_msg(self, value):
        self._fail_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.fail_msg:
            if hasattr(self.fail_msg, 'to_alipay_dict'):
                params['fail_msg'] = self.fail_msg.to_alipay_dict()
            else:
                params['fail_msg'] = self.fail_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WhiteListFailDetail()
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'fail_msg' in d:
            o.fail_msg = d['fail_msg']
        return o


