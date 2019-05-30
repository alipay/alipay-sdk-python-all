#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityRuleDetail import ActivityRuleDetail
from alipay.aop.api.domain.ActivityShop import ActivityShop
from alipay.aop.api.domain.ActivityStat import ActivityStat


class Activity(object):

    def __init__(self):
        self._activity_name = None
        self._activity_no = None
        self._activity_rule_detail = None
        self._activity_shop_list = None
        self._activity_stat = None
        self._activity_status = None
        self._brand_name = None
        self._end_time = None
        self._fulfil_dimension = None
        self._invoke_app_id = None
        self._out_activity_no = None
        self._partner_id = None
        self._rule_type = None
        self._rule_type_desc = None
        self._start_time = None

    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_no(self):
        return self._activity_no

    @activity_no.setter
    def activity_no(self, value):
        self._activity_no = value
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
    def activity_shop_list(self):
        return self._activity_shop_list

    @activity_shop_list.setter
    def activity_shop_list(self, value):
        if isinstance(value, list):
            self._activity_shop_list = list()
            for i in value:
                if isinstance(i, ActivityShop):
                    self._activity_shop_list.append(i)
                else:
                    self._activity_shop_list.append(ActivityShop.from_alipay_dict(i))
    @property
    def activity_stat(self):
        return self._activity_stat

    @activity_stat.setter
    def activity_stat(self, value):
        if isinstance(value, ActivityStat):
            self._activity_stat = value
        else:
            self._activity_stat = ActivityStat.from_alipay_dict(value)
    @property
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
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
    def invoke_app_id(self):
        return self._invoke_app_id

    @invoke_app_id.setter
    def invoke_app_id(self, value):
        self._invoke_app_id = value
    @property
    def out_activity_no(self):
        return self._out_activity_no

    @out_activity_no.setter
    def out_activity_no(self, value):
        self._out_activity_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def rule_type(self):
        return self._rule_type

    @rule_type.setter
    def rule_type(self, value):
        self._rule_type = value
    @property
    def rule_type_desc(self):
        return self._rule_type_desc

    @rule_type_desc.setter
    def rule_type_desc(self, value):
        self._rule_type_desc = value
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
        if self.activity_no:
            if hasattr(self.activity_no, 'to_alipay_dict'):
                params['activity_no'] = self.activity_no.to_alipay_dict()
            else:
                params['activity_no'] = self.activity_no
        if self.activity_rule_detail:
            if hasattr(self.activity_rule_detail, 'to_alipay_dict'):
                params['activity_rule_detail'] = self.activity_rule_detail.to_alipay_dict()
            else:
                params['activity_rule_detail'] = self.activity_rule_detail
        if self.activity_shop_list:
            if isinstance(self.activity_shop_list, list):
                for i in range(0, len(self.activity_shop_list)):
                    element = self.activity_shop_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_shop_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_shop_list, 'to_alipay_dict'):
                params['activity_shop_list'] = self.activity_shop_list.to_alipay_dict()
            else:
                params['activity_shop_list'] = self.activity_shop_list
        if self.activity_stat:
            if hasattr(self.activity_stat, 'to_alipay_dict'):
                params['activity_stat'] = self.activity_stat.to_alipay_dict()
            else:
                params['activity_stat'] = self.activity_stat
        if self.activity_status:
            if hasattr(self.activity_status, 'to_alipay_dict'):
                params['activity_status'] = self.activity_status.to_alipay_dict()
            else:
                params['activity_status'] = self.activity_status
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
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
        if self.invoke_app_id:
            if hasattr(self.invoke_app_id, 'to_alipay_dict'):
                params['invoke_app_id'] = self.invoke_app_id.to_alipay_dict()
            else:
                params['invoke_app_id'] = self.invoke_app_id
        if self.out_activity_no:
            if hasattr(self.out_activity_no, 'to_alipay_dict'):
                params['out_activity_no'] = self.out_activity_no.to_alipay_dict()
            else:
                params['out_activity_no'] = self.out_activity_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.rule_type:
            if hasattr(self.rule_type, 'to_alipay_dict'):
                params['rule_type'] = self.rule_type.to_alipay_dict()
            else:
                params['rule_type'] = self.rule_type
        if self.rule_type_desc:
            if hasattr(self.rule_type_desc, 'to_alipay_dict'):
                params['rule_type_desc'] = self.rule_type_desc.to_alipay_dict()
            else:
                params['rule_type_desc'] = self.rule_type_desc
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
        o = Activity()
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'activity_no' in d:
            o.activity_no = d['activity_no']
        if 'activity_rule_detail' in d:
            o.activity_rule_detail = d['activity_rule_detail']
        if 'activity_shop_list' in d:
            o.activity_shop_list = d['activity_shop_list']
        if 'activity_stat' in d:
            o.activity_stat = d['activity_stat']
        if 'activity_status' in d:
            o.activity_status = d['activity_status']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'fulfil_dimension' in d:
            o.fulfil_dimension = d['fulfil_dimension']
        if 'invoke_app_id' in d:
            o.invoke_app_id = d['invoke_app_id']
        if 'out_activity_no' in d:
            o.out_activity_no = d['out_activity_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'rule_type' in d:
            o.rule_type = d['rule_type']
        if 'rule_type_desc' in d:
            o.rule_type_desc = d['rule_type_desc']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


