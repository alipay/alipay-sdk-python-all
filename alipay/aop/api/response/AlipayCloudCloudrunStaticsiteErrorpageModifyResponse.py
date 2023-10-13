#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ErrorPageSetting import ErrorPageSetting


class AlipayCloudCloudrunStaticsiteErrorpageModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunStaticsiteErrorpageModifyResponse, self).__init__()
        self._domain_list = None
        self._error_page = None

    @property
    def domain_list(self):
        return self._domain_list

    @domain_list.setter
    def domain_list(self, value):
        if isinstance(value, list):
            self._domain_list = list()
            for i in value:
                self._domain_list.append(i)
    @property
    def error_page(self):
        return self._error_page

    @error_page.setter
    def error_page(self, value):
        if isinstance(value, ErrorPageSetting):
            self._error_page = value
        else:
            self._error_page = ErrorPageSetting.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunStaticsiteErrorpageModifyResponse, self).parse_response_content(response_content)
        if 'domain_list' in response:
            self.domain_list = response['domain_list']
        if 'error_page' in response:
            self.error_page = response['error_page']
