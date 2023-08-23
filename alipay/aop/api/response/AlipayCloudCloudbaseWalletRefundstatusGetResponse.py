#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseWalletRefundstatusGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseWalletRefundstatusGetResponse, self).__init__()
        self._refund_status = None

    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseWalletRefundstatusGetResponse, self).parse_response_content(response_content)
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
