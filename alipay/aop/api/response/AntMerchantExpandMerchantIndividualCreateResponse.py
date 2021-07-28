#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandMerchantIndividualCreateResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandMerchantIndividualCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandMerchantIndividualCreateResponse, self).parse_response_content(response_content)
