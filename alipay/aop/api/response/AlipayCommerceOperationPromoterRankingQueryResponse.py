#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PointRankingInfo import PointRankingInfo


class AlipayCommerceOperationPromoterRankingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationPromoterRankingQueryResponse, self).__init__()
        self._ranking_info = None

    @property
    def ranking_info(self):
        return self._ranking_info

    @ranking_info.setter
    def ranking_info(self, value):
        if isinstance(value, PointRankingInfo):
            self._ranking_info = value
        else:
            self._ranking_info = PointRankingInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationPromoterRankingQueryResponse, self).parse_response_content(response_content)
        if 'ranking_info' in response:
            self.ranking_info = response['ranking_info']
