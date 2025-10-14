#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCcmImplusChatrecordBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmImplusChatrecordBatchqueryResponse, self).__init__()
        self._next = None
        self._rows = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value
    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, value):
        if isinstance(value, list):
            self._rows = list()
            for i in value:
                self._rows.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmImplusChatrecordBatchqueryResponse, self).parse_response_content(response_content)
        if 'next' in response:
            self.next = response['next']
        if 'rows' in response:
            self.rows = response['rows']
