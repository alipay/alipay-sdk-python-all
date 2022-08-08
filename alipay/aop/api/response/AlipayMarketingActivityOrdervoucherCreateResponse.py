#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherAvailableScopeResultInfo import VoucherAvailableScopeResultInfo
from alipay.aop.api.domain.OrderVoucherUseRuleResult import OrderVoucherUseRuleResult


class AlipayMarketingActivityOrdervoucherCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityOrdervoucherCreateResponse, self).__init__()
        self._activity_id = None
        self._voucher_available_scope_result_info = None
        self._voucher_use_rule_result = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def voucher_available_scope_result_info(self):
        return self._voucher_available_scope_result_info

    @voucher_available_scope_result_info.setter
    def voucher_available_scope_result_info(self, value):
        if isinstance(value, VoucherAvailableScopeResultInfo):
            self._voucher_available_scope_result_info = value
        else:
            self._voucher_available_scope_result_info = VoucherAvailableScopeResultInfo.from_alipay_dict(value)
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
        response = super(AlipayMarketingActivityOrdervoucherCreateResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'voucher_available_scope_result_info' in response:
            self.voucher_available_scope_result_info = response['voucher_available_scope_result_info']
        if 'voucher_use_rule_result' in response:
            self.voucher_use_rule_result = response['voucher_use_rule_result']
