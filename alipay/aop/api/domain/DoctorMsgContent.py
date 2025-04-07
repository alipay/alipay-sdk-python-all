#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DoctorMsgContent(object):

    def __init__(self):
        self._ext_doctor_id = None
        self._platform_code = None
        self._qualification_status = None
        self._reason = None
        self._time_stamp = None

    @property
    def ext_doctor_id(self):
        return self._ext_doctor_id

    @ext_doctor_id.setter
    def ext_doctor_id(self, value):
        self._ext_doctor_id = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def qualification_status(self):
        return self._qualification_status

    @qualification_status.setter
    def qualification_status(self, value):
        self._qualification_status = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def time_stamp(self):
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, value):
        self._time_stamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_doctor_id:
            if hasattr(self.ext_doctor_id, 'to_alipay_dict'):
                params['ext_doctor_id'] = self.ext_doctor_id.to_alipay_dict()
            else:
                params['ext_doctor_id'] = self.ext_doctor_id
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.qualification_status:
            if hasattr(self.qualification_status, 'to_alipay_dict'):
                params['qualification_status'] = self.qualification_status.to_alipay_dict()
            else:
                params['qualification_status'] = self.qualification_status
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
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
        o = DoctorMsgContent()
        if 'ext_doctor_id' in d:
            o.ext_doctor_id = d['ext_doctor_id']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'qualification_status' in d:
            o.qualification_status = d['qualification_status']
        if 'reason' in d:
            o.reason = d['reason']
        if 'time_stamp' in d:
            o.time_stamp = d['time_stamp']
        return o


