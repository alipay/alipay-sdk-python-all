#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniVersionOnlineResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniVersionOnlineResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniVersionOnlineResponse, self).parse_response_content(response_content)
