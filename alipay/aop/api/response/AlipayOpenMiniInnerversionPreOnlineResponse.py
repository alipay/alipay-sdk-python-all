#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerversionPreOnlineResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionPreOnlineResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionPreOnlineResponse, self).parse_response_content(response_content)
