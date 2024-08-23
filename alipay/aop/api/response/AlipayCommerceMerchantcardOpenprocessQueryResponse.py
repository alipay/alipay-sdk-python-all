#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantSettleInInfo import MerchantSettleInInfo


class AlipayCommerceMerchantcardOpenprocessQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardOpenprocessQueryResponse, self).__init__()
        self._fail_reason = None
        self._merchant_settle_in_info = None
        self._query_result = None

    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def merchant_settle_in_info(self):
        return self._merchant_settle_in_info

    @merchant_settle_in_info.setter
    def merchant_settle_in_info(self, value):
        if isinstance(value, MerchantSettleInInfo):
            self._merchant_settle_in_info = value
        else:
            self._merchant_settle_in_info = MerchantSettleInInfo.from_alipay_dict(value)
    @property
    def query_result(self):
        return self._query_result

    @query_result.setter
    def query_result(self, value):
        self._query_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardOpenprocessQueryResponse, self).parse_response_content(response_content)
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'merchant_settle_in_info' in response:
            self.merchant_settle_in_info = response['merchant_settle_in_info']
        if 'query_result' in response:
            self.query_result = response['query_result']
