#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateCompetitionErrorresultNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCompetitionErrorresultNotifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCompetitionErrorresultNotifyResponse, self).parse_response_content(response_content)
