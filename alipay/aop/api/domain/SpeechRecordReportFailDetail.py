#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpeechRecordReportFailDetail(object):

    def __init__(self):
        self._error_code = None
        self._error_msg = None
        self._speech_id = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def speech_id(self):
        return self._speech_id

    @speech_id.setter
    def speech_id(self, value):
        self._speech_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        if self.speech_id:
            if hasattr(self.speech_id, 'to_alipay_dict'):
                params['speech_id'] = self.speech_id.to_alipay_dict()
            else:
                params['speech_id'] = self.speech_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpeechRecordReportFailDetail()
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'speech_id' in d:
            o.speech_id = d['speech_id']
        return o


