#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromotionDurationResponse import PromotionDurationResponse


class VoucherActivityResponse(object):

    def __init__(self):
        self._activity_describe = None
        self._activity_effective_end_time = None
        self._activity_effective_start_time = None
        self._activity_id = None
        self._activity_name = None
        self._ceiling_amount = None
        self._promotion_discount = None
        self._promotion_duration = None
        self._promotion_limit = None
        self._threshold_amount = None
        self._voucher_amount = None
        self._voucher_describe = None
        self._voucher_name = None
        self._voucher_type = None

    @property
    def activity_describe(self):
        return self._activity_describe

    @activity_describe.setter
    def activity_describe(self, value):
        self._activity_describe = value
    @property
    def activity_effective_end_time(self):
        return self._activity_effective_end_time

    @activity_effective_end_time.setter
    def activity_effective_end_time(self, value):
        self._activity_effective_end_time = value
    @property
    def activity_effective_start_time(self):
        return self._activity_effective_start_time

    @activity_effective_start_time.setter
    def activity_effective_start_time(self, value):
        self._activity_effective_start_time = value
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
    def ceiling_amount(self):
        return self._ceiling_amount

    @ceiling_amount.setter
    def ceiling_amount(self, value):
        self._ceiling_amount = value
    @property
    def promotion_discount(self):
        return self._promotion_discount

    @promotion_discount.setter
    def promotion_discount(self, value):
        self._promotion_discount = value
    @property
    def promotion_duration(self):
        return self._promotion_duration

    @promotion_duration.setter
    def promotion_duration(self, value):
        if isinstance(value, PromotionDurationResponse):
            self._promotion_duration = value
        else:
            self._promotion_duration = PromotionDurationResponse.from_alipay_dict(value)
    @property
    def promotion_limit(self):
        return self._promotion_limit

    @promotion_limit.setter
    def promotion_limit(self, value):
        self._promotion_limit = value
    @property
    def threshold_amount(self):
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, value):
        self._threshold_amount = value
    @property
    def voucher_amount(self):
        return self._voucher_amount

    @voucher_amount.setter
    def voucher_amount(self, value):
        self._voucher_amount = value
    @property
    def voucher_describe(self):
        return self._voucher_describe

    @voucher_describe.setter
    def voucher_describe(self, value):
        self._voucher_describe = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_describe:
            if hasattr(self.activity_describe, 'to_alipay_dict'):
                params['activity_describe'] = self.activity_describe.to_alipay_dict()
            else:
                params['activity_describe'] = self.activity_describe
        if self.activity_effective_end_time:
            if hasattr(self.activity_effective_end_time, 'to_alipay_dict'):
                params['activity_effective_end_time'] = self.activity_effective_end_time.to_alipay_dict()
            else:
                params['activity_effective_end_time'] = self.activity_effective_end_time
        if self.activity_effective_start_time:
            if hasattr(self.activity_effective_start_time, 'to_alipay_dict'):
                params['activity_effective_start_time'] = self.activity_effective_start_time.to_alipay_dict()
            else:
                params['activity_effective_start_time'] = self.activity_effective_start_time
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.ceiling_amount:
            if hasattr(self.ceiling_amount, 'to_alipay_dict'):
                params['ceiling_amount'] = self.ceiling_amount.to_alipay_dict()
            else:
                params['ceiling_amount'] = self.ceiling_amount
        if self.promotion_discount:
            if hasattr(self.promotion_discount, 'to_alipay_dict'):
                params['promotion_discount'] = self.promotion_discount.to_alipay_dict()
            else:
                params['promotion_discount'] = self.promotion_discount
        if self.promotion_duration:
            if hasattr(self.promotion_duration, 'to_alipay_dict'):
                params['promotion_duration'] = self.promotion_duration.to_alipay_dict()
            else:
                params['promotion_duration'] = self.promotion_duration
        if self.promotion_limit:
            if hasattr(self.promotion_limit, 'to_alipay_dict'):
                params['promotion_limit'] = self.promotion_limit.to_alipay_dict()
            else:
                params['promotion_limit'] = self.promotion_limit
        if self.threshold_amount:
            if hasattr(self.threshold_amount, 'to_alipay_dict'):
                params['threshold_amount'] = self.threshold_amount.to_alipay_dict()
            else:
                params['threshold_amount'] = self.threshold_amount
        if self.voucher_amount:
            if hasattr(self.voucher_amount, 'to_alipay_dict'):
                params['voucher_amount'] = self.voucher_amount.to_alipay_dict()
            else:
                params['voucher_amount'] = self.voucher_amount
        if self.voucher_describe:
            if hasattr(self.voucher_describe, 'to_alipay_dict'):
                params['voucher_describe'] = self.voucher_describe.to_alipay_dict()
            else:
                params['voucher_describe'] = self.voucher_describe
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherActivityResponse()
        if 'activity_describe' in d:
            o.activity_describe = d['activity_describe']
        if 'activity_effective_end_time' in d:
            o.activity_effective_end_time = d['activity_effective_end_time']
        if 'activity_effective_start_time' in d:
            o.activity_effective_start_time = d['activity_effective_start_time']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'ceiling_amount' in d:
            o.ceiling_amount = d['ceiling_amount']
        if 'promotion_discount' in d:
            o.promotion_discount = d['promotion_discount']
        if 'promotion_duration' in d:
            o.promotion_duration = d['promotion_duration']
        if 'promotion_limit' in d:
            o.promotion_limit = d['promotion_limit']
        if 'threshold_amount' in d:
            o.threshold_amount = d['threshold_amount']
        if 'voucher_amount' in d:
            o.voucher_amount = d['voucher_amount']
        if 'voucher_describe' in d:
            o.voucher_describe = d['voucher_describe']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


