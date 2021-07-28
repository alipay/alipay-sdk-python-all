#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LogisticsCompanyResult import LogisticsCompanyResult


class AlipayCommerceLogisticsLogisticscompanyInstantdeliveryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsLogisticscompanyInstantdeliveryQueryResponse, self).__init__()
        self._logistics_companies = None

    @property
    def logistics_companies(self):
        return self._logistics_companies

    @logistics_companies.setter
    def logistics_companies(self, value):
        if isinstance(value, list):
            self._logistics_companies = list()
            for i in value:
                if isinstance(i, LogisticsCompanyResult):
                    self._logistics_companies.append(i)
                else:
                    self._logistics_companies.append(LogisticsCompanyResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsLogisticscompanyInstantdeliveryQueryResponse, self).parse_response_content(response_content)
        if 'logistics_companies' in response:
            self.logistics_companies = response['logistics_companies']
