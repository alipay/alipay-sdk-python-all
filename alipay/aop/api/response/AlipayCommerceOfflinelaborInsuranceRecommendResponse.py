#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OfflineLaborRecomInsuranceProduct import OfflineLaborRecomInsuranceProduct


class AlipayCommerceOfflinelaborInsuranceRecommendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOfflinelaborInsuranceRecommendResponse, self).__init__()
        self._recom_product_plan_list = None

    @property
    def recom_product_plan_list(self):
        return self._recom_product_plan_list

    @recom_product_plan_list.setter
    def recom_product_plan_list(self, value):
        if isinstance(value, list):
            self._recom_product_plan_list = list()
            for i in value:
                if isinstance(i, OfflineLaborRecomInsuranceProduct):
                    self._recom_product_plan_list.append(i)
                else:
                    self._recom_product_plan_list.append(OfflineLaborRecomInsuranceProduct.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOfflinelaborInsuranceRecommendResponse, self).parse_response_content(response_content)
        if 'recom_product_plan_list' in response:
            self.recom_product_plan_list = response['recom_product_plan_list']
