#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantMrchsurpActivitysignupCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantMrchsurpActivitysignupCreateResponse, self).__init__()
        self._signup_record_id = None

    @property
    def signup_record_id(self):
        return self._signup_record_id

    @signup_record_id.setter
    def signup_record_id(self, value):
        self._signup_record_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantMrchsurpActivitysignupCreateResponse, self).parse_response_content(response_content)
        if 'signup_record_id' in response:
            self.signup_record_id = response['signup_record_id']
