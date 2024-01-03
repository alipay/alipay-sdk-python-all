#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityBaseInfo import ActivityBaseInfo
from alipay.aop.api.domain.UserVoucherBaseInfo import UserVoucherBaseInfo
from alipay.aop.api.domain.VoucherCustomerGuideInfo import VoucherCustomerGuideInfo
from alipay.aop.api.domain.VoucherDeductInfo import VoucherDeductInfo
from alipay.aop.api.domain.CommonVoucherDisplayInfo import CommonVoucherDisplayInfo
from alipay.aop.api.domain.VoucherDisplayPatternInfo import VoucherDisplayPatternInfo
from alipay.aop.api.domain.VoucherSendModeInfo import VoucherSendModeInfo
from alipay.aop.api.domain.CommonVoucherSendRule import CommonVoucherSendRule
from alipay.aop.api.domain.CommonVoucherUseRule import CommonVoucherUseRule
from alipay.aop.api.domain.VoucherUseRuleInfo import VoucherUseRuleInfo


class AlipayMarketingActivityUserQueryvoucherResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityUserQueryvoucherResponse, self).__init__()
        self._activity_base_info = None
        self._activity_id = None
        self._associate_trade_no = None
        self._available_begin_time = None
        self._available_end_time = None
        self._belong_merchant_id = None
        self._create_time = None
        self._user_voucher_base_info = None
        self._voucher_customer_guide_info = None
        self._voucher_deduct_info = None
        self._voucher_display_info = None
        self._voucher_display_pattern_info = None
        self._voucher_name = None
        self._voucher_send_mode_info = None
        self._voucher_send_rule = None
        self._voucher_status = None
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
    def associate_trade_no(self):
        return self._associate_trade_no

    @associate_trade_no.setter
    def associate_trade_no(self, value):
        self._associate_trade_no = value
    @property
    def available_begin_time(self):
        return self._available_begin_time

    @available_begin_time.setter
    def available_begin_time(self, value):
        self._available_begin_time = value
    @property
    def available_end_time(self):
        return self._available_end_time

    @available_end_time.setter
    def available_end_time(self, value):
        self._available_end_time = value
    @property
    def belong_merchant_id(self):
        return self._belong_merchant_id

    @belong_merchant_id.setter
    def belong_merchant_id(self, value):
        self._belong_merchant_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def user_voucher_base_info(self):
        return self._user_voucher_base_info

    @user_voucher_base_info.setter
    def user_voucher_base_info(self, value):
        if isinstance(value, UserVoucherBaseInfo):
            self._user_voucher_base_info = value
        else:
            self._user_voucher_base_info = UserVoucherBaseInfo.from_alipay_dict(value)
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
        if isinstance(value, CommonVoucherDisplayInfo):
            self._voucher_display_info = value
        else:
            self._voucher_display_info = CommonVoucherDisplayInfo.from_alipay_dict(value)
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
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
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
        if isinstance(value, CommonVoucherSendRule):
            self._voucher_send_rule = value
        else:
            self._voucher_send_rule = CommonVoucherSendRule.from_alipay_dict(value)
    @property
    def voucher_status(self):
        return self._voucher_status

    @voucher_status.setter
    def voucher_status(self, value):
        self._voucher_status = value
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
        if isinstance(value, CommonVoucherUseRule):
            self._voucher_use_rule = value
        else:
            self._voucher_use_rule = CommonVoucherUseRule.from_alipay_dict(value)
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
        response = super(AlipayMarketingActivityUserQueryvoucherResponse, self).parse_response_content(response_content)
        if 'activity_base_info' in response:
            self.activity_base_info = response['activity_base_info']
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'associate_trade_no' in response:
            self.associate_trade_no = response['associate_trade_no']
        if 'available_begin_time' in response:
            self.available_begin_time = response['available_begin_time']
        if 'available_end_time' in response:
            self.available_end_time = response['available_end_time']
        if 'belong_merchant_id' in response:
            self.belong_merchant_id = response['belong_merchant_id']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'user_voucher_base_info' in response:
            self.user_voucher_base_info = response['user_voucher_base_info']
        if 'voucher_customer_guide_info' in response:
            self.voucher_customer_guide_info = response['voucher_customer_guide_info']
        if 'voucher_deduct_info' in response:
            self.voucher_deduct_info = response['voucher_deduct_info']
        if 'voucher_display_info' in response:
            self.voucher_display_info = response['voucher_display_info']
        if 'voucher_display_pattern_info' in response:
            self.voucher_display_pattern_info = response['voucher_display_pattern_info']
        if 'voucher_name' in response:
            self.voucher_name = response['voucher_name']
        if 'voucher_send_mode_info' in response:
            self.voucher_send_mode_info = response['voucher_send_mode_info']
        if 'voucher_send_rule' in response:
            self.voucher_send_rule = response['voucher_send_rule']
        if 'voucher_status' in response:
            self.voucher_status = response['voucher_status']
        if 'voucher_type' in response:
            self.voucher_type = response['voucher_type']
        if 'voucher_use_rule' in response:
            self.voucher_use_rule = response['voucher_use_rule']
        if 'voucher_use_rule_info' in response:
            self.voucher_use_rule_info = response['voucher_use_rule_info']
