#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CompanyDetail import CompanyDetail


class AlipayBossProdCompanyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdCompanyQueryResponse, self).__init__()
        self._open_api_company_query_result = None

    @property
    def open_api_company_query_result(self):
        return self._open_api_company_query_result

    @open_api_company_query_result.setter
    def open_api_company_query_result(self, value):
        if isinstance(value, list):
            self._open_api_company_query_result = list()
            for i in value:
                if isinstance(i, CompanyDetail):
                    self._open_api_company_query_result.append(i)
                else:
                    self._open_api_company_query_result.append(CompanyDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdCompanyQueryResponse, self).parse_response_content(response_content)
        if 'open_api_company_query_result' in response:
            self.open_api_company_query_result = response['open_api_company_query_result']
