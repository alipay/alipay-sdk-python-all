#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CarbonJusticeQueryOpenapiDTO import CarbonJusticeQueryOpenapiDTO


class AlipayCommerceTransportCarbonjusticeLowcarbonbehaviorQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportCarbonjusticeLowcarbonbehaviorQueryResponse, self).__init__()
        self._carbon_justice_model_list = None

    @property
    def carbon_justice_model_list(self):
        return self._carbon_justice_model_list

    @carbon_justice_model_list.setter
    def carbon_justice_model_list(self, value):
        if isinstance(value, list):
            self._carbon_justice_model_list = list()
            for i in value:
                if isinstance(i, CarbonJusticeQueryOpenapiDTO):
                    self._carbon_justice_model_list.append(i)
                else:
                    self._carbon_justice_model_list.append(CarbonJusticeQueryOpenapiDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportCarbonjusticeLowcarbonbehaviorQueryResponse, self).parse_response_content(response_content)
        if 'carbon_justice_model_list' in response:
            self.carbon_justice_model_list = response['carbon_justice_model_list']
