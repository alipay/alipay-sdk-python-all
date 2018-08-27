#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataFindataReportQueryResponse(AlipayResponse):

    def __init__(self):
        super(SsdataFindataReportQueryResponse, self).__init__()
        self._biz_content = None
        self._biz_no = None
        self._org_biz_no = None

    @property
    def biz_content(self):
        return self._biz_content

    @biz_content.setter
    def biz_content(self, value):
        self._biz_content = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def org_biz_no(self):
        return self._org_biz_no

    @org_biz_no.setter
    def org_biz_no(self, value):
        self._org_biz_no = value

    def parse_response_content(self, response_content):
        response = super(SsdataFindataReportQueryResponse, self).parse_response_content(response_content)
        if 'biz_content' in response:
            self.biz_content = response['biz_content']
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'org_biz_no' in response:
            self.org_biz_no = response['org_biz_no']
