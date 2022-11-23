#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenOperationOpenbizmockQuitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOperationOpenbizmockQuitResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenOperationOpenbizmockQuitResponse, self).parse_response_content(response_content)
