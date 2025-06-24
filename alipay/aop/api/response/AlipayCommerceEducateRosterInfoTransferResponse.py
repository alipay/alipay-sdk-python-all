#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateRosterInfoTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateRosterInfoTransferResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateRosterInfoTransferResponse, self).parse_response_content(response_content)
