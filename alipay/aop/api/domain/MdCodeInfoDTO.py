#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MdCodeInfoDTO(object):

    def __init__(self):
        self._code_status = None
        self._code_value = None
        self._expire_time = None
        self._time_stamp = None

    @property
    def code_status(self):
        return self._code_status

    @code_status.setter
    def code_status(self, value):
        self._code_status = value
    @property
    def code_value(self):
        return self._code_value

    @code_value.setter
    def code_value(self, value):
        self._code_value = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def time_stamp(self):
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, value):
        self._time_stamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_status:
            if hasattr(self.code_status, 'to_alipay_dict'):
                params['code_status'] = self.code_status.to_alipay_dict()
            else:
                params['code_status'] = self.code_status
        if self.code_value:
            if hasattr(self.code_value, 'to_alipay_dict'):
                params['code_value'] = self.code_value.to_alipay_dict()
            else:
                params['code_value'] = self.code_value
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.time_stamp:
            if hasattr(self.time_stamp, 'to_alipay_dict'):
                params['time_stamp'] = self.time_stamp.to_alipay_dict()
            else:
                params['time_stamp'] = self.time_stamp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MdCodeInfoDTO()
        if 'code_status' in d:
            o.code_status = d['code_status']
        if 'code_value' in d:
            o.code_value = d['code_value']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'time_stamp' in d:
            o.time_stamp = d['time_stamp']
        return o


