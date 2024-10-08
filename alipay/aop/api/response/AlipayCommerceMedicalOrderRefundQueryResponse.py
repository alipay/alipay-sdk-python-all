#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RefundOrderDetailVO import RefundOrderDetailVO


class AlipayCommerceMedicalOrderRefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalOrderRefundQueryResponse, self).__init__()
        self._refund_list = None

    @property
    def refund_list(self):
        return self._refund_list

    @refund_list.setter
    def refund_list(self, value):
        if isinstance(value, list):
            self._refund_list = list()
            for i in value:
                if isinstance(i, RefundOrderDetailVO):
                    self._refund_list.append(i)
                else:
                    self._refund_list.append(RefundOrderDetailVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalOrderRefundQueryResponse, self).parse_response_content(response_content)
        if 'refund_list' in response:
            self.refund_list = response['refund_list']
