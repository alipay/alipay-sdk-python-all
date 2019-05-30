#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppPropertyMessageSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppPropertyMessageSendResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppPropertyMessageSendResponse, self).parse_response_content(response_content)
