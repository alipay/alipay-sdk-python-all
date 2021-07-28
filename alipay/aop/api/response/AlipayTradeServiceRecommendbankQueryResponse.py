#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecommendBankInfo import RecommendBankInfo


class AlipayTradeServiceRecommendbankQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeServiceRecommendbankQueryResponse, self).__init__()
        self._recommend_bank_infos = None

    @property
    def recommend_bank_infos(self):
        return self._recommend_bank_infos

    @recommend_bank_infos.setter
    def recommend_bank_infos(self, value):
        if isinstance(value, list):
            self._recommend_bank_infos = list()
            for i in value:
                if isinstance(i, RecommendBankInfo):
                    self._recommend_bank_infos.append(i)
                else:
                    self._recommend_bank_infos.append(RecommendBankInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayTradeServiceRecommendbankQueryResponse, self).parse_response_content(response_content)
        if 'recommend_bank_infos' in response:
            self.recommend_bank_infos = response['recommend_bank_infos']
