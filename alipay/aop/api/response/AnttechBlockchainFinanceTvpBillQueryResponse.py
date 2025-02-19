#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TrustFundOrder import TrustFundOrder


class AnttechBlockchainFinanceTvpBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceTvpBillQueryResponse, self).__init__()
        self._actual_total_amount = None
        self._adjusted_amount = None
        self._bill_detail_list = None
        self._bill_name = None
        self._bill_no = None
        self._billing_date = None
        self._desc = None
        self._end_date = None
        self._expire_time = None
        self._original_total_amount = None
        self._out_bill_no = None
        self._remark = None
        self._start_date = None
        self._status = None
        self._type = None

    @property
    def actual_total_amount(self):
        return self._actual_total_amount

    @actual_total_amount.setter
    def actual_total_amount(self, value):
        self._actual_total_amount = value
    @property
    def adjusted_amount(self):
        return self._adjusted_amount

    @adjusted_amount.setter
    def adjusted_amount(self, value):
        self._adjusted_amount = value
    @property
    def bill_detail_list(self):
        return self._bill_detail_list

    @bill_detail_list.setter
    def bill_detail_list(self, value):
        if isinstance(value, list):
            self._bill_detail_list = list()
            for i in value:
                if isinstance(i, TrustFundOrder):
                    self._bill_detail_list.append(i)
                else:
                    self._bill_detail_list.append(TrustFundOrder.from_alipay_dict(i))
    @property
    def bill_name(self):
        return self._bill_name

    @bill_name.setter
    def bill_name(self, value):
        self._bill_name = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def billing_date(self):
        return self._billing_date

    @billing_date.setter
    def billing_date(self, value):
        self._billing_date = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def original_total_amount(self):
        return self._original_total_amount

    @original_total_amount.setter
    def original_total_amount(self, value):
        self._original_total_amount = value
    @property
    def out_bill_no(self):
        return self._out_bill_no

    @out_bill_no.setter
    def out_bill_no(self, value):
        self._out_bill_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceTvpBillQueryResponse, self).parse_response_content(response_content)
        if 'actual_total_amount' in response:
            self.actual_total_amount = response['actual_total_amount']
        if 'adjusted_amount' in response:
            self.adjusted_amount = response['adjusted_amount']
        if 'bill_detail_list' in response:
            self.bill_detail_list = response['bill_detail_list']
        if 'bill_name' in response:
            self.bill_name = response['bill_name']
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'billing_date' in response:
            self.billing_date = response['billing_date']
        if 'desc' in response:
            self.desc = response['desc']
        if 'end_date' in response:
            self.end_date = response['end_date']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'original_total_amount' in response:
            self.original_total_amount = response['original_total_amount']
        if 'out_bill_no' in response:
            self.out_bill_no = response['out_bill_no']
        if 'remark' in response:
            self.remark = response['remark']
        if 'start_date' in response:
            self.start_date = response['start_date']
        if 'status' in response:
            self.status = response['status']
        if 'type' in response:
            self.type = response['type']
