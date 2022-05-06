#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertifyVerificationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertifyVerificationQueryResponse, self).__init__()
        self._mismatch_reason = None
        self._result_code = None
        self._result_msg = None
        self._score = None
        self._source_from = None

    @property
    def mismatch_reason(self):
        return self._mismatch_reason

    @mismatch_reason.setter
    def mismatch_reason(self, value):
        self._mismatch_reason = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def source_from(self):
        return self._source_from

    @source_from.setter
    def source_from(self, value):
        self._source_from = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertifyVerificationQueryResponse, self).parse_response_content(response_content)
        if 'mismatch_reason' in response:
            self.mismatch_reason = response['mismatch_reason']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
        if 'score' in response:
            self.score = response['score']
        if 'source_from' in response:
            self.source_from = response['source_from']
