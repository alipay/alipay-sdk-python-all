#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiFqqrcodeLogisticsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiFqqrcodeLogisticsQueryResponse, self).__init__()
        self._express_company_name = None
        self._express_no = None
        self._status = None

    @property
    def express_company_name(self):
        return self._express_company_name

    @express_company_name.setter
    def express_company_name(self, value):
        self._express_company_name = value
    @property
    def express_no(self):
        return self._express_no

    @express_no.setter
    def express_no(self, value):
        self._express_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiFqqrcodeLogisticsQueryResponse, self).parse_response_content(response_content)
        if 'express_company_name' in response:
            self.express_company_name = response['express_company_name']
        if 'express_no' in response:
            self.express_no = response['express_no']
        if 'status' in response:
            self.status = response['status']
