#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubscriptionPaymentDetail import SubscriptionPaymentDetail


class AlipayTradeSubscriptionPaymentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSubscriptionPaymentQueryResponse, self).__init__()
        self._end_time = None
        self._page_no = None
        self._page_size = None
        self._payment_details = None
        self._start_time = None
        self._subscription_id = None
        self._total_count = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def payment_details(self):
        return self._payment_details

    @payment_details.setter
    def payment_details(self, value):
        if isinstance(value, list):
            self._payment_details = list()
            for i in value:
                if isinstance(i, SubscriptionPaymentDetail):
                    self._payment_details.append(i)
                else:
                    self._payment_details.append(SubscriptionPaymentDetail.from_alipay_dict(i))
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def subscription_id(self):
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self._subscription_id = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSubscriptionPaymentQueryResponse, self).parse_response_content(response_content)
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'payment_details' in response:
            self.payment_details = response['payment_details']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'subscription_id' in response:
            self.subscription_id = response['subscription_id']
        if 'total_count' in response:
            self.total_count = response['total_count']
