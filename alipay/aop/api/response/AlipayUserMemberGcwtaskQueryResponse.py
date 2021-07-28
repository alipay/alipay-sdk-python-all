#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SquareDanceTaskInfo import SquareDanceTaskInfo


class AlipayUserMemberGcwtaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserMemberGcwtaskQueryResponse, self).__init__()
        self._result_code = None
        self._square_dance_task_info_list = None
        self._success = None

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def square_dance_task_info_list(self):
        return self._square_dance_task_info_list

    @square_dance_task_info_list.setter
    def square_dance_task_info_list(self, value):
        if isinstance(value, list):
            self._square_dance_task_info_list = list()
            for i in value:
                if isinstance(i, SquareDanceTaskInfo):
                    self._square_dance_task_info_list.append(i)
                else:
                    self._square_dance_task_info_list.append(SquareDanceTaskInfo.from_alipay_dict(i))
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserMemberGcwtaskQueryResponse, self).parse_response_content(response_content)
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'square_dance_task_info_list' in response:
            self.square_dance_task_info_list = response['square_dance_task_info_list']
        if 'success' in response:
            self.success = response['success']
