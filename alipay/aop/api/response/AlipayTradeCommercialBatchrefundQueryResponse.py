#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CommerceRefundDetail import CommerceRefundDetail


class AlipayTradeCommercialBatchrefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCommercialBatchrefundQueryResponse, self).__init__()
        self._actual_refund_amount = None
        self._batch_id = None
        self._create_time = None
        self._details = None
        self._fail_count = None
        self._refund_reason = None
        self._status = None
        self._success_count = None
        self._total_count = None
        self._total_refund_amount = None

    @property
    def actual_refund_amount(self):
        return self._actual_refund_amount

    @actual_refund_amount.setter
    def actual_refund_amount(self, value):
        self._actual_refund_amount = value
    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        if isinstance(value, list):
            self._details = list()
            for i in value:
                if isinstance(i, CommerceRefundDetail):
                    self._details.append(i)
                else:
                    self._details.append(CommerceRefundDetail.from_alipay_dict(i))
    @property
    def fail_count(self):
        return self._fail_count

    @fail_count.setter
    def fail_count(self, value):
        self._fail_count = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def success_count(self):
        return self._success_count

    @success_count.setter
    def success_count(self, value):
        self._success_count = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_refund_amount(self):
        return self._total_refund_amount

    @total_refund_amount.setter
    def total_refund_amount(self, value):
        self._total_refund_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCommercialBatchrefundQueryResponse, self).parse_response_content(response_content)
        if 'actual_refund_amount' in response:
            self.actual_refund_amount = response['actual_refund_amount']
        if 'batch_id' in response:
            self.batch_id = response['batch_id']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'details' in response:
            self.details = response['details']
        if 'fail_count' in response:
            self.fail_count = response['fail_count']
        if 'refund_reason' in response:
            self.refund_reason = response['refund_reason']
        if 'status' in response:
            self.status = response['status']
        if 'success_count' in response:
            self.success_count = response['success_count']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'total_refund_amount' in response:
            self.total_refund_amount = response['total_refund_amount']
