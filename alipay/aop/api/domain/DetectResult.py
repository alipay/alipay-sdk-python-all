#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DetectResult(object):

    def __init__(self):
        self._detect_result = None
        self._detect_status = None
        self._event_code = None

    @property
    def detect_result(self):
        return self._detect_result

    @detect_result.setter
    def detect_result(self, value):
        self._detect_result = value
    @property
    def detect_status(self):
        return self._detect_status

    @detect_status.setter
    def detect_status(self, value):
        self._detect_status = value
    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.detect_result:
            if hasattr(self.detect_result, 'to_alipay_dict'):
                params['detect_result'] = self.detect_result.to_alipay_dict()
            else:
                params['detect_result'] = self.detect_result
        if self.detect_status:
            if hasattr(self.detect_status, 'to_alipay_dict'):
                params['detect_status'] = self.detect_status.to_alipay_dict()
            else:
                params['detect_status'] = self.detect_status
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DetectResult()
        if 'detect_result' in d:
            o.detect_result = d['detect_result']
        if 'detect_status' in d:
            o.detect_status = d['detect_status']
        if 'event_code' in d:
            o.event_code = d['event_code']
        return o


