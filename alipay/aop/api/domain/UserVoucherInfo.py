#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityBaseInfo import ActivityBaseInfo
from alipay.aop.api.domain.UserVoucherBaseInfo import UserVoucherBaseInfo
from alipay.aop.api.domain.VoucherAvailableScopeInfo import VoucherAvailableScopeInfo
from alipay.aop.api.domain.VoucherCustomerGuideInfo import VoucherCustomerGuideInfo
from alipay.aop.api.domain.VoucherDeductInfo import VoucherDeductInfo
from alipay.aop.api.domain.CommonVoucherDisplayLiteInfo import CommonVoucherDisplayLiteInfo
from alipay.aop.api.domain.VoucherDisplayPatternInfo import VoucherDisplayPatternInfo
from alipay.aop.api.domain.VoucherSendModeInfo import VoucherSendModeInfo
from alipay.aop.api.domain.VoucherUseRuleInfo import VoucherUseRuleInfo
from alipay.aop.api.domain.CommonVoucherUseRuleLiteInfo import CommonVoucherUseRuleLiteInfo


class UserVoucherInfo(object):

    def __init__(self):
        self._activity_base_info = None
        self._activity_id = None
        self._available_begin_time = None
        self._available_end_time = None
        self._belong_merchant_id = None
        self._create_time = None
        self._user_voucher_base_info = None
        self._voucher_available_scope_info = None
        self._voucher_customer_guide_info = None
        self._voucher_deduct_info = None
        self._voucher_display_lite_info = None
        self._voucher_display_pattern_info = None
        self._voucher_id = None
        self._voucher_name = None
        self._voucher_send_mode_info = None
        self._voucher_status = None
        self._voucher_type = None
        self._voucher_use_rule_info = None
        self._voucher_use_rule_lite_info = None

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
    def voucher_display_lite_info(self):
        return self._voucher_display_lite_info

    @voucher_display_lite_info.setter
    def voucher_display_lite_info(self, value):
        if isinstance(value, CommonVoucherDisplayLiteInfo):
            self._voucher_display_lite_info = value
        else:
            self._voucher_display_lite_info = CommonVoucherDisplayLiteInfo.from_alipay_dict(value)
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
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
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
    def voucher_use_rule_info(self):
        return self._voucher_use_rule_info

    @voucher_use_rule_info.setter
    def voucher_use_rule_info(self, value):
        if isinstance(value, VoucherUseRuleInfo):
            self._voucher_use_rule_info = value
        else:
            self._voucher_use_rule_info = VoucherUseRuleInfo.from_alipay_dict(value)
    @property
    def voucher_use_rule_lite_info(self):
        return self._voucher_use_rule_lite_info

    @voucher_use_rule_lite_info.setter
    def voucher_use_rule_lite_info(self, value):
        if isinstance(value, CommonVoucherUseRuleLiteInfo):
            self._voucher_use_rule_lite_info = value
        else:
            self._voucher_use_rule_lite_info = CommonVoucherUseRuleLiteInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_base_info:
            if hasattr(self.activity_base_info, 'to_alipay_dict'):
                params['activity_base_info'] = self.activity_base_info.to_alipay_dict()
            else:
                params['activity_base_info'] = self.activity_base_info
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.available_begin_time:
            if hasattr(self.available_begin_time, 'to_alipay_dict'):
                params['available_begin_time'] = self.available_begin_time.to_alipay_dict()
            else:
                params['available_begin_time'] = self.available_begin_time
        if self.available_end_time:
            if hasattr(self.available_end_time, 'to_alipay_dict'):
                params['available_end_time'] = self.available_end_time.to_alipay_dict()
            else:
                params['available_end_time'] = self.available_end_time
        if self.belong_merchant_id:
            if hasattr(self.belong_merchant_id, 'to_alipay_dict'):
                params['belong_merchant_id'] = self.belong_merchant_id.to_alipay_dict()
            else:
                params['belong_merchant_id'] = self.belong_merchant_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.user_voucher_base_info:
            if hasattr(self.user_voucher_base_info, 'to_alipay_dict'):
                params['user_voucher_base_info'] = self.user_voucher_base_info.to_alipay_dict()
            else:
                params['user_voucher_base_info'] = self.user_voucher_base_info
        if self.voucher_available_scope_info:
            if hasattr(self.voucher_available_scope_info, 'to_alipay_dict'):
                params['voucher_available_scope_info'] = self.voucher_available_scope_info.to_alipay_dict()
            else:
                params['voucher_available_scope_info'] = self.voucher_available_scope_info
        if self.voucher_customer_guide_info:
            if hasattr(self.voucher_customer_guide_info, 'to_alipay_dict'):
                params['voucher_customer_guide_info'] = self.voucher_customer_guide_info.to_alipay_dict()
            else:
                params['voucher_customer_guide_info'] = self.voucher_customer_guide_info
        if self.voucher_deduct_info:
            if hasattr(self.voucher_deduct_info, 'to_alipay_dict'):
                params['voucher_deduct_info'] = self.voucher_deduct_info.to_alipay_dict()
            else:
                params['voucher_deduct_info'] = self.voucher_deduct_info
        if self.voucher_display_lite_info:
            if hasattr(self.voucher_display_lite_info, 'to_alipay_dict'):
                params['voucher_display_lite_info'] = self.voucher_display_lite_info.to_alipay_dict()
            else:
                params['voucher_display_lite_info'] = self.voucher_display_lite_info
        if self.voucher_display_pattern_info:
            if hasattr(self.voucher_display_pattern_info, 'to_alipay_dict'):
                params['voucher_display_pattern_info'] = self.voucher_display_pattern_info.to_alipay_dict()
            else:
                params['voucher_display_pattern_info'] = self.voucher_display_pattern_info
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_send_mode_info:
            if hasattr(self.voucher_send_mode_info, 'to_alipay_dict'):
                params['voucher_send_mode_info'] = self.voucher_send_mode_info.to_alipay_dict()
            else:
                params['voucher_send_mode_info'] = self.voucher_send_mode_info
        if self.voucher_status:
            if hasattr(self.voucher_status, 'to_alipay_dict'):
                params['voucher_status'] = self.voucher_status.to_alipay_dict()
            else:
                params['voucher_status'] = self.voucher_status
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        if self.voucher_use_rule_info:
            if hasattr(self.voucher_use_rule_info, 'to_alipay_dict'):
                params['voucher_use_rule_info'] = self.voucher_use_rule_info.to_alipay_dict()
            else:
                params['voucher_use_rule_info'] = self.voucher_use_rule_info
        if self.voucher_use_rule_lite_info:
            if hasattr(self.voucher_use_rule_lite_info, 'to_alipay_dict'):
                params['voucher_use_rule_lite_info'] = self.voucher_use_rule_lite_info.to_alipay_dict()
            else:
                params['voucher_use_rule_lite_info'] = self.voucher_use_rule_lite_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserVoucherInfo()
        if 'activity_base_info' in d:
            o.activity_base_info = d['activity_base_info']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'available_begin_time' in d:
            o.available_begin_time = d['available_begin_time']
        if 'available_end_time' in d:
            o.available_end_time = d['available_end_time']
        if 'belong_merchant_id' in d:
            o.belong_merchant_id = d['belong_merchant_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'user_voucher_base_info' in d:
            o.user_voucher_base_info = d['user_voucher_base_info']
        if 'voucher_available_scope_info' in d:
            o.voucher_available_scope_info = d['voucher_available_scope_info']
        if 'voucher_customer_guide_info' in d:
            o.voucher_customer_guide_info = d['voucher_customer_guide_info']
        if 'voucher_deduct_info' in d:
            o.voucher_deduct_info = d['voucher_deduct_info']
        if 'voucher_display_lite_info' in d:
            o.voucher_display_lite_info = d['voucher_display_lite_info']
        if 'voucher_display_pattern_info' in d:
            o.voucher_display_pattern_info = d['voucher_display_pattern_info']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_send_mode_info' in d:
            o.voucher_send_mode_info = d['voucher_send_mode_info']
        if 'voucher_status' in d:
            o.voucher_status = d['voucher_status']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        if 'voucher_use_rule_info' in d:
            o.voucher_use_rule_info = d['voucher_use_rule_info']
        if 'voucher_use_rule_lite_info' in d:
            o.voucher_use_rule_lite_info = d['voucher_use_rule_lite_info']
        return o


