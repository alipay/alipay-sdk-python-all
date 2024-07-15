#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SearchDetailsByInviterRes import SearchDetailsByInviterRes


class AlipayUserAuthRecordByinviterQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAuthRecordByinviterQueryResponse, self).__init__()
        self._orderStr = None
        self._search_res = None

    @property
    def orderStr(self):
        return self._orderStr

    @orderStr.setter
    def orderStr(self, value):
        self._orderStr = value
    @property
    def search_res(self):
        return self._search_res

    @search_res.setter
    def search_res(self, value):
        if isinstance(value, SearchDetailsByInviterRes):
            self._search_res = value
        else:
            self._search_res = SearchDetailsByInviterRes.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserAuthRecordByinviterQueryResponse, self).parse_response_content(response_content)
        if 'orderStr' in response:
            self.orderStr = response['orderStr']
        if 'search_res' in response:
            self.search_res = response['search_res']
