#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaskInfo import TaskInfo
from alipay.aop.api.domain.TaskTitleInfo import TaskTitleInfo


class AlipayCommerceOperationTaskListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationTaskListQueryResponse, self).__init__()
        self._has_next_page = None
        self._page_number = None
        self._task_list = None
        self._task_title = None
        self._total_pages = None
        self._total_size = None

    @property
    def has_next_page(self):
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, value):
        self._has_next_page = value
    @property
    def page_number(self):
        return self._page_number

    @page_number.setter
    def page_number(self, value):
        self._page_number = value
    @property
    def task_list(self):
        return self._task_list

    @task_list.setter
    def task_list(self, value):
        if isinstance(value, list):
            self._task_list = list()
            for i in value:
                if isinstance(i, TaskInfo):
                    self._task_list.append(i)
                else:
                    self._task_list.append(TaskInfo.from_alipay_dict(i))
    @property
    def task_title(self):
        return self._task_title

    @task_title.setter
    def task_title(self, value):
        if isinstance(value, TaskTitleInfo):
            self._task_title = value
        else:
            self._task_title = TaskTitleInfo.from_alipay_dict(value)
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationTaskListQueryResponse, self).parse_response_content(response_content)
        if 'has_next_page' in response:
            self.has_next_page = response['has_next_page']
        if 'page_number' in response:
            self.page_number = response['page_number']
        if 'task_list' in response:
            self.task_list = response['task_list']
        if 'task_title' in response:
            self.task_title = response['task_title']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
        if 'total_size' in response:
            self.total_size = response['total_size']
