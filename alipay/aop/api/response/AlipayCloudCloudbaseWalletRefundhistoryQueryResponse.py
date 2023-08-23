#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RefundHistory import RefundHistory


class AlipayCloudCloudbaseWalletRefundhistoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseWalletRefundhistoryQueryResponse, self).__init__()
        self._refund_histories = None

    @property
    def refund_histories(self):
        return self._refund_histories

    @refund_histories.setter
    def refund_histories(self, value):
        if isinstance(value, list):
            self._refund_histories = list()
            for i in value:
                if isinstance(i, RefundHistory):
                    self._refund_histories.append(i)
                else:
                    self._refund_histories.append(RefundHistory.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseWalletRefundhistoryQueryResponse, self).parse_response_content(response_content)
        if 'refund_histories' in response:
            self.refund_histories = response['refund_histories']
