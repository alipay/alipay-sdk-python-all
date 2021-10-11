#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PaymentVoucherBelongMerchantInfo import PaymentVoucherBelongMerchantInfo
from alipay.aop.api.domain.VoucherSummary import VoucherSummary
from alipay.aop.api.domain.PaymentVoucherBudgetInfo import PaymentVoucherBudgetInfo
from alipay.aop.api.domain.PaymentVoucherDisplayInfo import PaymentVoucherDisplayInfo
from alipay.aop.api.domain.PaymentVoucherSendRule import PaymentVoucherSendRule
from alipay.aop.api.domain.PaymentVoucherUseRuleDetail import PaymentVoucherUseRuleDetail


class AlipayMarketingActivityVoucherQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityVoucherQueryResponse, self).__init__()
        self._activity_id = None
        self._activity_name = None
        self._activity_status = None
        self._belong_merchant_info = None
        self._publish_end_time = None
        self._publish_start_time = None
        self._summary = None
        self._voucher_budget_info = None
        self._voucher_display_info = None
        self._voucher_send_rule = None
        self._voucher_type = None
        self._voucher_use_rule = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value
    @property
    def belong_merchant_info(self):
        return self._belong_merchant_info

    @belong_merchant_info.setter
    def belong_merchant_info(self, value):
        if isinstance(value, PaymentVoucherBelongMerchantInfo):
            self._belong_merchant_info = value
        else:
            self._belong_merchant_info = PaymentVoucherBelongMerchantInfo.from_alipay_dict(value)
    @property
    def publish_end_time(self):
        return self._publish_end_time

    @publish_end_time.setter
    def publish_end_time(self, value):
        self._publish_end_time = value
    @property
    def publish_start_time(self):
        return self._publish_start_time

    @publish_start_time.setter
    def publish_start_time(self, value):
        self._publish_start_time = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        if isinstance(value, VoucherSummary):
            self._summary = value
        else:
            self._summary = VoucherSummary.from_alipay_dict(value)
    @property
    def voucher_budget_info(self):
        return self._voucher_budget_info

    @voucher_budget_info.setter
    def voucher_budget_info(self, value):
        if isinstance(value, PaymentVoucherBudgetInfo):
            self._voucher_budget_info = value
        else:
            self._voucher_budget_info = PaymentVoucherBudgetInfo.from_alipay_dict(value)
    @property
    def voucher_display_info(self):
        return self._voucher_display_info

    @voucher_display_info.setter
    def voucher_display_info(self, value):
        if isinstance(value, PaymentVoucherDisplayInfo):
            self._voucher_display_info = value
        else:
            self._voucher_display_info = PaymentVoucherDisplayInfo.from_alipay_dict(value)
    @property
    def voucher_send_rule(self):
        return self._voucher_send_rule

    @voucher_send_rule.setter
    def voucher_send_rule(self, value):
        if isinstance(value, PaymentVoucherSendRule):
            self._voucher_send_rule = value
        else:
            self._voucher_send_rule = PaymentVoucherSendRule.from_alipay_dict(value)
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value
    @property
    def voucher_use_rule(self):
        return self._voucher_use_rule

    @voucher_use_rule.setter
    def voucher_use_rule(self, value):
        if isinstance(value, PaymentVoucherUseRuleDetail):
            self._voucher_use_rule = value
        else:
            self._voucher_use_rule = PaymentVoucherUseRuleDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityVoucherQueryResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'activity_name' in response:
            self.activity_name = response['activity_name']
        if 'activity_status' in response:
            self.activity_status = response['activity_status']
        if 'belong_merchant_info' in response:
            self.belong_merchant_info = response['belong_merchant_info']
        if 'publish_end_time' in response:
            self.publish_end_time = response['publish_end_time']
        if 'publish_start_time' in response:
            self.publish_start_time = response['publish_start_time']
        if 'summary' in response:
            self.summary = response['summary']
        if 'voucher_budget_info' in response:
            self.voucher_budget_info = response['voucher_budget_info']
        if 'voucher_display_info' in response:
            self.voucher_display_info = response['voucher_display_info']
        if 'voucher_send_rule' in response:
            self.voucher_send_rule = response['voucher_send_rule']
        if 'voucher_type' in response:
            self.voucher_type = response['voucher_type']
        if 'voucher_use_rule' in response:
            self.voucher_use_rule = response['voucher_use_rule']
