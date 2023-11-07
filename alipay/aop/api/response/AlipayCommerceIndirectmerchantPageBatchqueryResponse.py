#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndirectMerchantProcessorResponse import IndirectMerchantProcessorResponse


class AlipayCommerceIndirectmerchantPageBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIndirectmerchantPageBatchqueryResponse, self).__init__()
        self._content = None
        self._page_num = None
        self._page_size = None
        self._total_num = None
        self._total_size = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, list):
            self._content = list()
            for i in value:
                if isinstance(i, IndirectMerchantProcessorResponse):
                    self._content.append(i)
                else:
                    self._content.append(IndirectMerchantProcessorResponse.from_alipay_dict(i))
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
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIndirectmerchantPageBatchqueryResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_num' in response:
            self.total_num = response['total_num']
        if 'total_size' in response:
            self.total_size = response['total_size']
