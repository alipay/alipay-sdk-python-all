#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaymentVoucherBelongMerchantInfo import PaymentVoucherBelongMerchantInfo
from alipay.aop.api.domain.PaymentVoucherBudgetInfo import PaymentVoucherBudgetInfo
from alipay.aop.api.domain.PaymentVoucherDisplayInfo import PaymentVoucherDisplayInfo
from alipay.aop.api.domain.PaymentVoucherSendRule import PaymentVoucherSendRule
from alipay.aop.api.domain.PaymentVoucherUseRule import PaymentVoucherUseRule


class AlipayMarketingActivityVoucherCreateModel(object):

    def __init__(self):
        self._activity_name = None
        self._belong_merchant_info = None
        self._out_biz_no = None
        self._publish_end_time = None
        self._publish_start_time = None
        self._voucher_budget_info = None
        self._voucher_display_info = None
        self._voucher_send_rule = None
        self._voucher_type = None
        self._voucher_use_rule = None

    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
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
    def publish_start_time(self):
        return self._publish_start_time

    @publish_start_time.setter
    def publish_start_time(self, value):
        self._publish_start_time = value
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
        if isinstance(value, PaymentVoucherUseRule):
            self._voucher_use_rule = value
        else:
            self._voucher_use_rule = PaymentVoucherUseRule.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.belong_merchant_info:
            if hasattr(self.belong_merchant_info, 'to_alipay_dict'):
                params['belong_merchant_info'] = self.belong_merchant_info.to_alipay_dict()
            else:
                params['belong_merchant_info'] = self.belong_merchant_info
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
        if self.publish_start_time:
            if hasattr(self.publish_start_time, 'to_alipay_dict'):
                params['publish_start_time'] = self.publish_start_time.to_alipay_dict()
            else:
                params['publish_start_time'] = self.publish_start_time
        if self.voucher_budget_info:
            if hasattr(self.voucher_budget_info, 'to_alipay_dict'):
                params['voucher_budget_info'] = self.voucher_budget_info.to_alipay_dict()
            else:
                params['voucher_budget_info'] = self.voucher_budget_info
        if self.voucher_display_info:
            if hasattr(self.voucher_display_info, 'to_alipay_dict'):
                params['voucher_display_info'] = self.voucher_display_info.to_alipay_dict()
            else:
                params['voucher_display_info'] = self.voucher_display_info
        if self.voucher_send_rule:
            if hasattr(self.voucher_send_rule, 'to_alipay_dict'):
                params['voucher_send_rule'] = self.voucher_send_rule.to_alipay_dict()
            else:
                params['voucher_send_rule'] = self.voucher_send_rule
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        if self.voucher_use_rule:
            if hasattr(self.voucher_use_rule, 'to_alipay_dict'):
                params['voucher_use_rule'] = self.voucher_use_rule.to_alipay_dict()
            else:
                params['voucher_use_rule'] = self.voucher_use_rule
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityVoucherCreateModel()
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'belong_merchant_info' in d:
            o.belong_merchant_info = d['belong_merchant_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'publish_end_time' in d:
            o.publish_end_time = d['publish_end_time']
        if 'publish_start_time' in d:
            o.publish_start_time = d['publish_start_time']
        if 'voucher_budget_info' in d:
            o.voucher_budget_info = d['voucher_budget_info']
        if 'voucher_display_info' in d:
            o.voucher_display_info = d['voucher_display_info']
        if 'voucher_send_rule' in d:
            o.voucher_send_rule = d['voucher_send_rule']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        if 'voucher_use_rule' in d:
            o.voucher_use_rule = d['voucher_use_rule']
        return o


