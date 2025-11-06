#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NotifyRecord import NotifyRecord


class AlipayIserviceCcmCrmNotifyrecordQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmCrmNotifyrecordQueryResponse, self).__init__()
        self._current_page = None
        self._notify_record_list = None
        self._page_size = None
        self._total_page = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def notify_record_list(self):
        return self._notify_record_list

    @notify_record_list.setter
    def notify_record_list(self, value):
        if isinstance(value, list):
            self._notify_record_list = list()
            for i in value:
                if isinstance(i, NotifyRecord):
                    self._notify_record_list.append(i)
                else:
                    self._notify_record_list.append(NotifyRecord.from_alipay_dict(i))
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmCrmNotifyrecordQueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'notify_record_list' in response:
            self.notify_record_list = response['notify_record_list']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_page' in response:
            self.total_page = response['total_page']
