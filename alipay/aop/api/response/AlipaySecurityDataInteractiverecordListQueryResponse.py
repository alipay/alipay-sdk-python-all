#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InteractiveServiceRecordDetail import InteractiveServiceRecordDetail


class AlipaySecurityDataInteractiverecordListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityDataInteractiverecordListQueryResponse, self).__init__()
        self._current_page = None
        self._interact_records = None
        self._page_size = None
        self._total_size = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def interact_records(self):
        return self._interact_records

    @interact_records.setter
    def interact_records(self, value):
        if isinstance(value, list):
            self._interact_records = list()
            for i in value:
                if isinstance(i, InteractiveServiceRecordDetail):
                    self._interact_records.append(i)
                else:
                    self._interact_records.append(InteractiveServiceRecordDetail.from_alipay_dict(i))
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityDataInteractiverecordListQueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'interact_records' in response:
            self.interact_records = response['interact_records']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
