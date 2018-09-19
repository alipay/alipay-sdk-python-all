#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SinglePayDetail import SinglePayDetail


class AlipayMicropayOrderConfirmpayurlGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMicropayOrderConfirmpayurlGetResponse, self).__init__()
        self._single_pay_detail = None

    @property
    def single_pay_detail(self):
        return self._single_pay_detail

    @single_pay_detail.setter
    def single_pay_detail(self, value):
        if isinstance(value, SinglePayDetail):
            self._single_pay_detail = value
        else:
            self._single_pay_detail = SinglePayDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMicropayOrderConfirmpayurlGetResponse, self).parse_response_content(response_content)
        if 'single_pay_detail' in response:
            self.single_pay_detail = response['single_pay_detail']
