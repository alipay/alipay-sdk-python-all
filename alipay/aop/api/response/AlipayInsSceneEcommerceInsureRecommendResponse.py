#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsureRecommResultDTO import InsureRecommResultDTO
from alipay.aop.api.domain.InsOpenRejectResultDTO import InsOpenRejectResultDTO


class AlipayInsSceneEcommerceInsureRecommendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEcommerceInsureRecommendResponse, self).__init__()
        self._recommend_results = None
        self._reject_results = None

    @property
    def recommend_results(self):
        return self._recommend_results

    @recommend_results.setter
    def recommend_results(self, value):
        if isinstance(value, list):
            self._recommend_results = list()
            for i in value:
                if isinstance(i, InsureRecommResultDTO):
                    self._recommend_results.append(i)
                else:
                    self._recommend_results.append(InsureRecommResultDTO.from_alipay_dict(i))
    @property
    def reject_results(self):
        return self._reject_results

    @reject_results.setter
    def reject_results(self, value):
        if isinstance(value, list):
            self._reject_results = list()
            for i in value:
                if isinstance(i, InsOpenRejectResultDTO):
                    self._reject_results.append(i)
                else:
                    self._reject_results.append(InsOpenRejectResultDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEcommerceInsureRecommendResponse, self).parse_response_content(response_content)
        if 'recommend_results' in response:
            self.recommend_results = response['recommend_results']
        if 'reject_results' in response:
            self.reject_results = response['reject_results']
