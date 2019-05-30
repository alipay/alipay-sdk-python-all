#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpSceneTradeConsultResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpSceneTradeConsultResponse, self).__init__()
        self._decision = None
        self._order_no = None
        self._reject_reason = None

    @property
    def decision(self):
        return self._decision

    @decision.setter
    def decision(self, value):
        self._decision = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpSceneTradeConsultResponse, self).parse_response_content(response_content)
        if 'decision' in response:
            self.decision = response['decision']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
