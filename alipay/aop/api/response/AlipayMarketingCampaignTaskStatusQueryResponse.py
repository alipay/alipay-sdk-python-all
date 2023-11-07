#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaskPrizeSendInfo import TaskPrizeSendInfo
from alipay.aop.api.domain.TaskStatusInfo import TaskStatusInfo


class AlipayMarketingCampaignTaskStatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignTaskStatusQueryResponse, self).__init__()
        self._task_prize_send_info_list = None
        self._task_status_list = None

    @property
    def task_prize_send_info_list(self):
        return self._task_prize_send_info_list

    @task_prize_send_info_list.setter
    def task_prize_send_info_list(self, value):
        if isinstance(value, list):
            self._task_prize_send_info_list = list()
            for i in value:
                if isinstance(i, TaskPrizeSendInfo):
                    self._task_prize_send_info_list.append(i)
                else:
                    self._task_prize_send_info_list.append(TaskPrizeSendInfo.from_alipay_dict(i))
    @property
    def task_status_list(self):
        return self._task_status_list

    @task_status_list.setter
    def task_status_list(self, value):
        if isinstance(value, list):
            self._task_status_list = list()
            for i in value:
                if isinstance(i, TaskStatusInfo):
                    self._task_status_list.append(i)
                else:
                    self._task_status_list.append(TaskStatusInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignTaskStatusQueryResponse, self).parse_response_content(response_content)
        if 'task_prize_send_info_list' in response:
            self.task_prize_send_info_list = response['task_prize_send_info_list']
        if 'task_status_list' in response:
            self.task_status_list = response['task_status_list']
