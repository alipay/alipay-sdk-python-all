#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaskBaseInfo import TaskBaseInfo


class AlipayMarketingCampaignTaskSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignTaskSendResponse, self).__init__()
        self._task_base_info = None
        self._task_id = None
        self._trigger_result = None

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
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def trigger_result(self):
        return self._trigger_result

    @trigger_result.setter
    def trigger_result(self, value):
        self._trigger_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignTaskSendResponse, self).parse_response_content(response_content)
        if 'task_base_info' in response:
            self.task_base_info = response['task_base_info']
        if 'task_id' in response:
            self.task_id = response['task_id']
        if 'trigger_result' in response:
            self.trigger_result = response['trigger_result']
