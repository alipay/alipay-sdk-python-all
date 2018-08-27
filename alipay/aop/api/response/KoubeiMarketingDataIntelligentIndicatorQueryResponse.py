#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingDataIntelligentIndicatorQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataIntelligentIndicatorQueryResponse, self).__init__()
        self._indicator_infos = None

    @property
    def indicator_infos(self):
        return self._indicator_infos

    @indicator_infos.setter
    def indicator_infos(self, value):
        self._indicator_infos = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataIntelligentIndicatorQueryResponse, self).parse_response_content(response_content)
        if 'indicator_infos' in response:
            self.indicator_infos = response['indicator_infos']
