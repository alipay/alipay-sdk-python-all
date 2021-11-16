#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarUserAgreementQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarUserAgreementQueryResponse, self).__init__()
        self._message_activate = None
        self._senior_certificated = None

    @property
    def message_activate(self):
        return self._message_activate

    @message_activate.setter
    def message_activate(self, value):
        self._message_activate = value
    @property
    def senior_certificated(self):
        return self._senior_certificated

    @senior_certificated.setter
    def senior_certificated(self, value):
        self._senior_certificated = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarUserAgreementQueryResponse, self).parse_response_content(response_content)
        if 'message_activate' in response:
            self.message_activate = response['message_activate']
        if 'senior_certificated' in response:
            self.senior_certificated = response['senior_certificated']
