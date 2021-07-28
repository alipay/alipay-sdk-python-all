#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QueryRecord import QueryRecord


class AlipayBossProdAntlegalchainNotaryprocsumQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlegalchainNotaryprocsumQueryResponse, self).__init__()
        self._bas_data_id = None
        self._record_list = None

    @property
    def bas_data_id(self):
        return self._bas_data_id

    @bas_data_id.setter
    def bas_data_id(self, value):
        self._bas_data_id = value
    @property
    def record_list(self):
        return self._record_list

    @record_list.setter
    def record_list(self, value):
        if isinstance(value, list):
            self._record_list = list()
            for i in value:
                if isinstance(i, QueryRecord):
                    self._record_list.append(i)
                else:
                    self._record_list.append(QueryRecord.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlegalchainNotaryprocsumQueryResponse, self).parse_response_content(response_content)
        if 'bas_data_id' in response:
            self.bas_data_id = response['bas_data_id']
        if 'record_list' in response:
            self.record_list = response['record_list']
