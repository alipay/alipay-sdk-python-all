#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndexTrendVO import IndexTrendVO


class AlipayMerchantQipanTrendQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantQipanTrendQueryResponse, self).__init__()
        self._index_trend_results = None

    @property
    def index_trend_results(self):
        return self._index_trend_results

    @index_trend_results.setter
    def index_trend_results(self, value):
        if isinstance(value, list):
            self._index_trend_results = list()
            for i in value:
                if isinstance(i, IndexTrendVO):
                    self._index_trend_results.append(i)
                else:
                    self._index_trend_results.append(IndexTrendVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantQipanTrendQueryResponse, self).parse_response_content(response_content)
        if 'index_trend_results' in response:
            self.index_trend_results = response['index_trend_results']
