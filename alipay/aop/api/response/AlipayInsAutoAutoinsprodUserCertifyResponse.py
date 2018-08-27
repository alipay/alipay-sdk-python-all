#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsAutoAutoinsprodUserCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoAutoinsprodUserCertifyResponse, self).__init__()
        self._agent_cert_result = None

    @property
    def agent_cert_result(self):
        return self._agent_cert_result

    @agent_cert_result.setter
    def agent_cert_result(self, value):
        self._agent_cert_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoAutoinsprodUserCertifyResponse, self).parse_response_content(response_content)
        if 'agent_cert_result' in response:
            self.agent_cert_result = response['agent_cert_result']
