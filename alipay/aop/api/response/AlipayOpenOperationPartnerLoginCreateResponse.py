#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenOperationPartnerLoginCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOperationPartnerLoginCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenOperationPartnerLoginCreateResponse, self).parse_response_content(response_content)
