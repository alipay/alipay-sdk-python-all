#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SmsTemplateDetail import SmsTemplateDetail


class AlipayCloudCloudpromoMessageTemplateBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMessageTemplateBatchqueryResponse, self).__init__()
        self._current_page = None
        self._page_size = None
        self._template_list = None
        self._total_count = None

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
    def template_list(self):
        return self._template_list

    @template_list.setter
    def template_list(self, value):
        if isinstance(value, list):
            self._template_list = list()
            for i in value:
                if isinstance(i, SmsTemplateDetail):
                    self._template_list.append(i)
                else:
                    self._template_list.append(SmsTemplateDetail.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMessageTemplateBatchqueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'template_list' in response:
            self.template_list = response['template_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
