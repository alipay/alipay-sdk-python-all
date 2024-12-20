#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IsvBizOpenOrderFailReason import IsvBizOpenOrderFailReason


class AntMerchantExpandBizaccessOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandBizaccessOrderCreateResponse, self).__init__()
        self._fail_reasons = None
        self._merchant_pid = None
        self._order_id = None

    @property
    def fail_reasons(self):
        return self._fail_reasons

    @fail_reasons.setter
    def fail_reasons(self, value):
        if isinstance(value, list):
            self._fail_reasons = list()
            for i in value:
                if isinstance(i, IsvBizOpenOrderFailReason):
                    self._fail_reasons.append(i)
                else:
                    self._fail_reasons.append(IsvBizOpenOrderFailReason.from_alipay_dict(i))
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandBizaccessOrderCreateResponse, self).parse_response_content(response_content)
        if 'fail_reasons' in response:
            self.fail_reasons = response['fail_reasons']
        if 'merchant_pid' in response:
            self.merchant_pid = response['merchant_pid']
        if 'order_id' in response:
            self.order_id = response['order_id']
