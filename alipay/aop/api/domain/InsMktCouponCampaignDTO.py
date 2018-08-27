#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsMktCouponCampaignDTO(object):

    def __init__(self):
        self._campaign_end_time = None
        self._campaign_id = None
        self._campaign_memo = None
        self._campaign_name = None
        self._campaign_start_time = None
        self._coupon_type = None
        self._coupon_upper_value = None
        self._coupon_value = None

    @property
    def campaign_end_time(self):
        return self._campaign_end_time

    @campaign_end_time.setter
    def campaign_end_time(self, value):
        self._campaign_end_time = value
    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        self._campaign_id = value
    @property
    def campaign_memo(self):
        return self._campaign_memo

    @campaign_memo.setter
    def campaign_memo(self, value):
        self._campaign_memo = value
    @property
    def campaign_name(self):
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, value):
        self._campaign_name = value
    @property
    def campaign_start_time(self):
        return self._campaign_start_time

    @campaign_start_time.setter
    def campaign_start_time(self, value):
        self._campaign_start_time = value
    @property
    def coupon_type(self):
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, value):
        self._coupon_type = value
    @property
    def coupon_upper_value(self):
        return self._coupon_upper_value

    @coupon_upper_value.setter
    def coupon_upper_value(self, value):
        self._coupon_upper_value = value
    @property
    def coupon_value(self):
        return self._coupon_value

    @coupon_value.setter
    def coupon_value(self, value):
        self._coupon_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.campaign_end_time:
            if hasattr(self.campaign_end_time, 'to_alipay_dict'):
                params['campaign_end_time'] = self.campaign_end_time.to_alipay_dict()
            else:
                params['campaign_end_time'] = self.campaign_end_time
        if self.campaign_id:
            if hasattr(self.campaign_id, 'to_alipay_dict'):
                params['campaign_id'] = self.campaign_id.to_alipay_dict()
            else:
                params['campaign_id'] = self.campaign_id
        if self.campaign_memo:
            if hasattr(self.campaign_memo, 'to_alipay_dict'):
                params['campaign_memo'] = self.campaign_memo.to_alipay_dict()
            else:
                params['campaign_memo'] = self.campaign_memo
        if self.campaign_name:
            if hasattr(self.campaign_name, 'to_alipay_dict'):
                params['campaign_name'] = self.campaign_name.to_alipay_dict()
            else:
                params['campaign_name'] = self.campaign_name
        if self.campaign_start_time:
            if hasattr(self.campaign_start_time, 'to_alipay_dict'):
                params['campaign_start_time'] = self.campaign_start_time.to_alipay_dict()
            else:
                params['campaign_start_time'] = self.campaign_start_time
        if self.coupon_type:
            if hasattr(self.coupon_type, 'to_alipay_dict'):
                params['coupon_type'] = self.coupon_type.to_alipay_dict()
            else:
                params['coupon_type'] = self.coupon_type
        if self.coupon_upper_value:
            if hasattr(self.coupon_upper_value, 'to_alipay_dict'):
                params['coupon_upper_value'] = self.coupon_upper_value.to_alipay_dict()
            else:
                params['coupon_upper_value'] = self.coupon_upper_value
        if self.coupon_value:
            if hasattr(self.coupon_value, 'to_alipay_dict'):
                params['coupon_value'] = self.coupon_value.to_alipay_dict()
            else:
                params['coupon_value'] = self.coupon_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsMktCouponCampaignDTO()
        if 'campaign_end_time' in d:
            o.campaign_end_time = d['campaign_end_time']
        if 'campaign_id' in d:
            o.campaign_id = d['campaign_id']
        if 'campaign_memo' in d:
            o.campaign_memo = d['campaign_memo']
        if 'campaign_name' in d:
            o.campaign_name = d['campaign_name']
        if 'campaign_start_time' in d:
            o.campaign_start_time = d['campaign_start_time']
        if 'coupon_type' in d:
            o.coupon_type = d['coupon_type']
        if 'coupon_upper_value' in d:
            o.coupon_upper_value = d['coupon_upper_value']
        if 'coupon_value' in d:
            o.coupon_value = d['coupon_value']
        return o


