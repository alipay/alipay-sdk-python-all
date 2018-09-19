#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OverseasTravelRate import OverseasTravelRate


class AlipayOverseasTravelExchangerateBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelExchangerateBatchqueryResponse, self).__init__()
        self._rate_desc = None
        self._rate_source = None
        self._rates = None

    @property
    def rate_desc(self):
        return self._rate_desc

    @rate_desc.setter
    def rate_desc(self, value):
        self._rate_desc = value
    @property
    def rate_source(self):
        return self._rate_source

    @rate_source.setter
    def rate_source(self, value):
        self._rate_source = value
    @property
    def rates(self):
        return self._rates

    @rates.setter
    def rates(self, value):
        if isinstance(value, list):
            self._rates = list()
            for i in value:
                if isinstance(i, OverseasTravelRate):
                    self._rates.append(i)
                else:
                    self._rates.append(OverseasTravelRate.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelExchangerateBatchqueryResponse, self).parse_response_content(response_content)
        if 'rate_desc' in response:
            self.rate_desc = response['rate_desc']
        if 'rate_source' in response:
            self.rate_source = response['rate_source']
        if 'rates' in response:
            self.rates = response['rates']
