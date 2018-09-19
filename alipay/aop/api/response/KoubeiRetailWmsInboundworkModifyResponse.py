#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiRetailWmsInboundworkModifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsInboundworkModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsInboundworkModifyResponse, self).parse_response_content(response_content)
