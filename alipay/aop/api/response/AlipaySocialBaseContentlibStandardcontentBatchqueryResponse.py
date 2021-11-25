#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SourceContentInfo import SourceContentInfo


class AlipaySocialBaseContentlibStandardcontentBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseContentlibStandardcontentBatchqueryResponse, self).__init__()
        self._content_details = None
        self._content_ids = None
        self._page_num = None
        self._page_size = None
        self._total = None

    @property
    def content_details(self):
        return self._content_details

    @content_details.setter
    def content_details(self, value):
        if isinstance(value, list):
            self._content_details = list()
            for i in value:
                if isinstance(i, SourceContentInfo):
                    self._content_details.append(i)
                else:
                    self._content_details.append(SourceContentInfo.from_alipay_dict(i))
    @property
    def content_ids(self):
        return self._content_ids

    @content_ids.setter
    def content_ids(self, value):
        if isinstance(value, list):
            self._content_ids = list()
            for i in value:
                self._content_ids.append(i)
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
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseContentlibStandardcontentBatchqueryResponse, self).parse_response_content(response_content)
        if 'content_details' in response:
            self.content_details = response['content_details']
        if 'content_ids' in response:
            self.content_ids = response['content_ids']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
