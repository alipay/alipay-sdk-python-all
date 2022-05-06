#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossBaseProcessInstanceUrgeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossBaseProcessInstanceUrgeResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayBossBaseProcessInstanceUrgeResponse, self).parse_response_content(response_content)
