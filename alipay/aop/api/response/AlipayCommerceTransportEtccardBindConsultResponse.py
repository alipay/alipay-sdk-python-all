#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtccardBindConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtccardBindConsultResponse, self).__init__()
        self._check_result = None
        self._consult_token = None

    @property
    def check_result(self):
        return self._check_result

    @check_result.setter
    def check_result(self, value):
        self._check_result = value
    @property
    def consult_token(self):
        return self._consult_token

    @consult_token.setter
    def consult_token(self, value):
        self._consult_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtccardBindConsultResponse, self).parse_response_content(response_content)
        if 'check_result' in response:
            self.check_result = response['check_result']
        if 'consult_token' in response:
            self.consult_token = response['consult_token']
