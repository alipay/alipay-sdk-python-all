#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcEnterpriseInfoModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEnterpriseInfoModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEnterpriseInfoModifyResponse, self).parse_response_content(response_content)
