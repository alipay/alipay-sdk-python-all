#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ConditionItemPattern import ConditionItemPattern


class KoubeiCateringCrowdgroupConditionSetResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringCrowdgroupConditionSetResponse, self).__init__()
        self._condition_model_list = None
        self._crowd_group_id = None
        self._status = None

    @property
    def condition_model_list(self):
        return self._condition_model_list

    @condition_model_list.setter
    def condition_model_list(self, value):
        if isinstance(value, list):
            self._condition_model_list = list()
            for i in value:
                if isinstance(i, ConditionItemPattern):
                    self._condition_model_list.append(i)
                else:
                    self._condition_model_list.append(ConditionItemPattern.from_alipay_dict(i))
    @property
    def crowd_group_id(self):
        return self._crowd_group_id

    @crowd_group_id.setter
    def crowd_group_id(self, value):
        self._crowd_group_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringCrowdgroupConditionSetResponse, self).parse_response_content(response_content)
        if 'condition_model_list' in response:
            self.condition_model_list = response['condition_model_list']
        if 'crowd_group_id' in response:
            self.crowd_group_id = response['crowd_group_id']
        if 'status' in response:
            self.status = response['status']
