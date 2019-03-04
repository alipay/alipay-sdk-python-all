#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossFncUserinvoiceinfoModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncUserinvoiceinfoModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayBossFncUserinvoiceinfoModifyResponse, self).parse_response_content(response_content)
