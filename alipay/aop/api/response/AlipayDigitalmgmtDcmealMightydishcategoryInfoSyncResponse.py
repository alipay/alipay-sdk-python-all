#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalmgmtDcmealMightydishcategoryInfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtDcmealMightydishcategoryInfoSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtDcmealMightydishcategoryInfoSyncResponse, self).parse_response_content(response_content)
