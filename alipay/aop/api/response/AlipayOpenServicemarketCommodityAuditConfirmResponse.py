#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenServicemarketCommodityAuditConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenServicemarketCommodityAuditConfirmResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenServicemarketCommodityAuditConfirmResponse, self).parse_response_content(response_content)
