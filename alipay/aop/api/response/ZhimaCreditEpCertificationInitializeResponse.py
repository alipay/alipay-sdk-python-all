#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpCertificationInitializeResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpCertificationInitializeResponse, self).__init__()
        self._biz_no = None
        self._org_biz_no = None

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
        response = super(ZhimaCreditEpCertificationInitializeResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'org_biz_no' in response:
            self.org_biz_no = response['org_biz_no']
