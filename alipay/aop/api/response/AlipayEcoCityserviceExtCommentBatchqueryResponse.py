#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CmtContentBackFlow import CmtContentBackFlow


class AlipayEcoCityserviceExtCommentBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCityserviceExtCommentBatchqueryResponse, self).__init__()
        self._comment_list = None
        self._page_number = None
        self._page_size = None
        self._total = None

    @property
    def comment_list(self):
        return self._comment_list

    @comment_list.setter
    def comment_list(self, value):
        if isinstance(value, list):
            self._comment_list = list()
            for i in value:
                if isinstance(i, CmtContentBackFlow):
                    self._comment_list.append(i)
                else:
                    self._comment_list.append(CmtContentBackFlow.from_alipay_dict(i))
    @property
    def page_number(self):
        return self._page_number

    @page_number.setter
    def page_number(self, value):
        self._page_number = value
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
        response = super(AlipayEcoCityserviceExtCommentBatchqueryResponse, self).parse_response_content(response_content)
        if 'comment_list' in response:
            self.comment_list = response['comment_list']
        if 'page_number' in response:
            self.page_number = response['page_number']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
