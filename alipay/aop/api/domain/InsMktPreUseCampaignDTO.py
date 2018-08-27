#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsMktPreUseCampaignDTO(object):

    def __init__(self):
        self._campaign_id = None
        self._campaign_name = None
        self._coupon_type = None
        self._coupon_upper_value = None
        self._coupon_value = None
        self._pre_use = None
        self._reason = None

    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        self._campaign_id = value
    @property
    def campaign_name(self):
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, value):
        self._campaign_name = value
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
    @property
    def pre_use(self):
        return self._pre_use

    @pre_use.setter
    def pre_use(self, value):
        self._pre_use = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.campaign_id:
            if hasattr(self.campaign_id, 'to_alipay_dict'):
                params['campaign_id'] = self.campaign_id.to_alipay_dict()
            else:
                params['campaign_id'] = self.campaign_id
        if self.campaign_name:
            if hasattr(self.campaign_name, 'to_alipay_dict'):
                params['campaign_name'] = self.campaign_name.to_alipay_dict()
            else:
                params['campaign_name'] = self.campaign_name
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
        if self.pre_use:
            if hasattr(self.pre_use, 'to_alipay_dict'):
                params['pre_use'] = self.pre_use.to_alipay_dict()
            else:
                params['pre_use'] = self.pre_use
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsMktPreUseCampaignDTO()
        if 'campaign_id' in d:
            o.campaign_id = d['campaign_id']
        if 'campaign_name' in d:
            o.campaign_name = d['campaign_name']
        if 'coupon_type' in d:
            o.coupon_type = d['coupon_type']
        if 'coupon_upper_value' in d:
            o.coupon_upper_value = d['coupon_upper_value']
        if 'coupon_value' in d:
            o.coupon_value = d['coupon_value']
        if 'pre_use' in d:
            o.pre_use = d['pre_use']
        if 'reason' in d:
            o.reason = d['reason']
        return o


