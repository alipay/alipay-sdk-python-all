#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceGasMcardReturnResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceGasMcardReturnResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceGasMcardReturnResponse, self).parse_response_content(response_content)
