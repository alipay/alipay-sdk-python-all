#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceFsupvTaskCancelResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceFsupvTaskCancelResponse, self).__init__()
        self._fund_supv_task_id = None
        self._task_status = None

    @property
    def fund_supv_task_id(self):
        return self._fund_supv_task_id

    @fund_supv_task_id.setter
    def fund_supv_task_id(self, value):
        self._fund_supv_task_id = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceFsupvTaskCancelResponse, self).parse_response_content(response_content)
        if 'fund_supv_task_id' in response:
            self.fund_supv_task_id = response['fund_supv_task_id']
        if 'task_status' in response:
            self.task_status = response['task_status']
