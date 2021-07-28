#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FailTaskDetail import FailTaskDetail


class AlipayCommerceAbntaskModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAbntaskModifyResponse, self).__init__()
        self._fail_count = None
        self._fail_task_details = None
        self._success_count = None

    @property
    def fail_count(self):
        return self._fail_count

    @fail_count.setter
    def fail_count(self, value):
        self._fail_count = value
    @property
    def fail_task_details(self):
        return self._fail_task_details

    @fail_task_details.setter
    def fail_task_details(self, value):
        if isinstance(value, list):
            self._fail_task_details = list()
            for i in value:
                if isinstance(i, FailTaskDetail):
                    self._fail_task_details.append(i)
                else:
                    self._fail_task_details.append(FailTaskDetail.from_alipay_dict(i))
    @property
    def success_count(self):
        return self._success_count

    @success_count.setter
    def success_count(self, value):
        self._success_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAbntaskModifyResponse, self).parse_response_content(response_content)
        if 'fail_count' in response:
            self.fail_count = response['fail_count']
        if 'fail_task_details' in response:
            self.fail_task_details = response['fail_task_details']
        if 'success_count' in response:
            self.success_count = response['success_count']
