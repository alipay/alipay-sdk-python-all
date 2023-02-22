#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantMsgTemplateLibVO import MerchantMsgTemplateLibVO


class AlipayOpenMiniMessageTemplatelibBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniMessageTemplatelibBatchqueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._template_lib_list = None
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
    def template_lib_list(self):
        return self._template_lib_list

    @template_lib_list.setter
    def template_lib_list(self, value):
        if isinstance(value, list):
            self._template_lib_list = list()
            for i in value:
                if isinstance(i, MerchantMsgTemplateLibVO):
                    self._template_lib_list.append(i)
                else:
                    self._template_lib_list.append(MerchantMsgTemplateLibVO.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniMessageTemplatelibBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'template_lib_list' in response:
            self.template_lib_list = response['template_lib_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
