#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubAccountQueryResult import SubAccountQueryResult


class AnttechOceanbaseSubaccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseSubaccountQueryResponse, self).__init__()
        self._sub_account_query_result = None

    @property
    def sub_account_query_result(self):
        return self._sub_account_query_result

    @sub_account_query_result.setter
    def sub_account_query_result(self, value):
        if isinstance(value, SubAccountQueryResult):
            self._sub_account_query_result = value
        else:
            self._sub_account_query_result = SubAccountQueryResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseSubaccountQueryResponse, self).parse_response_content(response_content)
        if 'sub_account_query_result' in response:
            self.sub_account_query_result = response['sub_account_query_result']
