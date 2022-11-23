#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInstserviceSignresultBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInstserviceSignresultBatchqueryResponse, self).__init__()
        self._list = None

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        self._list = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInstserviceSignresultBatchqueryResponse, self).parse_response_content(response_content)
        if 'list' in response:
            self.list = response['list']
