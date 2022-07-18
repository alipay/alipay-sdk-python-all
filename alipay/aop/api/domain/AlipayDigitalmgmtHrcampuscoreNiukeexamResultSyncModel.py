#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NiukeExamCallbackRequest import NiukeExamCallbackRequest


class AlipayDigitalmgmtHrcampuscoreNiukeexamResultSyncModel(object):

    def __init__(self):
        self._niuke_exam_callback_request = None

    @property
    def niuke_exam_callback_request(self):
        return self._niuke_exam_callback_request

    @niuke_exam_callback_request.setter
    def niuke_exam_callback_request(self, value):
        if isinstance(value, NiukeExamCallbackRequest):
            self._niuke_exam_callback_request = value
        else:
            self._niuke_exam_callback_request = NiukeExamCallbackRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.niuke_exam_callback_request:
            if hasattr(self.niuke_exam_callback_request, 'to_alipay_dict'):
                params['niuke_exam_callback_request'] = self.niuke_exam_callback_request.to_alipay_dict()
            else:
                params['niuke_exam_callback_request'] = self.niuke_exam_callback_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtHrcampuscoreNiukeexamResultSyncModel()
        if 'niuke_exam_callback_request' in d:
            o.niuke_exam_callback_request = d['niuke_exam_callback_request']
        return o


