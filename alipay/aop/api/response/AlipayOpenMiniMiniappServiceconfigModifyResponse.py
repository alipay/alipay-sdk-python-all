#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniMiniappServiceconfigModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniMiniappServiceconfigModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniMiniappServiceconfigModifyResponse, self).parse_response_content(response_content)
