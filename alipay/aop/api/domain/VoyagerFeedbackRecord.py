#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoyagerFeedbackRecord(object):

    def __init__(self):
        self._feedback_ext_info = None
        self._type = None

    @property
    def feedback_ext_info(self):
        return self._feedback_ext_info

    @feedback_ext_info.setter
    def feedback_ext_info(self, value):
        self._feedback_ext_info = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.feedback_ext_info:
            if hasattr(self.feedback_ext_info, 'to_alipay_dict'):
                params['feedback_ext_info'] = self.feedback_ext_info.to_alipay_dict()
            else:
                params['feedback_ext_info'] = self.feedback_ext_info
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoyagerFeedbackRecord()
        if 'feedback_ext_info' in d:
            o.feedback_ext_info = d['feedback_ext_info']
        if 'type' in d:
            o.type = d['type']
        return o


