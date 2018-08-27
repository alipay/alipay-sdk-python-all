#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMsaasMediarecogVoiceMediaaudioUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogVoiceMediaaudioUploadResponse, self).__init__()
        self._extinfo_a = None
        self._extinfo_b = None
        self._result_memo = None
        self._result_status = None

    @property
    def extinfo_a(self):
        return self._extinfo_a

    @extinfo_a.setter
    def extinfo_a(self, value):
        self._extinfo_a = value
    @property
    def extinfo_b(self):
        return self._extinfo_b

    @extinfo_b.setter
    def extinfo_b(self, value):
        self._extinfo_b = value
    @property
    def result_memo(self):
        return self._result_memo

    @result_memo.setter
    def result_memo(self, value):
        self._result_memo = value
    @property
    def result_status(self):
        return self._result_status

    @result_status.setter
    def result_status(self, value):
        self._result_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogVoiceMediaaudioUploadResponse, self).parse_response_content(response_content)
        if 'extinfo_a' in response:
            self.extinfo_a = response['extinfo_a']
        if 'extinfo_b' in response:
            self.extinfo_b = response['extinfo_b']
        if 'result_memo' in response:
            self.result_memo = response['result_memo']
        if 'result_status' in response:
            self.result_status = response['result_status']
