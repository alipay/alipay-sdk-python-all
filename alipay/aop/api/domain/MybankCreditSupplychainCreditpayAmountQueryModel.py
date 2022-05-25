#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BrandQuotaQueryCondition import BrandQuotaQueryCondition
from alipay.aop.api.domain.Member import Member


class MybankCreditSupplychainCreditpayAmountQueryModel(object):

    def __init__(self):
        self._brand_quota_query_condition = None
        self._buyer = None
        self._channel_tag = None
        self._trace_id = None

    @property
    def brand_quota_query_condition(self):
        return self._brand_quota_query_condition

    @brand_quota_query_condition.setter
    def brand_quota_query_condition(self, value):
        if isinstance(value, BrandQuotaQueryCondition):
            self._brand_quota_query_condition = value
        else:
            self._brand_quota_query_condition = BrandQuotaQueryCondition.from_alipay_dict(value)
    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        if isinstance(value, Member):
            self._buyer = value
        else:
            self._buyer = Member.from_alipay_dict(value)
    @property
    def channel_tag(self):
        return self._channel_tag

    @channel_tag.setter
    def channel_tag(self, value):
        self._channel_tag = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_quota_query_condition:
            if hasattr(self.brand_quota_query_condition, 'to_alipay_dict'):
                params['brand_quota_query_condition'] = self.brand_quota_query_condition.to_alipay_dict()
            else:
                params['brand_quota_query_condition'] = self.brand_quota_query_condition
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.channel_tag:
            if hasattr(self.channel_tag, 'to_alipay_dict'):
                params['channel_tag'] = self.channel_tag.to_alipay_dict()
            else:
                params['channel_tag'] = self.channel_tag
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainCreditpayAmountQueryModel()
        if 'brand_quota_query_condition' in d:
            o.brand_quota_query_condition = d['brand_quota_query_condition']
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'channel_tag' in d:
            o.channel_tag = d['channel_tag']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o


