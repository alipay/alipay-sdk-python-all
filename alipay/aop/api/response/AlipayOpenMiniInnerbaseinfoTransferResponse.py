#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerbaseinfoTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerbaseinfoTransferResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerbaseinfoTransferResponse, self).parse_response_content(response_content)
