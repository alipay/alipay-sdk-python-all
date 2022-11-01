#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduPlanInstanceInfo import EduPlanInstanceInfo


class AlipayCommerceEducateTuitioncodeFundtransferQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateTuitioncodeFundtransferQueryResponse, self).__init__()
        self._amount = None
        self._fund_transfer_no = None
        self._out_req_no = None
        self._plan_list = None
        self._transfer_status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def fund_transfer_no(self):
        return self._fund_transfer_no

    @fund_transfer_no.setter
    def fund_transfer_no(self, value):
        self._fund_transfer_no = value
    @property
    def out_req_no(self):
        return self._out_req_no

    @out_req_no.setter
    def out_req_no(self, value):
        self._out_req_no = value
    @property
    def plan_list(self):
        return self._plan_list

    @plan_list.setter
    def plan_list(self, value):
        if isinstance(value, list):
            self._plan_list = list()
            for i in value:
                if isinstance(i, EduPlanInstanceInfo):
                    self._plan_list.append(i)
                else:
                    self._plan_list.append(EduPlanInstanceInfo.from_alipay_dict(i))
    @property
    def transfer_status(self):
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, value):
        self._transfer_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateTuitioncodeFundtransferQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'fund_transfer_no' in response:
            self.fund_transfer_no = response['fund_transfer_no']
        if 'out_req_no' in response:
            self.out_req_no = response['out_req_no']
        if 'plan_list' in response:
            self.plan_list = response['plan_list']
        if 'transfer_status' in response:
            self.transfer_status = response['transfer_status']
