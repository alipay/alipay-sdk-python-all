#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndrPoboAuthRecordDTO import IndrPoboAuthRecordDTO
from alipay.aop.api.domain.IndrPoboDebitRecordDTO import IndrPoboDebitRecordDTO
from alipay.aop.api.domain.IndrISVResult import IndrISVResult


class AlipayOverseasOpenPoboQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasOpenPoboQueryResponse, self).__init__()
        self._auth_records = None
        self._latest_debit_record = None
        self._payment_type = None
        self._result = None

    @property
    def auth_records(self):
        return self._auth_records

    @auth_records.setter
    def auth_records(self, value):
        if isinstance(value, list):
            self._auth_records = list()
            for i in value:
                if isinstance(i, IndrPoboAuthRecordDTO):
                    self._auth_records.append(i)
                else:
                    self._auth_records.append(IndrPoboAuthRecordDTO.from_alipay_dict(i))
    @property
    def latest_debit_record(self):
        return self._latest_debit_record

    @latest_debit_record.setter
    def latest_debit_record(self, value):
        if isinstance(value, IndrPoboDebitRecordDTO):
            self._latest_debit_record = value
        else:
            self._latest_debit_record = IndrPoboDebitRecordDTO.from_alipay_dict(value)
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, IndrISVResult):
            self._result = value
        else:
            self._result = IndrISVResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasOpenPoboQueryResponse, self).parse_response_content(response_content)
        if 'auth_records' in response:
            self.auth_records = response['auth_records']
        if 'latest_debit_record' in response:
            self.latest_debit_record = response['latest_debit_record']
        if 'payment_type' in response:
            self.payment_type = response['payment_type']
        if 'result' in response:
            self.result = response['result']
