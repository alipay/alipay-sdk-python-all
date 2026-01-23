#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseResourcepackageTopostpaidConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseResourcepackageTopostpaidConsultResponse, self).__init__()
        self._origin_refund_amount = None
        self._refund_amount = None

    @property
    def origin_refund_amount(self):
        return self._origin_refund_amount

    @origin_refund_amount.setter
    def origin_refund_amount(self, value):
        self._origin_refund_amount = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseResourcepackageTopostpaidConsultResponse, self).parse_response_content(response_content)
        if 'origin_refund_amount' in response:
            self.origin_refund_amount = response['origin_refund_amount']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
