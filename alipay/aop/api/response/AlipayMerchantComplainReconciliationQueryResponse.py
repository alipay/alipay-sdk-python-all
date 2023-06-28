#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantComplainReconciliationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantComplainReconciliationQueryResponse, self).__init__()
        self._notice = None
        self._status = None

    @property
    def notice(self):
        return self._notice

    @notice.setter
    def notice(self, value):
        self._notice = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantComplainReconciliationQueryResponse, self).parse_response_content(response_content)
        if 'notice' in response:
            self.notice = response['notice']
        if 'status' in response:
            self.status = response['status']
