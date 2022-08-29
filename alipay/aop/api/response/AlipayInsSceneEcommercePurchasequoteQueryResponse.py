#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PurchaseQueryResultDTO import PurchaseQueryResultDTO


class AlipayInsSceneEcommercePurchasequoteQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEcommercePurchasequoteQueryResponse, self).__init__()
        self._purchase_query_results = None

    @property
    def purchase_query_results(self):
        return self._purchase_query_results

    @purchase_query_results.setter
    def purchase_query_results(self, value):
        if isinstance(value, PurchaseQueryResultDTO):
            self._purchase_query_results = value
        else:
            self._purchase_query_results = PurchaseQueryResultDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEcommercePurchasequoteQueryResponse, self).parse_response_content(response_content)
        if 'purchase_query_results' in response:
            self.purchase_query_results = response['purchase_query_results']
