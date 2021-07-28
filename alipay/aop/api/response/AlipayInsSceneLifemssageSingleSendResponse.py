#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneLifemssageSingleSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneLifemssageSingleSendResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneLifemssageSingleSendResponse, self).parse_response_content(response_content)
