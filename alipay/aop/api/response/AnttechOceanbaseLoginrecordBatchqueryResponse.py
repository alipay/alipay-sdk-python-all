#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LoginRecordDTO import LoginRecordDTO


class AnttechOceanbaseLoginrecordBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseLoginrecordBatchqueryResponse, self).__init__()
        self._login_records = None

    @property
    def login_records(self):
        return self._login_records

    @login_records.setter
    def login_records(self, value):
        if isinstance(value, list):
            self._login_records = list()
            for i in value:
                if isinstance(i, LoginRecordDTO):
                    self._login_records.append(i)
                else:
                    self._login_records.append(LoginRecordDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseLoginrecordBatchqueryResponse, self).parse_response_content(response_content)
        if 'login_records' in response:
            self.login_records = response['login_records']
