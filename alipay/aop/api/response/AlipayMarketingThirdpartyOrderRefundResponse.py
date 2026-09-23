#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ThirdPartyRefundResultList import ThirdPartyRefundResultList


class AlipayMarketingThirdpartyOrderRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingThirdpartyOrderRefundResponse, self).__init__()
        self._failed_count = None
        self._refund_result_list = None
        self._success_count = None
        self._total = None

    @property
    def failed_count(self):
        return self._failed_count

    @failed_count.setter
    def failed_count(self, value):
        self._failed_count = value
    @property
    def refund_result_list(self):
        return self._refund_result_list

    @refund_result_list.setter
    def refund_result_list(self, value):
        if isinstance(value, ThirdPartyRefundResultList):
            self._refund_result_list = value
        else:
            self._refund_result_list = ThirdPartyRefundResultList.from_alipay_dict(value)
    @property
    def success_count(self):
        return self._success_count

    @success_count.setter
    def success_count(self, value):
        self._success_count = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingThirdpartyOrderRefundResponse, self).parse_response_content(response_content)
        if 'failed_count' in response:
            self.failed_count = response['failed_count']
        if 'refund_result_list' in response:
            self.refund_result_list = response['refund_result_list']
        if 'success_count' in response:
            self.success_count = response['success_count']
        if 'total' in response:
            self.total = response['total']
