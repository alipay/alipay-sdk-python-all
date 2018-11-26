#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityRuleDetail import ActivityRuleDetail
from alipay.aop.api.domain.ActivityShop import ActivityShop


class ZhimaMerchantActivityCreateModel(object):

    def __init__(self):
        self._activity_name = None
        self._activity_rule_detail = None
        self._activity_shops = None
        self._brand_name = None
        self._category_code = None
        self._end_time = None
        self._fulfil_dimension = None
        self._out_activity_no = None
        self._payback_account = None
        self._rule_type = None
        self._start_time = None

    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_rule_detail(self):
        return self._activity_rule_detail

    @activity_rule_detail.setter
    def activity_rule_detail(self, value):
        if isinstance(value, ActivityRuleDetail):
            self._activity_rule_detail = value
        else:
            self._activity_rule_detail = ActivityRuleDetail.from_alipay_dict(value)
    @property
    def activity_shops(self):
        return self._activity_shops

    @activity_shops.setter
    def activity_shops(self, value):
        if isinstance(value, list):
            self._activity_shops = list()
            for i in value:
                if isinstance(i, ActivityShop):
                    self._activity_shops.append(i)
                else:
                    self._activity_shops.append(ActivityShop.from_alipay_dict(i))
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def fulfil_dimension(self):
        return self._fulfil_dimension

    @fulfil_dimension.setter
    def fulfil_dimension(self, value):
        self._fulfil_dimension = value
    @property
    def out_activity_no(self):
        return self._out_activity_no

    @out_activity_no.setter
    def out_activity_no(self, value):
        self._out_activity_no = value
    @property
    def payback_account(self):
        return self._payback_account

    @payback_account.setter
    def payback_account(self, value):
        self._payback_account = value
    @property
    def rule_type(self):
        return self._rule_type

    @rule_type.setter
    def rule_type(self, value):
        self._rule_type = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.activity_rule_detail:
            if hasattr(self.activity_rule_detail, 'to_alipay_dict'):
                params['activity_rule_detail'] = self.activity_rule_detail.to_alipay_dict()
            else:
                params['activity_rule_detail'] = self.activity_rule_detail
        if self.activity_shops:
            if isinstance(self.activity_shops, list):
                for i in range(0, len(self.activity_shops)):
                    element = self.activity_shops[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_shops[i] = element.to_alipay_dict()
            if hasattr(self.activity_shops, 'to_alipay_dict'):
                params['activity_shops'] = self.activity_shops.to_alipay_dict()
            else:
                params['activity_shops'] = self.activity_shops
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.fulfil_dimension:
            if hasattr(self.fulfil_dimension, 'to_alipay_dict'):
                params['fulfil_dimension'] = self.fulfil_dimension.to_alipay_dict()
            else:
                params['fulfil_dimension'] = self.fulfil_dimension
        if self.out_activity_no:
            if hasattr(self.out_activity_no, 'to_alipay_dict'):
                params['out_activity_no'] = self.out_activity_no.to_alipay_dict()
            else:
                params['out_activity_no'] = self.out_activity_no
        if self.payback_account:
            if hasattr(self.payback_account, 'to_alipay_dict'):
                params['payback_account'] = self.payback_account.to_alipay_dict()
            else:
                params['payback_account'] = self.payback_account
        if self.rule_type:
            if hasattr(self.rule_type, 'to_alipay_dict'):
                params['rule_type'] = self.rule_type.to_alipay_dict()
            else:
                params['rule_type'] = self.rule_type
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantActivityCreateModel()
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'activity_rule_detail' in d:
            o.activity_rule_detail = d['activity_rule_detail']
        if 'activity_shops' in d:
            o.activity_shops = d['activity_shops']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'fulfil_dimension' in d:
            o.fulfil_dimension = d['fulfil_dimension']
        if 'out_activity_no' in d:
            o.out_activity_no = d['out_activity_no']
        if 'payback_account' in d:
            o.payback_account = d['payback_account']
        if 'rule_type' in d:
            o.rule_type = d['rule_type']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


