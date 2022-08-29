#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudGeneralsaasFaceSourceCertifyResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudGeneralsaasFaceSourceCertifyResponse, self).__init__()
        self._certify_no = None
        self._mismatch_reason = None
        self._passed = None
        self._quality = None
        self._score = None

    @property
    def certify_no(self):
        return self._certify_no

    @certify_no.setter
    def certify_no(self, value):
        self._certify_no = value
    @property
    def mismatch_reason(self):
        return self._mismatch_reason

    @mismatch_reason.setter
    def mismatch_reason(self, value):
        self._mismatch_reason = value
    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value
    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, value):
        self._quality = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudGeneralsaasFaceSourceCertifyResponse, self).parse_response_content(response_content)
        if 'certify_no' in response:
            self.certify_no = response['certify_no']
        if 'mismatch_reason' in response:
            self.mismatch_reason = response['mismatch_reason']
        if 'passed' in response:
            self.passed = response['passed']
        if 'quality' in response:
            self.quality = response['quality']
        if 'score' in response:
            self.score = response['score']
