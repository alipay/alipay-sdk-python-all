#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCertificateOrderRefundconfirmcommitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCertificateOrderRefundconfirmcommitResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCertificateOrderRefundconfirmcommitResponse, self).parse_response_content(response_content)
