#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaskInstanceRewardInfoDTO import TaskInstanceRewardInfoDTO


class AlipayCommerceCommonTaskdataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommonTaskdataQueryResponse, self).__init__()
        self._reward_info = None
        self._scan_num = None
        self._task_instance_id = None
        self._task_templete_id = None
        self._trade_num = None

    @property
    def reward_info(self):
        return self._reward_info

    @reward_info.setter
    def reward_info(self, value):
        if isinstance(value, list):
            self._reward_info = list()
            for i in value:
                if isinstance(i, TaskInstanceRewardInfoDTO):
                    self._reward_info.append(i)
                else:
                    self._reward_info.append(TaskInstanceRewardInfoDTO.from_alipay_dict(i))
    @property
    def scan_num(self):
        return self._scan_num

    @scan_num.setter
    def scan_num(self, value):
        self._scan_num = value
    @property
    def task_instance_id(self):
        return self._task_instance_id

    @task_instance_id.setter
    def task_instance_id(self, value):
        self._task_instance_id = value
    @property
    def task_templete_id(self):
        return self._task_templete_id

    @task_templete_id.setter
    def task_templete_id(self, value):
        self._task_templete_id = value
    @property
    def trade_num(self):
        return self._trade_num

    @trade_num.setter
    def trade_num(self, value):
        self._trade_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommonTaskdataQueryResponse, self).parse_response_content(response_content)
        if 'reward_info' in response:
            self.reward_info = response['reward_info']
        if 'scan_num' in response:
            self.scan_num = response['scan_num']
        if 'task_instance_id' in response:
            self.task_instance_id = response['task_instance_id']
        if 'task_templete_id' in response:
            self.task_templete_id = response['task_templete_id']
        if 'trade_num' in response:
            self.trade_num = response['trade_num']
