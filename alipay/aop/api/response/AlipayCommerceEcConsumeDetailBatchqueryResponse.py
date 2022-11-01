#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcConsumeInfo import EcConsumeInfo


class AlipayCommerceEcConsumeDetailBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcConsumeDetailBatchqueryResponse, self).__init__()
        self._consume_info_list = None
        self._page_num = None
        self._page_size = None

    @property
    def consume_info_list(self):
        return self._consume_info_list

    @consume_info_list.setter
    def consume_info_list(self, value):
        if isinstance(value, list):
            self._consume_info_list = list()
            for i in value:
                if isinstance(i, EcConsumeInfo):
                    self._consume_info_list.append(i)
                else:
                    self._consume_info_list.append(EcConsumeInfo.from_alipay_dict(i))
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

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcConsumeDetailBatchqueryResponse, self).parse_response_content(response_content)
        if 'consume_info_list' in response:
            self.consume_info_list = response['consume_info_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
