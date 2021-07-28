#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CampaignExtInfo import CampaignExtInfo


class AlipayCommerceDataCampaignCreateModel(object):

    def __init__(self):
        self._award_name = None
        self._end_time = None
        self._ext_info = None
        self._limit_product = None
        self._merchant_name = None
        self._merchant_pid = None
        self._milestone_list = None
        self._periodic_total_num = None
        self._push_unit = None
        self._push_unit_name = None
        self._recall_rule = None
        self._start_time = None

    @property
    def award_name(self):
        return self._award_name

    @award_name.setter
    def award_name(self, value):
        self._award_name = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def limit_product(self):
        return self._limit_product

    @limit_product.setter
    def limit_product(self, value):
        self._limit_product = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def milestone_list(self):
        return self._milestone_list

    @milestone_list.setter
    def milestone_list(self, value):
        self._milestone_list = value
    @property
    def periodic_total_num(self):
        return self._periodic_total_num

    @periodic_total_num.setter
    def periodic_total_num(self, value):
        self._periodic_total_num = value
    @property
    def push_unit(self):
        return self._push_unit

    @push_unit.setter
    def push_unit(self, value):
        self._push_unit = value
    @property
    def push_unit_name(self):
        return self._push_unit_name

    @push_unit_name.setter
    def push_unit_name(self, value):
        self._push_unit_name = value
    @property
    def recall_rule(self):
        return self._recall_rule

    @recall_rule.setter
    def recall_rule(self, value):
        if isinstance(value, CampaignExtInfo):
            self._recall_rule = value
        else:
            self._recall_rule = CampaignExtInfo.from_alipay_dict(value)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.award_name:
            if hasattr(self.award_name, 'to_alipay_dict'):
                params['award_name'] = self.award_name.to_alipay_dict()
            else:
                params['award_name'] = self.award_name
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.limit_product:
            if hasattr(self.limit_product, 'to_alipay_dict'):
                params['limit_product'] = self.limit_product.to_alipay_dict()
            else:
                params['limit_product'] = self.limit_product
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.milestone_list:
            if hasattr(self.milestone_list, 'to_alipay_dict'):
                params['milestone_list'] = self.milestone_list.to_alipay_dict()
            else:
                params['milestone_list'] = self.milestone_list
        if self.periodic_total_num:
            if hasattr(self.periodic_total_num, 'to_alipay_dict'):
                params['periodic_total_num'] = self.periodic_total_num.to_alipay_dict()
            else:
                params['periodic_total_num'] = self.periodic_total_num
        if self.push_unit:
            if hasattr(self.push_unit, 'to_alipay_dict'):
                params['push_unit'] = self.push_unit.to_alipay_dict()
            else:
                params['push_unit'] = self.push_unit
        if self.push_unit_name:
            if hasattr(self.push_unit_name, 'to_alipay_dict'):
                params['push_unit_name'] = self.push_unit_name.to_alipay_dict()
            else:
                params['push_unit_name'] = self.push_unit_name
        if self.recall_rule:
            if hasattr(self.recall_rule, 'to_alipay_dict'):
                params['recall_rule'] = self.recall_rule.to_alipay_dict()
            else:
                params['recall_rule'] = self.recall_rule
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
        o = AlipayCommerceDataCampaignCreateModel()
        if 'award_name' in d:
            o.award_name = d['award_name']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'limit_product' in d:
            o.limit_product = d['limit_product']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'milestone_list' in d:
            o.milestone_list = d['milestone_list']
        if 'periodic_total_num' in d:
            o.periodic_total_num = d['periodic_total_num']
        if 'push_unit' in d:
            o.push_unit = d['push_unit']
        if 'push_unit_name' in d:
            o.push_unit_name = d['push_unit_name']
        if 'recall_rule' in d:
            o.recall_rule = d['recall_rule']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


