#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaskBaseInfo import TaskBaseInfo
from alipay.aop.api.domain.TaskFullInfo import TaskFullInfo


class AlipayMarketingCampaignTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignTaskQueryResponse, self).__init__()
        self._task_base_info = None
        self._task_cen_id = None
        self._task_full_list = None

    @property
    def task_base_info(self):
        return self._task_base_info

    @task_base_info.setter
    def task_base_info(self, value):
        if isinstance(value, TaskBaseInfo):
            self._task_base_info = value
        else:
            self._task_base_info = TaskBaseInfo.from_alipay_dict(value)
    @property
    def task_cen_id(self):
        return self._task_cen_id

    @task_cen_id.setter
    def task_cen_id(self, value):
        self._task_cen_id = value
    @property
    def task_full_list(self):
        return self._task_full_list

    @task_full_list.setter
    def task_full_list(self, value):
        if isinstance(value, list):
            self._task_full_list = list()
            for i in value:
                if isinstance(i, TaskFullInfo):
                    self._task_full_list.append(i)
                else:
                    self._task_full_list.append(TaskFullInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignTaskQueryResponse, self).parse_response_content(response_content)
        if 'task_base_info' in response:
            self.task_base_info = response['task_base_info']
        if 'task_cen_id' in response:
            self.task_cen_id = response['task_cen_id']
        if 'task_full_list' in response:
            self.task_full_list = response['task_full_list']
