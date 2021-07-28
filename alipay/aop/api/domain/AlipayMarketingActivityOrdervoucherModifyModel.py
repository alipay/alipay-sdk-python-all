#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CustomerGuideModify import CustomerGuideModify
from alipay.aop.api.domain.VoucherUseRuleModify import VoucherUseRuleModify


class AlipayMarketingActivityOrdervoucherModifyModel(object):

    def __init__(self):
        self._activity_id = None
        self._customer_guide = None
        self._out_biz_no = None
        self._publish_end_time = None
        self._voucher_use_rule = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def customer_guide(self):
        return self._customer_guide

    @customer_guide.setter
    def customer_guide(self, value):
        if isinstance(value, CustomerGuideModify):
            self._customer_guide = value
        else:
            self._customer_guide = CustomerGuideModify.from_alipay_dict(value)
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
    def voucher_use_rule(self):
        return self._voucher_use_rule

    @voucher_use_rule.setter
    def voucher_use_rule(self, value):
        if isinstance(value, VoucherUseRuleModify):
            self._voucher_use_rule = value
        else:
            self._voucher_use_rule = VoucherUseRuleModify.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
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
        o = AlipayMarketingActivityOrdervoucherModifyModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'customer_guide' in d:
            o.customer_guide = d['customer_guide']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'publish_end_time' in d:
            o.publish_end_time = d['publish_end_time']
        if 'voucher_use_rule' in d:
            o.voucher_use_rule = d['voucher_use_rule']
        return o


