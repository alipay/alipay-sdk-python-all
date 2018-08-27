#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PlanRule import PlanRule


class ActivityPlanInfo(object):

    def __init__(self):
        self._activity_end_time = None
        self._activity_start_time = None
        self._confirm_end_time = None
        self._invite_order_id = None
        self._plan_rule_list = None
        self._plat_activity_agreement = None
        self._plat_activity_id = None
        self._plat_activity_label_type = None
        self._plat_activity_name = None
        self._plat_activity_rule_desc = None
        self._plat_activity_status = None
        self._plat_other_desc = None

    @property
    def activity_end_time(self):
        return self._activity_end_time

    @activity_end_time.setter
    def activity_end_time(self, value):
        self._activity_end_time = value
    @property
    def activity_start_time(self):
        return self._activity_start_time

    @activity_start_time.setter
    def activity_start_time(self, value):
        self._activity_start_time = value
    @property
    def confirm_end_time(self):
        return self._confirm_end_time

    @confirm_end_time.setter
    def confirm_end_time(self, value):
        self._confirm_end_time = value
    @property
    def invite_order_id(self):
        return self._invite_order_id

    @invite_order_id.setter
    def invite_order_id(self, value):
        self._invite_order_id = value
    @property
    def plan_rule_list(self):
        return self._plan_rule_list

    @plan_rule_list.setter
    def plan_rule_list(self, value):
        if isinstance(value, list):
            self._plan_rule_list = list()
            for i in value:
                if isinstance(i, PlanRule):
                    self._plan_rule_list.append(i)
                else:
                    self._plan_rule_list.append(PlanRule.from_alipay_dict(i))
    @property
    def plat_activity_agreement(self):
        return self._plat_activity_agreement

    @plat_activity_agreement.setter
    def plat_activity_agreement(self, value):
        self._plat_activity_agreement = value
    @property
    def plat_activity_id(self):
        return self._plat_activity_id

    @plat_activity_id.setter
    def plat_activity_id(self, value):
        self._plat_activity_id = value
    @property
    def plat_activity_label_type(self):
        return self._plat_activity_label_type

    @plat_activity_label_type.setter
    def plat_activity_label_type(self, value):
        self._plat_activity_label_type = value
    @property
    def plat_activity_name(self):
        return self._plat_activity_name

    @plat_activity_name.setter
    def plat_activity_name(self, value):
        self._plat_activity_name = value
    @property
    def plat_activity_rule_desc(self):
        return self._plat_activity_rule_desc

    @plat_activity_rule_desc.setter
    def plat_activity_rule_desc(self, value):
        self._plat_activity_rule_desc = value
    @property
    def plat_activity_status(self):
        return self._plat_activity_status

    @plat_activity_status.setter
    def plat_activity_status(self, value):
        self._plat_activity_status = value
    @property
    def plat_other_desc(self):
        return self._plat_other_desc

    @plat_other_desc.setter
    def plat_other_desc(self, value):
        self._plat_other_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_end_time:
            if hasattr(self.activity_end_time, 'to_alipay_dict'):
                params['activity_end_time'] = self.activity_end_time.to_alipay_dict()
            else:
                params['activity_end_time'] = self.activity_end_time
        if self.activity_start_time:
            if hasattr(self.activity_start_time, 'to_alipay_dict'):
                params['activity_start_time'] = self.activity_start_time.to_alipay_dict()
            else:
                params['activity_start_time'] = self.activity_start_time
        if self.confirm_end_time:
            if hasattr(self.confirm_end_time, 'to_alipay_dict'):
                params['confirm_end_time'] = self.confirm_end_time.to_alipay_dict()
            else:
                params['confirm_end_time'] = self.confirm_end_time
        if self.invite_order_id:
            if hasattr(self.invite_order_id, 'to_alipay_dict'):
                params['invite_order_id'] = self.invite_order_id.to_alipay_dict()
            else:
                params['invite_order_id'] = self.invite_order_id
        if self.plan_rule_list:
            if isinstance(self.plan_rule_list, list):
                for i in range(0, len(self.plan_rule_list)):
                    element = self.plan_rule_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.plan_rule_list[i] = element.to_alipay_dict()
            if hasattr(self.plan_rule_list, 'to_alipay_dict'):
                params['plan_rule_list'] = self.plan_rule_list.to_alipay_dict()
            else:
                params['plan_rule_list'] = self.plan_rule_list
        if self.plat_activity_agreement:
            if hasattr(self.plat_activity_agreement, 'to_alipay_dict'):
                params['plat_activity_agreement'] = self.plat_activity_agreement.to_alipay_dict()
            else:
                params['plat_activity_agreement'] = self.plat_activity_agreement
        if self.plat_activity_id:
            if hasattr(self.plat_activity_id, 'to_alipay_dict'):
                params['plat_activity_id'] = self.plat_activity_id.to_alipay_dict()
            else:
                params['plat_activity_id'] = self.plat_activity_id
        if self.plat_activity_label_type:
            if hasattr(self.plat_activity_label_type, 'to_alipay_dict'):
                params['plat_activity_label_type'] = self.plat_activity_label_type.to_alipay_dict()
            else:
                params['plat_activity_label_type'] = self.plat_activity_label_type
        if self.plat_activity_name:
            if hasattr(self.plat_activity_name, 'to_alipay_dict'):
                params['plat_activity_name'] = self.plat_activity_name.to_alipay_dict()
            else:
                params['plat_activity_name'] = self.plat_activity_name
        if self.plat_activity_rule_desc:
            if hasattr(self.plat_activity_rule_desc, 'to_alipay_dict'):
                params['plat_activity_rule_desc'] = self.plat_activity_rule_desc.to_alipay_dict()
            else:
                params['plat_activity_rule_desc'] = self.plat_activity_rule_desc
        if self.plat_activity_status:
            if hasattr(self.plat_activity_status, 'to_alipay_dict'):
                params['plat_activity_status'] = self.plat_activity_status.to_alipay_dict()
            else:
                params['plat_activity_status'] = self.plat_activity_status
        if self.plat_other_desc:
            if hasattr(self.plat_other_desc, 'to_alipay_dict'):
                params['plat_other_desc'] = self.plat_other_desc.to_alipay_dict()
            else:
                params['plat_other_desc'] = self.plat_other_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityPlanInfo()
        if 'activity_end_time' in d:
            o.activity_end_time = d['activity_end_time']
        if 'activity_start_time' in d:
            o.activity_start_time = d['activity_start_time']
        if 'confirm_end_time' in d:
            o.confirm_end_time = d['confirm_end_time']
        if 'invite_order_id' in d:
            o.invite_order_id = d['invite_order_id']
        if 'plan_rule_list' in d:
            o.plan_rule_list = d['plan_rule_list']
        if 'plat_activity_agreement' in d:
            o.plat_activity_agreement = d['plat_activity_agreement']
        if 'plat_activity_id' in d:
            o.plat_activity_id = d['plat_activity_id']
        if 'plat_activity_label_type' in d:
            o.plat_activity_label_type = d['plat_activity_label_type']
        if 'plat_activity_name' in d:
            o.plat_activity_name = d['plat_activity_name']
        if 'plat_activity_rule_desc' in d:
            o.plat_activity_rule_desc = d['plat_activity_rule_desc']
        if 'plat_activity_status' in d:
            o.plat_activity_status = d['plat_activity_status']
        if 'plat_other_desc' in d:
            o.plat_other_desc = d['plat_other_desc']
        return o


