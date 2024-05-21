#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsurePlanDTO import InsurePlanDTO


class AlipayInsSceneEcommerceInsurequoteConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEcommerceInsurequoteConsultResponse, self).__init__()
        self._insure_plan = None

    @property
    def insure_plan(self):
        return self._insure_plan

    @insure_plan.setter
    def insure_plan(self, value):
        if isinstance(value, InsurePlanDTO):
            self._insure_plan = value
        else:
            self._insure_plan = InsurePlanDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEcommerceInsurequoteConsultResponse, self).parse_response_content(response_content)
        if 'insure_plan' in response:
            self.insure_plan = response['insure_plan']
