#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderVoucherUseRuleResult import OrderVoucherUseRuleResult


class AlipayMarketingActivityOrdervoucherModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityOrdervoucherModifyResponse, self).__init__()
        self._voucher_use_rule_result = None

    @property
    def voucher_use_rule_result(self):
        return self._voucher_use_rule_result

    @voucher_use_rule_result.setter
    def voucher_use_rule_result(self, value):
        if isinstance(value, OrderVoucherUseRuleResult):
            self._voucher_use_rule_result = value
        else:
            self._voucher_use_rule_result = OrderVoucherUseRuleResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityOrdervoucherModifyResponse, self).parse_response_content(response_content)
        if 'voucher_use_rule_result' in response:
            self.voucher_use_rule_result = response['voucher_use_rule_result']
