#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ArrangementOpenQueryResultVO import ArrangementOpenQueryResultVO


class MybankCreditLoanapplyArrangementQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoanapplyArrangementQueryResponse, self).__init__()
        self._arrangement_query_result = None

    @property
    def arrangement_query_result(self):
        return self._arrangement_query_result

    @arrangement_query_result.setter
    def arrangement_query_result(self, value):
        if isinstance(value, list):
            self._arrangement_query_result = list()
            for i in value:
                if isinstance(i, ArrangementOpenQueryResultVO):
                    self._arrangement_query_result.append(i)
                else:
                    self._arrangement_query_result.append(ArrangementOpenQueryResultVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoanapplyArrangementQueryResponse, self).parse_response_content(response_content)
        if 'arrangement_query_result' in response:
            self.arrangement_query_result = response['arrangement_query_result']
