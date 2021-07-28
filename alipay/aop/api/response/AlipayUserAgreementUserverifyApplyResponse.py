#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAgreementUserverifyApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementUserverifyApplyResponse, self).__init__()
        self._apply_token = None

    @property
    def apply_token(self):
        return self._apply_token

    @apply_token.setter
    def apply_token(self, value):
        self._apply_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementUserverifyApplyResponse, self).parse_response_content(response_content)
        if 'apply_token' in response:
            self.apply_token = response['apply_token']
