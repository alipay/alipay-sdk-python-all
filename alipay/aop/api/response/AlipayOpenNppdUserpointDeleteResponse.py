#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenNppdUserpointDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenNppdUserpointDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenNppdUserpointDeleteResponse, self).parse_response_content(response_content)
