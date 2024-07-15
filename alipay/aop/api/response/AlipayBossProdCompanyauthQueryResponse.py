#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CompanyListQueryResult import CompanyListQueryResult


class AlipayBossProdCompanyauthQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdCompanyauthQueryResponse, self).__init__()
        self._company_list_query_result = None

    @property
    def company_list_query_result(self):
        return self._company_list_query_result

    @company_list_query_result.setter
    def company_list_query_result(self, value):
        if isinstance(value, CompanyListQueryResult):
            self._company_list_query_result = value
        else:
            self._company_list_query_result = CompanyListQueryResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdCompanyauthQueryResponse, self).parse_response_content(response_content)
        if 'company_list_query_result' in response:
            self.company_list_query_result = response['company_list_query_result']
