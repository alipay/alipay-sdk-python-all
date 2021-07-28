#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantWeikeInvoiceNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantWeikeInvoiceNotifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMerchantWeikeInvoiceNotifyResponse, self).parse_response_content(response_content)
