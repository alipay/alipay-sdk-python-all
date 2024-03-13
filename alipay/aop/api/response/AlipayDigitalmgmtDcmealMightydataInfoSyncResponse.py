#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalmgmtDcmealMightydataInfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtDcmealMightydataInfoSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtDcmealMightydataInfoSyncResponse, self).parse_response_content(response_content)
