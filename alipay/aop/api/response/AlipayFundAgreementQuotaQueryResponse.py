#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QuotaQueryResponse import QuotaQueryResponse


class AlipayFundAgreementQuotaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAgreementQuotaQueryResponse, self).__init__()
        self._quota_query_response_list = None

    @property
    def quota_query_response_list(self):
        return self._quota_query_response_list

    @quota_query_response_list.setter
    def quota_query_response_list(self, value):
        if isinstance(value, list):
            self._quota_query_response_list = list()
            for i in value:
                if isinstance(i, QuotaQueryResponse):
                    self._quota_query_response_list.append(i)
                else:
                    self._quota_query_response_list.append(QuotaQueryResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundAgreementQuotaQueryResponse, self).parse_response_content(response_content)
        if 'quota_query_response_list' in response:
            self.quota_query_response_list = response['quota_query_response_list']
