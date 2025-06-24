#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTerminalEdgecloudSwnetflowCardusageSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTerminalEdgecloudSwnetflowCardusageSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayTerminalEdgecloudSwnetflowCardusageSyncResponse, self).parse_response_content(response_content)
