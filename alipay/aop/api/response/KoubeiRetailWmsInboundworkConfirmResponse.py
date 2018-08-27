#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiRetailWmsInboundworkConfirmResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsInboundworkConfirmResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsInboundworkConfirmResponse, self).parse_response_content(response_content)
