#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniPayeeBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniPayeeBindResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniPayeeBindResponse, self).parse_response_content(response_content)
