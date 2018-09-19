#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TableInfoResult import TableInfoResult


class KoubeiCateringTablelistQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringTablelistQueryResponse, self).__init__()
        self._tableinfo_result = None

    @property
    def tableinfo_result(self):
        return self._tableinfo_result

    @tableinfo_result.setter
    def tableinfo_result(self, value):
        if isinstance(value, TableInfoResult):
            self._tableinfo_result = value
        else:
            self._tableinfo_result = TableInfoResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringTablelistQueryResponse, self).parse_response_content(response_content)
        if 'tableinfo_result' in response:
            self.tableinfo_result = response['tableinfo_result']
