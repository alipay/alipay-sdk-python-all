#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppEbppShareStatusSetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppEbppShareStatusSetResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEbppEbppShareStatusSetResponse, self).parse_response_content(response_content)
