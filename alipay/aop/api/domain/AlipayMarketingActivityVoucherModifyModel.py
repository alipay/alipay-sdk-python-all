#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityBaseInfo import ActivityBaseInfo
from alipay.aop.api.domain.VoucherAvailableScopeInfo import VoucherAvailableScopeInfo
from alipay.aop.api.domain.VoucherSendModeInfo import VoucherSendModeInfo
from alipay.aop.api.domain.PaymentVoucherUseRuleModify import PaymentVoucherUseRuleModify
from alipay.aop.api.domain.VoucherUseRuleInfo import VoucherUseRuleInfo


class AlipayMarketingActivityVoucherModifyModel(object):

    def __init__(self):
        self._activity_base_info = None
        self._activity_id = None
        self._merchant_access_mode = None
        self._out_biz_no = None
        self._publish_end_time = None
        self._voucher_available_scope_info = None
        self._voucher_send_mode_info = None
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
    def merchant_access_mode(self):
        return self._merchant_access_mode

    @merchant_access_mode.setter
    def merchant_access_mode(self, value):
        self._merchant_access_mode = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def publish_end_time(self):
        return self._publish_end_time

    @publish_end_time.setter
    def publish_end_time(self, value):
        self._publish_end_time = value
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
    def voucher_send_mode_info(self):
        return self._voucher_send_mode_info

    @voucher_send_mode_info.setter
    def voucher_send_mode_info(self, value):
        if isinstance(value, VoucherSendModeInfo):
            self._voucher_send_mode_info = value
        else:
            self._voucher_send_mode_info = VoucherSendModeInfo.from_alipay_dict(value)
    @property
    def voucher_use_rule(self):
        return self._voucher_use_rule

    @voucher_use_rule.setter
    def voucher_use_rule(self, value):
        if isinstance(value, PaymentVoucherUseRuleModify):
            self._voucher_use_rule = value
        else:
            self._voucher_use_rule = PaymentVoucherUseRuleModify.from_alipay_dict(value)
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
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.merchant_access_mode:
            if hasattr(self.merchant_access_mode, 'to_alipay_dict'):
                params['merchant_access_mode'] = self.merchant_access_mode.to_alipay_dict()
            else:
                params['merchant_access_mode'] = self.merchant_access_mode
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.publish_end_time:
            if hasattr(self.publish_end_time, 'to_alipay_dict'):
                params['publish_end_time'] = self.publish_end_time.to_alipay_dict()
            else:
                params['publish_end_time'] = self.publish_end_time
        if self.voucher_available_scope_info:
            if hasattr(self.voucher_available_scope_info, 'to_alipay_dict'):
                params['voucher_available_scope_info'] = self.voucher_available_scope_info.to_alipay_dict()
            else:
                params['voucher_available_scope_info'] = self.voucher_available_scope_info
        if self.voucher_send_mode_info:
            if hasattr(self.voucher_send_mode_info, 'to_alipay_dict'):
                params['voucher_send_mode_info'] = self.voucher_send_mode_info.to_alipay_dict()
            else:
                params['voucher_send_mode_info'] = self.voucher_send_mode_info
        if self.voucher_use_rule:
            if hasattr(self.voucher_use_rule, 'to_alipay_dict'):
                params['voucher_use_rule'] = self.voucher_use_rule.to_alipay_dict()
            else:
                params['voucher_use_rule'] = self.voucher_use_rule
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
        o = AlipayMarketingActivityVoucherModifyModel()
        if 'activity_base_info' in d:
            o.activity_base_info = d['activity_base_info']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'merchant_access_mode' in d:
            o.merchant_access_mode = d['merchant_access_mode']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'publish_end_time' in d:
            o.publish_end_time = d['publish_end_time']
        if 'voucher_available_scope_info' in d:
            o.voucher_available_scope_info = d['voucher_available_scope_info']
        if 'voucher_send_mode_info' in d:
            o.voucher_send_mode_info = d['voucher_send_mode_info']
        if 'voucher_use_rule' in d:
            o.voucher_use_rule = d['voucher_use_rule']
        if 'voucher_use_rule_info' in d:
            o.voucher_use_rule_info = d['voucher_use_rule_info']
        return o


