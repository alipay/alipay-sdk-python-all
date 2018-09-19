#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PaymentSchedule import PaymentSchedule


class AlipayEcapiprodDrawndnPaymentscheduleGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcapiprodDrawndnPaymentscheduleGetResponse, self).__init__()
        self._payment_schedules = None
        self._request_id = None

    @property
    def payment_schedules(self):
        return self._payment_schedules

    @payment_schedules.setter
    def payment_schedules(self, value):
        if isinstance(value, list):
            self._payment_schedules = list()
            for i in value:
                if isinstance(i, PaymentSchedule):
                    self._payment_schedules.append(i)
                else:
                    self._payment_schedules.append(PaymentSchedule.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcapiprodDrawndnPaymentscheduleGetResponse, self).parse_response_content(response_content)
        if 'payment_schedules' in response:
            self.payment_schedules = response['payment_schedules']
        if 'request_id' in response:
            self.request_id = response['request_id']
