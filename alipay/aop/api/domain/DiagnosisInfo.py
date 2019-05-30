#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DiagnosisInfo(object):

    def __init__(self):
        self._decision_code = None
        self._decision_desc = None
        self._orgin_error_code = None
        self._reason_code = None
        self._reason_desc = None
        self._time = None

    @property
    def decision_code(self):
        return self._decision_code

    @decision_code.setter
    def decision_code(self, value):
        self._decision_code = value
    @property
    def decision_desc(self):
        return self._decision_desc

    @decision_desc.setter
    def decision_desc(self, value):
        self._decision_desc = value
    @property
    def orgin_error_code(self):
        return self._orgin_error_code

    @orgin_error_code.setter
    def orgin_error_code(self, value):
        self._orgin_error_code = value
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value
    @property
    def reason_desc(self):
        return self._reason_desc

    @reason_desc.setter
    def reason_desc(self, value):
        self._reason_desc = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.decision_code:
            if hasattr(self.decision_code, 'to_alipay_dict'):
                params['decision_code'] = self.decision_code.to_alipay_dict()
            else:
                params['decision_code'] = self.decision_code
        if self.decision_desc:
            if hasattr(self.decision_desc, 'to_alipay_dict'):
                params['decision_desc'] = self.decision_desc.to_alipay_dict()
            else:
                params['decision_desc'] = self.decision_desc
        if self.orgin_error_code:
            if hasattr(self.orgin_error_code, 'to_alipay_dict'):
                params['orgin_error_code'] = self.orgin_error_code.to_alipay_dict()
            else:
                params['orgin_error_code'] = self.orgin_error_code
        if self.reason_code:
            if hasattr(self.reason_code, 'to_alipay_dict'):
                params['reason_code'] = self.reason_code.to_alipay_dict()
            else:
                params['reason_code'] = self.reason_code
        if self.reason_desc:
            if hasattr(self.reason_desc, 'to_alipay_dict'):
                params['reason_desc'] = self.reason_desc.to_alipay_dict()
            else:
                params['reason_desc'] = self.reason_desc
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiagnosisInfo()
        if 'decision_code' in d:
            o.decision_code = d['decision_code']
        if 'decision_desc' in d:
            o.decision_desc = d['decision_desc']
        if 'orgin_error_code' in d:
            o.orgin_error_code = d['orgin_error_code']
        if 'reason_code' in d:
            o.reason_code = d['reason_code']
        if 'reason_desc' in d:
            o.reason_desc = d['reason_desc']
        if 'time' in d:
            o.time = d['time']
        return o


