#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniSafedomainDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniSafedomainDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniSafedomainDeleteResponse, self).parse_response_content(response_content)
