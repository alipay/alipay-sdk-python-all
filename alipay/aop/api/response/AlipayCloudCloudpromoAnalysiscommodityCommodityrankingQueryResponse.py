#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiOperationalAnalysisGoodsRankResult import OpenApiOperationalAnalysisGoodsRankResult


class AlipayCloudCloudpromoAnalysiscommodityCommodityrankingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoAnalysiscommodityCommodityrankingQueryResponse, self).__init__()
        self._results = None

    @property
    def results(self):
        return self._results

    @results.setter
    def results(self, value):
        if isinstance(value, OpenApiOperationalAnalysisGoodsRankResult):
            self._results = value
        else:
            self._results = OpenApiOperationalAnalysisGoodsRankResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoAnalysiscommodityCommodityrankingQueryResponse, self).parse_response_content(response_content)
        if 'results' in response:
            self.results = response['results']
