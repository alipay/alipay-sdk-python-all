#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BelongMerchantInfo import BelongMerchantInfo
from alipay.aop.api.domain.CustomerGuide import CustomerGuide
from alipay.aop.api.domain.VoucherDisplayInfo import VoucherDisplayInfo
from alipay.aop.api.domain.VoucherSendRuleDetail import VoucherSendRuleDetail
from alipay.aop.api.domain.VoucherUseRule import VoucherUseRule


class AlipayMarketingActivityOrdervoucherCreateModel(object):

    def __init__(self):
        self._activity_name = None
        self._belong_merchant_info = None
        self._biz_tag = None
        self._code_mode = None
        self._customer_guide = None
        self._out_biz_no = None
        self._publish_end_time = None
        self._publish_start_time = None
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
    def code_mode(self):
        return self._code_mode

    @code_mode.setter
    def code_mode(self, value):
        self._code_mode = value
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
        if self.biz_tag:
            if hasattr(self.biz_tag, 'to_alipay_dict'):
                params['biz_tag'] = self.biz_tag.to_alipay_dict()
            else:
                params['biz_tag'] = self.biz_tag
        if self.code_mode:
            if hasattr(self.code_mode, 'to_alipay_dict'):
                params['code_mode'] = self.code_mode.to_alipay_dict()
            else:
                params['code_mode'] = self.code_mode
        if self.customer_guide:
            if hasattr(self.customer_guide, 'to_alipay_dict'):
                params['customer_guide'] = self.customer_guide.to_alipay_dict()
            else:
                params['customer_guide'] = self.customer_guide
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
        o = AlipayMarketingActivityOrdervoucherCreateModel()
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'belong_merchant_info' in d:
            o.belong_merchant_info = d['belong_merchant_info']
        if 'biz_tag' in d:
            o.biz_tag = d['biz_tag']
        if 'code_mode' in d:
            o.code_mode = d['code_mode']
        if 'customer_guide' in d:
            o.customer_guide = d['customer_guide']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'publish_end_time' in d:
            o.publish_end_time = d['publish_end_time']
        if 'publish_start_time' in d:
            o.publish_start_time = d['publish_start_time']
        if 'voucher_display_info' in d:
            o.voucher_display_info = d['voucher_display_info']
        if 'voucher_send_rule' in d:
            o.voucher_send_rule = d['voucher_send_rule']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        if 'voucher_use_rule' in d:
            o.voucher_use_rule = d['voucher_use_rule']
        return o


