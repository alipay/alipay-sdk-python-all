#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerversionOfflineResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionOfflineResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionOfflineResponse, self).parse_response_content(response_content)
