#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationActivityMerchantModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationActivityMerchantModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationActivityMerchantModifyResponse, self).parse_response_content(response_content)
