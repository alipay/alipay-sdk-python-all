#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentCarQuoteInfo import RentCarQuoteInfo


class AlipayEcoMycarRentcarQuoteadvQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarRentcarQuoteadvQueryResponse, self).__init__()
        self._quote_infos = None
        self._total_size = None

    @property
    def quote_infos(self):
        return self._quote_infos

    @quote_infos.setter
    def quote_infos(self, value):
        if isinstance(value, list):
            self._quote_infos = list()
            for i in value:
                if isinstance(i, RentCarQuoteInfo):
                    self._quote_infos.append(i)
                else:
                    self._quote_infos.append(RentCarQuoteInfo.from_alipay_dict(i))
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarRentcarQuoteadvQueryResponse, self).parse_response_content(response_content)
        if 'quote_infos' in response:
            self.quote_infos = response['quote_infos']
        if 'total_size' in response:
            self.total_size = response['total_size']
