#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppEbppWsgwMsgSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppEbppWsgwMsgSendResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEbppEbppWsgwMsgSendResponse, self).parse_response_content(response_content)
