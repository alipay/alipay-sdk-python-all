#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QueryUserTaskListResponse import QueryUserTaskListResponse


class AlipayCommerceWaterUsertaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceWaterUsertaskQueryResponse, self).__init__()
        self._user_task_list_info = None

    @property
    def user_task_list_info(self):
        return self._user_task_list_info

    @user_task_list_info.setter
    def user_task_list_info(self, value):
        if isinstance(value, QueryUserTaskListResponse):
            self._user_task_list_info = value
        else:
            self._user_task_list_info = QueryUserTaskListResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceWaterUsertaskQueryResponse, self).parse_response_content(response_content)
        if 'user_task_list_info' in response:
            self.user_task_list_info = response['user_task_list_info']
