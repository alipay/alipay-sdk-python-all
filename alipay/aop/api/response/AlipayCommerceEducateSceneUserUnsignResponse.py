#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSceneUserUnsignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSceneUserUnsignResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSceneUserUnsignResponse, self).parse_response_content(response_content)
