#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaskDetailInfo import TaskDetailInfo
from alipay.aop.api.domain.TaskVoucherInfo import TaskVoucherInfo


class AlipayCommerceOperationTaskDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationTaskDetailQueryResponse, self).__init__()
        self._task_detail_info = None
        self._task_voucher_list = None

    @property
    def task_detail_info(self):
        return self._task_detail_info

    @task_detail_info.setter
    def task_detail_info(self, value):
        if isinstance(value, TaskDetailInfo):
            self._task_detail_info = value
        else:
            self._task_detail_info = TaskDetailInfo.from_alipay_dict(value)
    @property
    def task_voucher_list(self):
        return self._task_voucher_list

    @task_voucher_list.setter
    def task_voucher_list(self, value):
        if isinstance(value, list):
            self._task_voucher_list = list()
            for i in value:
                if isinstance(i, TaskVoucherInfo):
                    self._task_voucher_list.append(i)
                else:
                    self._task_voucher_list.append(TaskVoucherInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationTaskDetailQueryResponse, self).parse_response_content(response_content)
        if 'task_detail_info' in response:
            self.task_detail_info = response['task_detail_info']
        if 'task_voucher_list' in response:
            self.task_voucher_list = response['task_voucher_list']
