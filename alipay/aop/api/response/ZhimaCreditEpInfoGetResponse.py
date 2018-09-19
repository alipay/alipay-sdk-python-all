#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CompanyInfo import CompanyInfo


class ZhimaCreditEpInfoGetResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpInfoGetResponse, self).__init__()
        self._biz_no = None
        self._company_info = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def company_info(self):
        return self._company_info

    @company_info.setter
    def company_info(self, value):
        if isinstance(value, CompanyInfo):
            self._company_info = value
        else:
            self._company_info = CompanyInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpInfoGetResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'company_info' in response:
            self.company_info = response['company_info']
