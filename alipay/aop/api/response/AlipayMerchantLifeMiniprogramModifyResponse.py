#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantLifeMiniprogramModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantLifeMiniprogramModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMerchantLifeMiniprogramModifyResponse, self).parse_response_content(response_content)
