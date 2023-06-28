#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaskInstanceBasicInfoDTO import TaskInstanceBasicInfoDTO


class AlipayCommerceCommonTaskinstanceBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommonTaskinstanceBatchqueryResponse, self).__init__()
        self._page_no = None
        self._page_size = None
        self._task_info_list = None
        self._total_size = None

    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def task_info_list(self):
        return self._task_info_list

    @task_info_list.setter
    def task_info_list(self, value):
        if isinstance(value, list):
            self._task_info_list = list()
            for i in value:
                if isinstance(i, TaskInstanceBasicInfoDTO):
                    self._task_info_list.append(i)
                else:
                    self._task_info_list.append(TaskInstanceBasicInfoDTO.from_alipay_dict(i))
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommonTaskinstanceBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'task_info_list' in response:
            self.task_info_list = response['task_info_list']
        if 'total_size' in response:
            self.total_size = response['total_size']
