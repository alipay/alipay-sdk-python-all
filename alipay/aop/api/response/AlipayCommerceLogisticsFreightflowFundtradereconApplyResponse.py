#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFreightflowFundtradereconApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowFundtradereconApplyResponse, self).__init__()
        self._biz_no = None
        self._download_url = None
        self._query_date = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def query_date(self):
        return self._query_date

    @query_date.setter
    def query_date(self, value):
        self._query_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowFundtradereconApplyResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'download_url' in response:
            self.download_url = response['download_url']
        if 'query_date' in response:
            self.query_date = response['query_date']
