#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskVerifyidentityVoiceprintVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskVerifyidentityVoiceprintVerifyResponse, self).__init__()
        self._asr_content = None
        self._long_verify_session_id = None
        self._verify_code = None
        self._verify_data = None
        self._verify_message = None
        self._verify_pass = None
        self._verify_session_id = None

    @property
    def asr_content(self):
        return self._asr_content

    @asr_content.setter
    def asr_content(self, value):
        self._asr_content = value
    @property
    def long_verify_session_id(self):
        return self._long_verify_session_id

    @long_verify_session_id.setter
    def long_verify_session_id(self, value):
        self._long_verify_session_id = value
    @property
    def verify_code(self):
        return self._verify_code

    @verify_code.setter
    def verify_code(self, value):
        self._verify_code = value
    @property
    def verify_data(self):
        return self._verify_data

    @verify_data.setter
    def verify_data(self, value):
        self._verify_data = value
    @property
    def verify_message(self):
        return self._verify_message

    @verify_message.setter
    def verify_message(self, value):
        self._verify_message = value
    @property
    def verify_pass(self):
        return self._verify_pass

    @verify_pass.setter
    def verify_pass(self, value):
        self._verify_pass = value
    @property
    def verify_session_id(self):
        return self._verify_session_id

    @verify_session_id.setter
    def verify_session_id(self, value):
        self._verify_session_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskVerifyidentityVoiceprintVerifyResponse, self).parse_response_content(response_content)
        if 'asr_content' in response:
            self.asr_content = response['asr_content']
        if 'long_verify_session_id' in response:
            self.long_verify_session_id = response['long_verify_session_id']
        if 'verify_code' in response:
            self.verify_code = response['verify_code']
        if 'verify_data' in response:
            self.verify_data = response['verify_data']
        if 'verify_message' in response:
            self.verify_message = response['verify_message']
        if 'verify_pass' in response:
            self.verify_pass = response['verify_pass']
        if 'verify_session_id' in response:
            self.verify_session_id = response['verify_session_id']
