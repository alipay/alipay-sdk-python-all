#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsureRecomProductPlan import InsureRecomProductPlan


class AlipayFundFlexiblestaffingInsureConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundFlexiblestaffingInsureConsultResponse, self).__init__()
        self._recom_product_plan_list = None

    @property
    def recom_product_plan_list(self):
        return self._recom_product_plan_list

    @recom_product_plan_list.setter
    def recom_product_plan_list(self, value):
        if isinstance(value, list):
            self._recom_product_plan_list = list()
            for i in value:
                if isinstance(i, InsureRecomProductPlan):
                    self._recom_product_plan_list.append(i)
                else:
                    self._recom_product_plan_list.append(InsureRecomProductPlan.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundFlexiblestaffingInsureConsultResponse, self).parse_response_content(response_content)
        if 'recom_product_plan_list' in response:
            self.recom_product_plan_list = response['recom_product_plan_list']
