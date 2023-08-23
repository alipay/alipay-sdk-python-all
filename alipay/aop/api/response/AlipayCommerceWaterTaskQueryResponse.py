#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PrizeResponse import PrizeResponse


class AlipayCommerceWaterTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceWaterTaskQueryResponse, self).__init__()
        self._creator = None
        self._creator_open_id = None
        self._merchant_pid = None
        self._prize_response = None
        self._second_merchant_appid = None
        self._task_condition = None
        self._task_contract_period = None
        self._task_end = None
        self._task_id = None
        self._task_join_count = None
        self._task_name = None
        self._task_start = None
        self._task_status = None
        self._task_title = None

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def creator_open_id(self):
        return self._creator_open_id

    @creator_open_id.setter
    def creator_open_id(self, value):
        self._creator_open_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def prize_response(self):
        return self._prize_response

    @prize_response.setter
    def prize_response(self, value):
        if isinstance(value, PrizeResponse):
            self._prize_response = value
        else:
            self._prize_response = PrizeResponse.from_alipay_dict(value)
    @property
    def second_merchant_appid(self):
        return self._second_merchant_appid

    @second_merchant_appid.setter
    def second_merchant_appid(self, value):
        self._second_merchant_appid = value
    @property
    def task_condition(self):
        return self._task_condition

    @task_condition.setter
    def task_condition(self, value):
        self._task_condition = value
    @property
    def task_contract_period(self):
        return self._task_contract_period

    @task_contract_period.setter
    def task_contract_period(self, value):
        self._task_contract_period = value
    @property
    def task_end(self):
        return self._task_end

    @task_end.setter
    def task_end(self, value):
        self._task_end = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_join_count(self):
        return self._task_join_count

    @task_join_count.setter
    def task_join_count(self, value):
        self._task_join_count = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_start(self):
        return self._task_start

    @task_start.setter
    def task_start(self, value):
        self._task_start = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value
    @property
    def task_title(self):
        return self._task_title

    @task_title.setter
    def task_title(self, value):
        self._task_title = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceWaterTaskQueryResponse, self).parse_response_content(response_content)
        if 'creator' in response:
            self.creator = response['creator']
        if 'creator_open_id' in response:
            self.creator_open_id = response['creator_open_id']
        if 'merchant_pid' in response:
            self.merchant_pid = response['merchant_pid']
        if 'prize_response' in response:
            self.prize_response = response['prize_response']
        if 'second_merchant_appid' in response:
            self.second_merchant_appid = response['second_merchant_appid']
        if 'task_condition' in response:
            self.task_condition = response['task_condition']
        if 'task_contract_period' in response:
            self.task_contract_period = response['task_contract_period']
        if 'task_end' in response:
            self.task_end = response['task_end']
        if 'task_id' in response:
            self.task_id = response['task_id']
        if 'task_join_count' in response:
            self.task_join_count = response['task_join_count']
        if 'task_name' in response:
            self.task_name = response['task_name']
        if 'task_start' in response:
            self.task_start = response['task_start']
        if 'task_status' in response:
            self.task_status = response['task_status']
        if 'task_title' in response:
            self.task_title = response['task_title']
