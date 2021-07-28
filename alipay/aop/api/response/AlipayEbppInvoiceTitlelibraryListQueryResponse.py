#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceTitlelibraryListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceTitlelibraryListQueryResponse, self).__init__()
        self._title_name_list = None

    @property
    def title_name_list(self):
        return self._title_name_list

    @title_name_list.setter
    def title_name_list(self, value):
        if isinstance(value, list):
            self._title_name_list = list()
            for i in value:
                self._title_name_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceTitlelibraryListQueryResponse, self).parse_response_content(response_content)
        if 'title_name_list' in response:
            self.title_name_list = response['title_name_list']
