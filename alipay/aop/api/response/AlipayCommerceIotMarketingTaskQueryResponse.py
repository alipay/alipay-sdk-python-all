#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ISPTaskInfo import ISPTaskInfo


class AlipayCommerceIotMarketingTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotMarketingTaskQueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._pages = None
        self._task_info_list = None
        self._total_count = None

    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        self._pages = value
    @property
    def task_info_list(self):
        return self._task_info_list

    @task_info_list.setter
    def task_info_list(self, value):
        if isinstance(value, list):
            self._task_info_list = list()
            for i in value:
                if isinstance(i, ISPTaskInfo):
                    self._task_info_list.append(i)
                else:
                    self._task_info_list.append(ISPTaskInfo.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotMarketingTaskQueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'pages' in response:
            self.pages = response['pages']
        if 'task_info_list' in response:
            self.task_info_list = response['task_info_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
