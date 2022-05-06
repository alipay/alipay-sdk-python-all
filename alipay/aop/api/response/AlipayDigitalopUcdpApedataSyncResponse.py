#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalopUcdpApedataSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalopUcdpApedataSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayDigitalopUcdpApedataSyncResponse, self).parse_response_content(response_content)
