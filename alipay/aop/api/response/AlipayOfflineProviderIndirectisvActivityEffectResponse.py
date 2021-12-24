#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderIndirectisvActivityEffectResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderIndirectisvActivityEffectResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderIndirectisvActivityEffectResponse, self).parse_response_content(response_content)
