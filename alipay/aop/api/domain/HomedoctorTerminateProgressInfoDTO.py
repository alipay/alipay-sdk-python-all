#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HomedoctorTerminateProgressInfoDTO(object):

    def __init__(self):
        self._reject_reason = None
        self._terminate_time = None

    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def terminate_time(self):
        return self._terminate_time

    @terminate_time.setter
    def terminate_time(self, value):
        self._terminate_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        if self.terminate_time:
            if hasattr(self.terminate_time, 'to_alipay_dict'):
                params['terminate_time'] = self.terminate_time.to_alipay_dict()
            else:
                params['terminate_time'] = self.terminate_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HomedoctorTerminateProgressInfoDTO()
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'terminate_time' in d:
            o.terminate_time = d['terminate_time']
        return o


