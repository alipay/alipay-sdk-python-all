#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderNpassporterVerifyresultinfoCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderNpassporterVerifyresultinfoCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderNpassporterVerifyresultinfoCreateResponse, self).parse_response_content(response_content)
