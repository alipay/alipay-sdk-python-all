#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducatePlaceInfoDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducatePlaceInfoDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducatePlaceInfoDeleteResponse, self).parse_response_content(response_content)
