#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsMarketingCertificateBatchcreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsMarketingCertificateBatchcreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayInsMarketingCertificateBatchcreateResponse, self).parse_response_content(response_content)
