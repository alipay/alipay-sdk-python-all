#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniPoiShowstatusModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniPoiShowstatusModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniPoiShowstatusModifyResponse, self).parse_response_content(response_content)
