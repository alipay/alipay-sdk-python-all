#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotmbsIsvdataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotmbsIsvdataQueryResponse, self).__init__()
        self._content_list = None
        self._list_total_count = None

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

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotmbsIsvdataQueryResponse, self).parse_response_content(response_content)
        if 'content_list' in response:
            self.content_list = response['content_list']
        if 'list_total_count' in response:
            self.list_total_count = response['list_total_count']
