#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AddPlanGroupResult import AddPlanGroupResult


class AlipayCommerceTransportAdPlanCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportAdPlanCreateResponse, self).__init__()
        self._add_plan_group_result = None

    @property
    def add_plan_group_result(self):
        return self._add_plan_group_result

    @add_plan_group_result.setter
    def add_plan_group_result(self, value):
        if isinstance(value, AddPlanGroupResult):
            self._add_plan_group_result = value
        else:
            self._add_plan_group_result = AddPlanGroupResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportAdPlanCreateResponse, self).parse_response_content(response_content)
        if 'add_plan_group_result' in response:
            self.add_plan_group_result = response['add_plan_group_result']
