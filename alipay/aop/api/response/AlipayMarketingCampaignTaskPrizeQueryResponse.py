#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaskPrizeSendInfo import TaskPrizeSendInfo


class AlipayMarketingCampaignTaskPrizeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignTaskPrizeQueryResponse, self).__init__()
        self._task_prize_send_info_list = None

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

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignTaskPrizeQueryResponse, self).parse_response_content(response_content)
        if 'task_prize_send_info_list' in response:
            self.task_prize_send_info_list = response['task_prize_send_info_list']
