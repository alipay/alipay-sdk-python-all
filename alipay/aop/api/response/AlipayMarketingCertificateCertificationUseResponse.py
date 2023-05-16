#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCertificateCertificationUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCertificateCertificationUseResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCertificateCertificationUseResponse, self).parse_response_content(response_content)
