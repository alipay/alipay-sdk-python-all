#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoanapplyBkamcAntauthsignConsultResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoanapplyBkamcAntauthsignConsultResponse, self).__init__()
        self._authed = None

    @property
    def authed(self):
        return self._authed

    @authed.setter
    def authed(self, value):
        self._authed = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoanapplyBkamcAntauthsignConsultResponse, self).parse_response_content(response_content)
        if 'authed' in response:
            self.authed = response['authed']
