#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceSearchboxCategorySyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSearchboxCategorySyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSearchboxCategorySyncResponse, self).parse_response_content(response_content)
