#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSchoolcodeTokenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSchoolcodeTokenCreateResponse, self).__init__()
        self._school_code_token = None

    @property
    def school_code_token(self):
        return self._school_code_token

    @school_code_token.setter
    def school_code_token(self, value):
        self._school_code_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSchoolcodeTokenCreateResponse, self).parse_response_content(response_content)
        if 'school_code_token' in response:
            self.school_code_token = response['school_code_token']
