#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditScoreBriefGetResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditScoreBriefGetResponse, self).__init__()
        self._biz_no = None
        self._is_admittance = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def is_admittance(self):
        return self._is_admittance

    @is_admittance.setter
    def is_admittance(self, value):
        self._is_admittance = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditScoreBriefGetResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'is_admittance' in response:
            self.is_admittance = response['is_admittance']
