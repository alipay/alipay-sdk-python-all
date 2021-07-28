#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BelongMerchantInfo import BelongMerchantInfo
from alipay.aop.api.domain.CustomerGuide import CustomerGuide
from alipay.aop.api.domain.VoucherSummary import VoucherSummary
from alipay.aop.api.domain.VoucherDisplayInfo import VoucherDisplayInfo
from alipay.aop.api.domain.VoucherSendRuleDetail import VoucherSendRuleDetail
from alipay.aop.api.domain.VoucherUseRule import VoucherUseRule


class AlipayMarketingActivityOrdervoucherQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityOrdervoucherQueryResponse, self).__init__()
        self._activity_id = None
        self._activity_name = None
        self._activity_operation_status = None
        self._activity_status = None
        self._belong_merchant_info = None
        self._biz_tag = None
        self._customer_guide = None
        self._publish_end_time = None
        self._publish_start_time = None
        self._summary = None
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
    def activity_operation_status(self):
        return self._activity_operation_status

    @activity_operation_status.setter
    def activity_operation_status(self, value):
        self._activity_operation_status = value
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
        if isinstance(value, BelongMerchantInfo):
            self._belong_merchant_info = value
        else:
            self._belong_merchant_info = BelongMerchantInfo.from_alipay_dict(value)
    @property
    def biz_tag(self):
        return self._biz_tag

    @biz_tag.setter
    def biz_tag(self, value):
        self._biz_tag = value
    @property
    def customer_guide(self):
        return self._customer_guide

    @customer_guide.setter
    def customer_guide(self, value):
        if isinstance(value, CustomerGuide):
            self._customer_guide = value
        else:
            self._customer_guide = CustomerGuide.from_alipay_dict(value)
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
    def voucher_display_info(self):
        return self._voucher_display_info

    @voucher_display_info.setter
    def voucher_display_info(self, value):
        if isinstance(value, VoucherDisplayInfo):
            self._voucher_display_info = value
        else:
            self._voucher_display_info = VoucherDisplayInfo.from_alipay_dict(value)
    @property
    def voucher_send_rule(self):
        return self._voucher_send_rule

    @voucher_send_rule.setter
    def voucher_send_rule(self, value):
        if isinstance(value, VoucherSendRuleDetail):
            self._voucher_send_rule = value
        else:
            self._voucher_send_rule = VoucherSendRuleDetail.from_alipay_dict(value)
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
        if isinstance(value, VoucherUseRule):
            self._voucher_use_rule = value
        else:
            self._voucher_use_rule = VoucherUseRule.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityOrdervoucherQueryResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'activity_name' in response:
            self.activity_name = response['activity_name']
        if 'activity_operation_status' in response:
            self.activity_operation_status = response['activity_operation_status']
        if 'activity_status' in response:
            self.activity_status = response['activity_status']
        if 'belong_merchant_info' in response:
            self.belong_merchant_info = response['belong_merchant_info']
        if 'biz_tag' in response:
            self.biz_tag = response['biz_tag']
        if 'customer_guide' in response:
            self.customer_guide = response['customer_guide']
        if 'publish_end_time' in response:
            self.publish_end_time = response['publish_end_time']
        if 'publish_start_time' in response:
            self.publish_start_time = response['publish_start_time']
        if 'summary' in response:
            self.summary = response['summary']
        if 'voucher_display_info' in response:
            self.voucher_display_info = response['voucher_display_info']
        if 'voucher_send_rule' in response:
            self.voucher_send_rule = response['voucher_send_rule']
        if 'voucher_type' in response:
            self.voucher_type = response['voucher_type']
        if 'voucher_use_rule' in response:
            self.voucher_use_rule = response['voucher_use_rule']
