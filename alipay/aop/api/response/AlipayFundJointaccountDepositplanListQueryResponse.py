#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FundPlanDTO import FundPlanDTO


class AlipayFundJointaccountDepositplanListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountDepositplanListQueryResponse, self).__init__()
        self._fund_plan_list = None

    @property
    def fund_plan_list(self):
        return self._fund_plan_list

    @fund_plan_list.setter
    def fund_plan_list(self, value):
        if isinstance(value, list):
            self._fund_plan_list = list()
            for i in value:
                if isinstance(i, FundPlanDTO):
                    self._fund_plan_list.append(i)
                else:
                    self._fund_plan_list.append(FundPlanDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountDepositplanListQueryResponse, self).parse_response_content(response_content)
        if 'fund_plan_list' in response:
            self.fund_plan_list = response['fund_plan_list']
