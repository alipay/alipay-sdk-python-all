#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayContentCommercialInteractivecoreRoundstopSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayContentCommercialInteractivecoreRoundstopSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayContentCommercialInteractivecoreRoundstopSyncResponse, self).parse_response_content(response_content)
