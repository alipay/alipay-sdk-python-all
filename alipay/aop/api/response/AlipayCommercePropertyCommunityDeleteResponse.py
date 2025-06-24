#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommercePropertyCommunityDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePropertyCommunityDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommercePropertyCommunityDeleteResponse, self).parse_response_content(response_content)
