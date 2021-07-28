#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossFncGfsettleprodInvoiceDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncGfsettleprodInvoiceDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayBossFncGfsettleprodInvoiceDeleteResponse, self).parse_response_content(response_content)
