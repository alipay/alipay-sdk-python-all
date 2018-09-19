#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingDataIndicatorQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataIndicatorQueryResponse, self).__init__()
        self._indicator_infos = None
        self._total_size = None

    @property
    def indicator_infos(self):
        return self._indicator_infos

    @indicator_infos.setter
    def indicator_infos(self, value):
        self._indicator_infos = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataIndicatorQueryResponse, self).parse_response_content(response_content)
        if 'indicator_infos' in response:
            self.indicator_infos = response['indicator_infos']
        if 'total_size' in response:
            self.total_size = response['total_size']
