#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotContentBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotContentBatchqueryResponse, self).__init__()
        self._content_list = None
        self._list_total_count = None
        self._message = None
        self._query_result_code = None
        self._query_token = None

    @property
    def content_list(self):
        return self._content_list

    @content_list.setter
    def content_list(self, value):
        if isinstance(value, list):
            self._content_list = list()
            for i in value:
                self._content_list.append(i)
    @property
    def list_total_count(self):
        return self._list_total_count

    @list_total_count.setter
    def list_total_count(self, value):
        self._list_total_count = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def query_result_code(self):
        return self._query_result_code

    @query_result_code.setter
    def query_result_code(self, value):
        self._query_result_code = value
    @property
    def query_token(self):
        return self._query_token

    @query_token.setter
    def query_token(self, value):
        self._query_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotContentBatchqueryResponse, self).parse_response_content(response_content)
        if 'content_list' in response:
            self.content_list = response['content_list']
        if 'list_total_count' in response:
            self.list_total_count = response['list_total_count']
        if 'message' in response:
            self.message = response['message']
        if 'query_result_code' in response:
            self.query_result_code = response['query_result_code']
        if 'query_token' in response:
            self.query_token = response['query_token']
