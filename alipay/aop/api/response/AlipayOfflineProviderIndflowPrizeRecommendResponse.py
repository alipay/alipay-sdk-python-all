#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AdVoucherPrizeDetail import AdVoucherPrizeDetail


class AlipayOfflineProviderIndflowPrizeRecommendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderIndflowPrizeRecommendResponse, self).__init__()
        self._recommend_prizes = None
        self._record_id = None

    @property
    def recommend_prizes(self):
        return self._recommend_prizes

    @recommend_prizes.setter
    def recommend_prizes(self, value):
        if isinstance(value, list):
            self._recommend_prizes = list()
            for i in value:
                if isinstance(i, AdVoucherPrizeDetail):
                    self._recommend_prizes.append(i)
                else:
                    self._recommend_prizes.append(AdVoucherPrizeDetail.from_alipay_dict(i))
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderIndflowPrizeRecommendResponse, self).parse_response_content(response_content)
        if 'recommend_prizes' in response:
            self.recommend_prizes = response['recommend_prizes']
        if 'record_id' in response:
            self.record_id = response['record_id']
