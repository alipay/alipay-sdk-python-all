#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniSafedomainCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniSafedomainCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniSafedomainCreateResponse, self).parse_response_content(response_content)
