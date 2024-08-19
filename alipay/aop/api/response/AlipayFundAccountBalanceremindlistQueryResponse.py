#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BalanceRemindPlanDTO import BalanceRemindPlanDTO


class AlipayFundAccountBalanceremindlistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAccountBalanceremindlistQueryResponse, self).__init__()
        self._plan_list = None

    @property
    def plan_list(self):
        return self._plan_list

    @plan_list.setter
    def plan_list(self, value):
        if isinstance(value, list):
            self._plan_list = list()
            for i in value:
                if isinstance(i, BalanceRemindPlanDTO):
                    self._plan_list.append(i)
                else:
                    self._plan_list.append(BalanceRemindPlanDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundAccountBalanceremindlistQueryResponse, self).parse_response_content(response_content)
        if 'plan_list' in response:
            self.plan_list = response['plan_list']
