#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceSearchboxItemSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSearchboxItemSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSearchboxItemSyncResponse, self).parse_response_content(response_content)
