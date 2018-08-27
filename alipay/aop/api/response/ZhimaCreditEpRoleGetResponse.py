#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CompanyRole import CompanyRole


class ZhimaCreditEpRoleGetResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpRoleGetResponse, self).__init__()
        self._biz_no = None
        self._company_role = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def company_role(self):
        return self._company_role

    @company_role.setter
    def company_role(self, value):
        if isinstance(value, CompanyRole):
            self._company_role = value
        else:
            self._company_role = CompanyRole.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpRoleGetResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'company_role' in response:
            self.company_role = response['company_role']
