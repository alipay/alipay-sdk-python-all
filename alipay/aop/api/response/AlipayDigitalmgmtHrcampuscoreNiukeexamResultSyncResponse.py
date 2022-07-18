#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NiukeExamCallbackResult import NiukeExamCallbackResult


class AlipayDigitalmgmtHrcampuscoreNiukeexamResultSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtHrcampuscoreNiukeexamResultSyncResponse, self).__init__()
        self._niuke_exam_callback_result = None
        self._success = None

    @property
    def niuke_exam_callback_result(self):
        return self._niuke_exam_callback_result

    @niuke_exam_callback_result.setter
    def niuke_exam_callback_result(self, value):
        if isinstance(value, NiukeExamCallbackResult):
            self._niuke_exam_callback_result = value
        else:
            self._niuke_exam_callback_result = NiukeExamCallbackResult.from_alipay_dict(value)
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtHrcampuscoreNiukeexamResultSyncResponse, self).parse_response_content(response_content)
        if 'niuke_exam_callback_result' in response:
            self.niuke_exam_callback_result = response['niuke_exam_callback_result']
        if 'success' in response:
            self.success = response['success']
