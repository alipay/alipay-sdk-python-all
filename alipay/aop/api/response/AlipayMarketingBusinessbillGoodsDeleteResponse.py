#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingBusinessbillGoodsDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingBusinessbillGoodsDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMarketingBusinessbillGoodsDeleteResponse, self).parse_response_content(response_content)
