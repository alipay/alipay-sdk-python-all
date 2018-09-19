#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserCrowdConditions import UserCrowdConditions


class KoubeiCateringCrowdgroupConditionQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringCrowdgroupConditionQueryResponse, self).__init__()
        self._condition_list = None

    @property
    def condition_list(self):
        return self._condition_list

    @condition_list.setter
    def condition_list(self, value):
        if isinstance(value, list):
            self._condition_list = list()
            for i in value:
                if isinstance(i, UserCrowdConditions):
                    self._condition_list.append(i)
                else:
                    self._condition_list.append(UserCrowdConditions.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringCrowdgroupConditionQueryResponse, self).parse_response_content(response_content)
        if 'condition_list' in response:
            self.condition_list = response['condition_list']
