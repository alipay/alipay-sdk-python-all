#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniVersionOfflineResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniVersionOfflineResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniVersionOfflineResponse, self).parse_response_content(response_content)
