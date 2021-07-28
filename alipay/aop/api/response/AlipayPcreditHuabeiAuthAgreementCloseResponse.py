#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiAuthAgreementCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiAuthAgreementCloseResponse, self).__init__()
        self._out_request_no = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiAuthAgreementCloseResponse, self).parse_response_content(response_content)
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
