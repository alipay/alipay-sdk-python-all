#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserMpointAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserMpointAddResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayUserMpointAddResponse, self).parse_response_content(response_content)
