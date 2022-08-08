#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityBaseInfo import ActivityBaseInfo
from alipay.aop.api.domain.BelongMerchantInfo import BelongMerchantInfo
from alipay.aop.api.domain.CustomerGuide import CustomerGuide
from alipay.aop.api.domain.VoucherSummary import VoucherSummary
from alipay.aop.api.domain.VoucherAvailableScopeInfo import VoucherAvailableScopeInfo
from alipay.aop.api.domain.VoucherCustomerGuideInfo import VoucherCustomerGuideInfo
from alipay.aop.api.domain.VoucherDeductInfo import VoucherDeductInfo
from alipay.aop.api.domain.VoucherDisplayInfo import VoucherDisplayInfo
from alipay.aop.api.domain.VoucherDisplayPatternInfo import VoucherDisplayPatternInfo
from alipay.aop.api.domain.VoucherInventoryInfo import VoucherInventoryInfo
from alipay.aop.api.domain.VoucherSendModeInfo import VoucherSendModeInfo
from alipay.aop.api.domain.VoucherSendRuleDetail import VoucherSendRuleDetail
from alipay.aop.api.domain.VoucherUseRule import VoucherUseRule
from alipay.aop.api.domain.VoucherUseRuleInfo import VoucherUseRuleInfo


class AlipayMarketingActivityOrdervoucherQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityOrdervoucherQueryResponse, self).__init__()
        self._activity_base_info = None
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
        self._voucher_available_scope_info = None
        self._voucher_customer_guide_info = None
        self._voucher_deduct_info = None
        self._voucher_display_info = None
        self._voucher_display_pattern_info = None
        self._voucher_inventory_info = None
        self._voucher_send_mode_info = None
        self._voucher_send_rule = None
        self._voucher_type = None
        self._voucher_use_rule = None
        self._voucher_use_rule_info = None

    @property
    def activity_base_info(self):
        return self._activity_base_info

    @activity_base_info.setter
    def activity_base_info(self, value):
        if isinstance(value, ActivityBaseInfo):
            self._activity_base_info = value
        else:
            self._activity_base_info = ActivityBaseInfo.from_alipay_dict(value)
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
    def voucher_available_scope_info(self):
        return self._voucher_available_scope_info

    @voucher_available_scope_info.setter
    def voucher_available_scope_info(self, value):
        if isinstance(value, VoucherAvailableScopeInfo):
            self._voucher_available_scope_info = value
        else:
            self._voucher_available_scope_info = VoucherAvailableScopeInfo.from_alipay_dict(value)
    @property
    def voucher_customer_guide_info(self):
        return self._voucher_customer_guide_info

    @voucher_customer_guide_info.setter
    def voucher_customer_guide_info(self, value):
        if isinstance(value, VoucherCustomerGuideInfo):
            self._voucher_customer_guide_info = value
        else:
            self._voucher_customer_guide_info = VoucherCustomerGuideInfo.from_alipay_dict(value)
    @property
    def voucher_deduct_info(self):
        return self._voucher_deduct_info

    @voucher_deduct_info.setter
    def voucher_deduct_info(self, value):
        if isinstance(value, VoucherDeductInfo):
            self._voucher_deduct_info = value
        else:
            self._voucher_deduct_info = VoucherDeductInfo.from_alipay_dict(value)
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
    def voucher_display_pattern_info(self):
        return self._voucher_display_pattern_info

    @voucher_display_pattern_info.setter
    def voucher_display_pattern_info(self, value):
        if isinstance(value, VoucherDisplayPatternInfo):
            self._voucher_display_pattern_info = value
        else:
            self._voucher_display_pattern_info = VoucherDisplayPatternInfo.from_alipay_dict(value)
    @property
    def voucher_inventory_info(self):
        return self._voucher_inventory_info

    @voucher_inventory_info.setter
    def voucher_inventory_info(self, value):
        if isinstance(value, VoucherInventoryInfo):
            self._voucher_inventory_info = value
        else:
            self._voucher_inventory_info = VoucherInventoryInfo.from_alipay_dict(value)
    @property
    def voucher_send_mode_info(self):
        return self._voucher_send_mode_info

    @voucher_send_mode_info.setter
    def voucher_send_mode_info(self, value):
        if isinstance(value, VoucherSendModeInfo):
            self._voucher_send_mode_info = value
        else:
            self._voucher_send_mode_info = VoucherSendModeInfo.from_alipay_dict(value)
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
    @property
    def voucher_use_rule_info(self):
        return self._voucher_use_rule_info

    @voucher_use_rule_info.setter
    def voucher_use_rule_info(self, value):
        if isinstance(value, VoucherUseRuleInfo):
            self._voucher_use_rule_info = value
        else:
            self._voucher_use_rule_info = VoucherUseRuleInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityOrdervoucherQueryResponse, self).parse_response_content(response_content)
        if 'activity_base_info' in response:
            self.activity_base_info = response['activity_base_info']
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
        if 'voucher_available_scope_info' in response:
            self.voucher_available_scope_info = response['voucher_available_scope_info']
        if 'voucher_customer_guide_info' in response:
            self.voucher_customer_guide_info = response['voucher_customer_guide_info']
        if 'voucher_deduct_info' in response:
            self.voucher_deduct_info = response['voucher_deduct_info']
        if 'voucher_display_info' in response:
            self.voucher_display_info = response['voucher_display_info']
        if 'voucher_display_pattern_info' in response:
            self.voucher_display_pattern_info = response['voucher_display_pattern_info']
        if 'voucher_inventory_info' in response:
            self.voucher_inventory_info = response['voucher_inventory_info']
        if 'voucher_send_mode_info' in response:
            self.voucher_send_mode_info = response['voucher_send_mode_info']
        if 'voucher_send_rule' in response:
            self.voucher_send_rule = response['voucher_send_rule']
        if 'voucher_type' in response:
            self.voucher_type = response['voucher_type']
        if 'voucher_use_rule' in response:
            self.voucher_use_rule = response['voucher_use_rule']
        if 'voucher_use_rule_info' in response:
            self.voucher_use_rule_info = response['voucher_use_rule_info']
