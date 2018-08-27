#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RepaymentRecords import RepaymentRecords


class AlipayEcapiprodDrawndnRepaymentrecordQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcapiprodDrawndnRepaymentrecordQueryResponse, self).__init__()
        self._repayment_records = None
        self._request_id = None

    @property
    def repayment_records(self):
        return self._repayment_records

    @repayment_records.setter
    def repayment_records(self, value):
        if isinstance(value, list):
            self._repayment_records = list()
            for i in value:
                if isinstance(i, RepaymentRecords):
                    self._repayment_records.append(i)
                else:
                    self._repayment_records.append(RepaymentRecords.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcapiprodDrawndnRepaymentrecordQueryResponse, self).parse_response_content(response_content)
        if 'repayment_records' in response:
            self.repayment_records = response['repayment_records']
        if 'request_id' in response:
            self.request_id = response['request_id']
