#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerPointRefundResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerPointRefundResponse, self).__init__()
        self._refund_finished = None

    @property
    def refund_finished(self):
        return self._refund_finished

    @refund_finished.setter
    def refund_finished(self, value):
        self._refund_finished = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerPointRefundResponse, self).parse_response_content(response_content)
        if 'refund_finished' in response:
            self.refund_finished = response['refund_finished']
