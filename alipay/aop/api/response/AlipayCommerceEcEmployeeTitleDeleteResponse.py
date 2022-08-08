#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcEmployeeTitleDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEmployeeTitleDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEmployeeTitleDeleteResponse, self).parse_response_content(response_content)
