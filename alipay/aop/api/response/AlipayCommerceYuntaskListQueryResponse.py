#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.YunTaskTemplateInfoDTO import YunTaskTemplateInfoDTO


class AlipayCommerceYuntaskListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskListQueryResponse, self).__init__()
        self._page = None
        self._page_size = None
        self._task_list = None
        self._total_size = None

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def task_list(self):
        return self._task_list

    @task_list.setter
    def task_list(self, value):
        if isinstance(value, list):
            self._task_list = list()
            for i in value:
                if isinstance(i, YunTaskTemplateInfoDTO):
                    self._task_list.append(i)
                else:
                    self._task_list.append(YunTaskTemplateInfoDTO.from_alipay_dict(i))
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskListQueryResponse, self).parse_response_content(response_content)
        if 'page' in response:
            self.page = response['page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'task_list' in response:
            self.task_list = response['task_list']
        if 'total_size' in response:
            self.total_size = response['total_size']
