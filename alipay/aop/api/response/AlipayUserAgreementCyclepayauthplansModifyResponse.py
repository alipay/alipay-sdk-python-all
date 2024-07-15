#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExecutionPlan import ExecutionPlan


class AlipayUserAgreementCyclepayauthplansModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementCyclepayauthplansModifyResponse, self).__init__()
        self._execution_plans = None

    @property
    def execution_plans(self):
        return self._execution_plans

    @execution_plans.setter
    def execution_plans(self, value):
        if isinstance(value, ExecutionPlan):
            self._execution_plans = value
        else:
            self._execution_plans = ExecutionPlan.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementCyclepayauthplansModifyResponse, self).parse_response_content(response_content)
        if 'execution_plans' in response:
            self.execution_plans = response['execution_plans']
