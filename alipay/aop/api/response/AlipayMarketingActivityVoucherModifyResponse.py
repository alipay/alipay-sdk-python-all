#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingActivityVoucherModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityVoucherModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityVoucherModifyResponse, self).parse_response_content(response_content)
