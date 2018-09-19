#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniVersionGrayOnlineResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniVersionGrayOnlineResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniVersionGrayOnlineResponse, self).parse_response_content(response_content)
