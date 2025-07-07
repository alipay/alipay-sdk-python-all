#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftCtocRealtimeTransferResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftCtocRealtimeTransferResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AnttechNftCtocRealtimeTransferResponse, self).parse_response_content(response_content)
