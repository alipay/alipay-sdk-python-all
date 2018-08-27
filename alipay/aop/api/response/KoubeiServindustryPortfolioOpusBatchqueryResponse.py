#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpusInfo import OpusInfo


class KoubeiServindustryPortfolioOpusBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiServindustryPortfolioOpusBatchqueryResponse, self).__init__()
        self._opuses = None
        self._total_size = None

    @property
    def opuses(self):
        return self._opuses

    @opuses.setter
    def opuses(self, value):
        if isinstance(value, list):
            self._opuses = list()
            for i in value:
                if isinstance(i, OpusInfo):
                    self._opuses.append(i)
                else:
                    self._opuses.append(OpusInfo.from_alipay_dict(i))
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(KoubeiServindustryPortfolioOpusBatchqueryResponse, self).parse_response_content(response_content)
        if 'opuses' in response:
            self.opuses = response['opuses']
        if 'total_size' in response:
            self.total_size = response['total_size']
