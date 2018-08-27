#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceTitleSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceTitleSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceTitleSyncResponse, self).parse_response_content(response_content)
