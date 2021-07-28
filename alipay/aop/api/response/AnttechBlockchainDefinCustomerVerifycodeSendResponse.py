#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainDefinCustomerVerifycodeSendResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinCustomerVerifycodeSendResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinCustomerVerifycodeSendResponse, self).parse_response_content(response_content)
