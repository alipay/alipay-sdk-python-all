#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaskInstanceInfo import TaskInstanceInfo
from alipay.aop.api.domain.TaskVoucherBasicInfo import TaskVoucherBasicInfo
from alipay.aop.api.domain.TaskPointRankInfo import TaskPointRankInfo


class AlipayCommerceYuntaskHunterGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskHunterGetResponse, self).__init__()
        self._task_instance_info = None
        self._task_voucher_list = None
        self._user_ranking_info_list = None

    @property
    def task_instance_info(self):
        return self._task_instance_info

    @task_instance_info.setter
    def task_instance_info(self, value):
        if isinstance(value, TaskInstanceInfo):
            self._task_instance_info = value
        else:
            self._task_instance_info = TaskInstanceInfo.from_alipay_dict(value)
    @property
    def task_voucher_list(self):
        return self._task_voucher_list

    @task_voucher_list.setter
    def task_voucher_list(self, value):
        if isinstance(value, list):
            self._task_voucher_list = list()
            for i in value:
                if isinstance(i, TaskVoucherBasicInfo):
                    self._task_voucher_list.append(i)
                else:
                    self._task_voucher_list.append(TaskVoucherBasicInfo.from_alipay_dict(i))
    @property
    def user_ranking_info_list(self):
        return self._user_ranking_info_list

    @user_ranking_info_list.setter
    def user_ranking_info_list(self, value):
        if isinstance(value, list):
            self._user_ranking_info_list = list()
            for i in value:
                if isinstance(i, TaskPointRankInfo):
                    self._user_ranking_info_list.append(i)
                else:
                    self._user_ranking_info_list.append(TaskPointRankInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskHunterGetResponse, self).parse_response_content(response_content)
        if 'task_instance_info' in response:
            self.task_instance_info = response['task_instance_info']
        if 'task_voucher_list' in response:
            self.task_voucher_list = response['task_voucher_list']
        if 'user_ranking_info_list' in response:
            self.user_ranking_info_list = response['user_ranking_info_list']
