#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceBase import ServiceBase


class AlipayOpenAppServiceValidpageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppServiceValidpageQueryResponse, self).__init__()
        self._current_page = None
        self._page_size = None
        self._service_list = None
        self._total = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def service_list(self):
        return self._service_list

    @service_list.setter
    def service_list(self, value):
        if isinstance(value, list):
            self._service_list = list()
            for i in value:
                if isinstance(i, ServiceBase):
                    self._service_list.append(i)
                else:
                    self._service_list.append(ServiceBase.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppServiceValidpageQueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'service_list' in response:
            self.service_list = response['service_list']
        if 'total' in response:
            self.total = response['total']
