#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BenefitBudgetQueryResultDTO import BenefitBudgetQueryResultDTO
from alipay.aop.api.domain.ResultInfoDTO import ResultInfoDTO


class AlipayOverseasTravelBenefitbudgetQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelBenefitbudgetQueryResponse, self).__init__()
        self._budget_details = None
        self._result = None

    @property
    def budget_details(self):
        return self._budget_details

    @budget_details.setter
    def budget_details(self, value):
        if isinstance(value, list):
            self._budget_details = list()
            for i in value:
                if isinstance(i, BenefitBudgetQueryResultDTO):
                    self._budget_details.append(i)
                else:
                    self._budget_details.append(BenefitBudgetQueryResultDTO.from_alipay_dict(i))
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, ResultInfoDTO):
            self._result = value
        else:
            self._result = ResultInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelBenefitbudgetQueryResponse, self).parse_response_content(response_content)
        if 'budget_details' in response:
            self.budget_details = response['budget_details']
        if 'result' in response:
            self.result = response['result']
