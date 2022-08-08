#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityBaseInfo import ActivityBaseInfo
from alipay.aop.api.domain.VoucherAvailableScopeInfo import VoucherAvailableScopeInfo
from alipay.aop.api.domain.VoucherDeductInfo import VoucherDeductInfo
from alipay.aop.api.domain.VoucherDisplayPatternInfo import VoucherDisplayPatternInfo
from alipay.aop.api.domain.VoucherSendModeInfo import VoucherSendModeInfo
from alipay.aop.api.domain.VoucherUseRuleInfo import VoucherUseRuleInfo


class VoucherPackageActivityInfo(object):

    def __init__(self):
        self._activity_base_info = None
        self._voucher_available_scope_info = None
        self._voucher_deduct_info = None
        self._voucher_display_pattern_info = None
        self._voucher_send_mode_info = None
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
    def voucher_available_scope_info(self):
        return self._voucher_available_scope_info

    @voucher_available_scope_info.setter
    def voucher_available_scope_info(self, value):
        if isinstance(value, VoucherAvailableScopeInfo):
            self._voucher_available_scope_info = value
        else:
            self._voucher_available_scope_info = VoucherAvailableScopeInfo.from_alipay_dict(value)
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
    def voucher_display_pattern_info(self):
        return self._voucher_display_pattern_info

    @voucher_display_pattern_info.setter
    def voucher_display_pattern_info(self, value):
        if isinstance(value, VoucherDisplayPatternInfo):
            self._voucher_display_pattern_info = value
        else:
            self._voucher_display_pattern_info = VoucherDisplayPatternInfo.from_alipay_dict(value)
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
    def voucher_use_rule_info(self):
        return self._voucher_use_rule_info

    @voucher_use_rule_info.setter
    def voucher_use_rule_info(self, value):
        if isinstance(value, VoucherUseRuleInfo):
            self._voucher_use_rule_info = value
        else:
            self._voucher_use_rule_info = VoucherUseRuleInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_base_info:
            if hasattr(self.activity_base_info, 'to_alipay_dict'):
                params['activity_base_info'] = self.activity_base_info.to_alipay_dict()
            else:
                params['activity_base_info'] = self.activity_base_info
        if self.voucher_available_scope_info:
            if hasattr(self.voucher_available_scope_info, 'to_alipay_dict'):
                params['voucher_available_scope_info'] = self.voucher_available_scope_info.to_alipay_dict()
            else:
                params['voucher_available_scope_info'] = self.voucher_available_scope_info
        if self.voucher_deduct_info:
            if hasattr(self.voucher_deduct_info, 'to_alipay_dict'):
                params['voucher_deduct_info'] = self.voucher_deduct_info.to_alipay_dict()
            else:
                params['voucher_deduct_info'] = self.voucher_deduct_info
        if self.voucher_display_pattern_info:
            if hasattr(self.voucher_display_pattern_info, 'to_alipay_dict'):
                params['voucher_display_pattern_info'] = self.voucher_display_pattern_info.to_alipay_dict()
            else:
                params['voucher_display_pattern_info'] = self.voucher_display_pattern_info
        if self.voucher_send_mode_info:
            if hasattr(self.voucher_send_mode_info, 'to_alipay_dict'):
                params['voucher_send_mode_info'] = self.voucher_send_mode_info.to_alipay_dict()
            else:
                params['voucher_send_mode_info'] = self.voucher_send_mode_info
        if self.voucher_use_rule_info:
            if hasattr(self.voucher_use_rule_info, 'to_alipay_dict'):
                params['voucher_use_rule_info'] = self.voucher_use_rule_info.to_alipay_dict()
            else:
                params['voucher_use_rule_info'] = self.voucher_use_rule_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherPackageActivityInfo()
        if 'activity_base_info' in d:
            o.activity_base_info = d['activity_base_info']
        if 'voucher_available_scope_info' in d:
            o.voucher_available_scope_info = d['voucher_available_scope_info']
        if 'voucher_deduct_info' in d:
            o.voucher_deduct_info = d['voucher_deduct_info']
        if 'voucher_display_pattern_info' in d:
            o.voucher_display_pattern_info = d['voucher_display_pattern_info']
        if 'voucher_send_mode_info' in d:
            o.voucher_send_mode_info = d['voucher_send_mode_info']
        if 'voucher_use_rule_info' in d:
            o.voucher_use_rule_info = d['voucher_use_rule_info']
        return o


