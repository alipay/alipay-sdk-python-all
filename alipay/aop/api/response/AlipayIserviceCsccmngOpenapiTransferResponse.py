#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCsccmngOpenapiTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCsccmngOpenapiTransferResponse, self).__init__()
        self._result_content = None

    @property
    def result_content(self):
        return self._result_content

    @result_content.setter
    def result_content(self, value):
        self._result_content = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCsccmngOpenapiTransferResponse, self).parse_response_content(response_content)
        if 'result_content' in response:
            self.result_content = response['result_content']
