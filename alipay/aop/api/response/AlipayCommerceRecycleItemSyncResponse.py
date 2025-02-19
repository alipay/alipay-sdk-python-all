#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRecycleItemSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleItemSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleItemSyncResponse, self).parse_response_content(response_content)
