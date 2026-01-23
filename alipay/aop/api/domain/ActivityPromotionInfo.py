#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityPromotionDuration import ActivityPromotionDuration


class ActivityPromotionInfo(object):

    def __init__(self):
        self._activity_promotion_duration = None
        self._ceil_promotion_amount = None
        self._deduction_amount = None
        self._discount_ratio = None
        self._product_type = None
        self._promotion_type = None
        self._threshold_amount = None

    @property
    def activity_promotion_duration(self):
        return self._activity_promotion_duration

    @activity_promotion_duration.setter
    def activity_promotion_duration(self, value):
        if isinstance(value, ActivityPromotionDuration):
            self._activity_promotion_duration = value
        else:
            self._activity_promotion_duration = ActivityPromotionDuration.from_alipay_dict(value)
    @property
    def ceil_promotion_amount(self):
        return self._ceil_promotion_amount

    @ceil_promotion_amount.setter
    def ceil_promotion_amount(self, value):
        self._ceil_promotion_amount = value
    @property
    def deduction_amount(self):
        return self._deduction_amount

    @deduction_amount.setter
    def deduction_amount(self, value):
        self._deduction_amount = value
    @property
    def discount_ratio(self):
        return self._discount_ratio

    @discount_ratio.setter
    def discount_ratio(self, value):
        self._discount_ratio = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def promotion_type(self):
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, value):
        self._promotion_type = value
    @property
    def threshold_amount(self):
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, value):
        self._threshold_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_promotion_duration:
            if hasattr(self.activity_promotion_duration, 'to_alipay_dict'):
                params['activity_promotion_duration'] = self.activity_promotion_duration.to_alipay_dict()
            else:
                params['activity_promotion_duration'] = self.activity_promotion_duration
        if self.ceil_promotion_amount:
            if hasattr(self.ceil_promotion_amount, 'to_alipay_dict'):
                params['ceil_promotion_amount'] = self.ceil_promotion_amount.to_alipay_dict()
            else:
                params['ceil_promotion_amount'] = self.ceil_promotion_amount
        if self.deduction_amount:
            if hasattr(self.deduction_amount, 'to_alipay_dict'):
                params['deduction_amount'] = self.deduction_amount.to_alipay_dict()
            else:
                params['deduction_amount'] = self.deduction_amount
        if self.discount_ratio:
            if hasattr(self.discount_ratio, 'to_alipay_dict'):
                params['discount_ratio'] = self.discount_ratio.to_alipay_dict()
            else:
                params['discount_ratio'] = self.discount_ratio
        if self.product_type:
            if hasattr(self.product_type, 'to_alipay_dict'):
                params['product_type'] = self.product_type.to_alipay_dict()
            else:
                params['product_type'] = self.product_type
        if self.promotion_type:
            if hasattr(self.promotion_type, 'to_alipay_dict'):
                params['promotion_type'] = self.promotion_type.to_alipay_dict()
            else:
                params['promotion_type'] = self.promotion_type
        if self.threshold_amount:
            if hasattr(self.threshold_amount, 'to_alipay_dict'):
                params['threshold_amount'] = self.threshold_amount.to_alipay_dict()
            else:
                params['threshold_amount'] = self.threshold_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityPromotionInfo()
        if 'activity_promotion_duration' in d:
            o.activity_promotion_duration = d['activity_promotion_duration']
        if 'ceil_promotion_amount' in d:
            o.ceil_promotion_amount = d['ceil_promotion_amount']
        if 'deduction_amount' in d:
            o.deduction_amount = d['deduction_amount']
        if 'discount_ratio' in d:
            o.discount_ratio = d['discount_ratio']
        if 'product_type' in d:
            o.product_type = d['product_type']
        if 'promotion_type' in d:
            o.promotion_type = d['promotion_type']
        if 'threshold_amount' in d:
            o.threshold_amount = d['threshold_amount']
        return o


