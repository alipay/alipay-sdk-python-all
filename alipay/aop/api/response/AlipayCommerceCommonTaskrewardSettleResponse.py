#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCommonTaskrewardSettleResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommonTaskrewardSettleResponse, self).__init__()
        self._published_amount = None
        self._reward_amount = None
        self._reward_type = None
        self._task_instance_id = None
        self._total_amount = None

    @property
    def published_amount(self):
        return self._published_amount

    @published_amount.setter
    def published_amount(self, value):
        self._published_amount = value
    @property
    def reward_amount(self):
        return self._reward_amount

    @reward_amount.setter
    def reward_amount(self, value):
        self._reward_amount = value
    @property
    def reward_type(self):
        return self._reward_type

    @reward_type.setter
    def reward_type(self, value):
        self._reward_type = value
    @property
    def task_instance_id(self):
        return self._task_instance_id

    @task_instance_id.setter
    def task_instance_id(self, value):
        self._task_instance_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommonTaskrewardSettleResponse, self).parse_response_content(response_content)
        if 'published_amount' in response:
            self.published_amount = response['published_amount']
        if 'reward_amount' in response:
            self.reward_amount = response['reward_amount']
        if 'reward_type' in response:
            self.reward_type = response['reward_type']
        if 'task_instance_id' in response:
            self.task_instance_id = response['task_instance_id']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
