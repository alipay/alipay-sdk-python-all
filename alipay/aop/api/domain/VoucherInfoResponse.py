#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromotionDurationResponse import PromotionDurationResponse


class VoucherInfoResponse(object):

    def __init__(self):
        self._activity_id = None
        self._brand_name = None
        self._ceiling_amount = None
        self._logo = None
        self._promotion_discount = None
        self._promotion_duration = None
        self._promotion_limit = None
        self._threshold_amount = None
        self._voucher_amount = None
        self._voucher_description = None
        self._voucher_effective_end_time = None
        self._voucher_effective_start_time = None
        self._voucher_id = None
        self._voucher_jump_url = None
        self._voucher_name = None
        self._voucher_status = None
        self._voucher_type = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def ceiling_amount(self):
        return self._ceiling_amount

    @ceiling_amount.setter
    def ceiling_amount(self, value):
        self._ceiling_amount = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
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
    def voucher_description(self):
        return self._voucher_description

    @voucher_description.setter
    def voucher_description(self, value):
        self._voucher_description = value
    @property
    def voucher_effective_end_time(self):
        return self._voucher_effective_end_time

    @voucher_effective_end_time.setter
    def voucher_effective_end_time(self, value):
        self._voucher_effective_end_time = value
    @property
    def voucher_effective_start_time(self):
        return self._voucher_effective_start_time

    @voucher_effective_start_time.setter
    def voucher_effective_start_time(self, value):
        self._voucher_effective_start_time = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_jump_url(self):
        return self._voucher_jump_url

    @voucher_jump_url.setter
    def voucher_jump_url(self, value):
        self._voucher_jump_url = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.ceiling_amount:
            if hasattr(self.ceiling_amount, 'to_alipay_dict'):
                params['ceiling_amount'] = self.ceiling_amount.to_alipay_dict()
            else:
                params['ceiling_amount'] = self.ceiling_amount
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
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
        if self.voucher_description:
            if hasattr(self.voucher_description, 'to_alipay_dict'):
                params['voucher_description'] = self.voucher_description.to_alipay_dict()
            else:
                params['voucher_description'] = self.voucher_description
        if self.voucher_effective_end_time:
            if hasattr(self.voucher_effective_end_time, 'to_alipay_dict'):
                params['voucher_effective_end_time'] = self.voucher_effective_end_time.to_alipay_dict()
            else:
                params['voucher_effective_end_time'] = self.voucher_effective_end_time
        if self.voucher_effective_start_time:
            if hasattr(self.voucher_effective_start_time, 'to_alipay_dict'):
                params['voucher_effective_start_time'] = self.voucher_effective_start_time.to_alipay_dict()
            else:
                params['voucher_effective_start_time'] = self.voucher_effective_start_time
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_jump_url:
            if hasattr(self.voucher_jump_url, 'to_alipay_dict'):
                params['voucher_jump_url'] = self.voucher_jump_url.to_alipay_dict()
            else:
                params['voucher_jump_url'] = self.voucher_jump_url
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherInfoResponse()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'ceiling_amount' in d:
            o.ceiling_amount = d['ceiling_amount']
        if 'logo' in d:
            o.logo = d['logo']
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
        if 'voucher_description' in d:
            o.voucher_description = d['voucher_description']
        if 'voucher_effective_end_time' in d:
            o.voucher_effective_end_time = d['voucher_effective_end_time']
        if 'voucher_effective_start_time' in d:
            o.voucher_effective_start_time = d['voucher_effective_start_time']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_jump_url' in d:
            o.voucher_jump_url = d['voucher_jump_url']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_status' in d:
            o.voucher_status = d['voucher_status']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


