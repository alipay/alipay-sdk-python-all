#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExportBillkey import ExportBillkey


class AlipayEbppJfexportBillkeyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJfexportBillkeyQueryResponse, self).__init__()
        self._billkey_list = None

    @property
    def billkey_list(self):
        return self._billkey_list

    @billkey_list.setter
    def billkey_list(self, value):
        if isinstance(value, list):
            self._billkey_list = list()
            for i in value:
                if isinstance(i, ExportBillkey):
                    self._billkey_list.append(i)
                else:
                    self._billkey_list.append(ExportBillkey.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJfexportBillkeyQueryResponse, self).parse_response_content(response_content)
        if 'billkey_list' in response:
            self.billkey_list = response['billkey_list']
