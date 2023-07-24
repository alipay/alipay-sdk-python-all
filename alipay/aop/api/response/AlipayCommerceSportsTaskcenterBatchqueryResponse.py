#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserTaskSimpleDto import UserTaskSimpleDto


class AlipayCommerceSportsTaskcenterBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSportsTaskcenterBatchqueryResponse, self).__init__()
        self._user_task_list = None

    @property
    def user_task_list(self):
        return self._user_task_list

    @user_task_list.setter
    def user_task_list(self, value):
        if isinstance(value, list):
            self._user_task_list = list()
            for i in value:
                if isinstance(i, UserTaskSimpleDto):
                    self._user_task_list.append(i)
                else:
                    self._user_task_list.append(UserTaskSimpleDto.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSportsTaskcenterBatchqueryResponse, self).parse_response_content(response_content)
        if 'user_task_list' in response:
            self.user_task_list = response['user_task_list']
