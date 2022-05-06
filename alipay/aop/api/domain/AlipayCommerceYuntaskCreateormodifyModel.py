#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PlanInfo import PlanInfo


class AlipayCommerceYuntaskCreateormodifyModel(object):

    def __init__(self):
        self._applet_id = None
        self._create_biz_no = None
        self._funder_id = None
        self._funder_type = None
        self._incentive = None
        self._incentive_mode = None
        self._incentive_rule = None
        self._merchant_pid = None
        self._operate_user_id = None
        self._organizer_id = None
        self._organizer_name = None
        self._organizer_type = None
        self._plan_info = None
        self._task_desc = None
        self._task_end_time = None
        self._task_name = None
        self._task_start_time = None
        self._task_template_id = None
        self._task_type = None

    @property
    def applet_id(self):
        return self._applet_id

    @applet_id.setter
    def applet_id(self, value):
        self._applet_id = value
    @property
    def create_biz_no(self):
        return self._create_biz_no

    @create_biz_no.setter
    def create_biz_no(self, value):
        self._create_biz_no = value
    @property
    def funder_id(self):
        return self._funder_id

    @funder_id.setter
    def funder_id(self, value):
        self._funder_id = value
    @property
    def funder_type(self):
        return self._funder_type

    @funder_type.setter
    def funder_type(self, value):
        self._funder_type = value
    @property
    def incentive(self):
        return self._incentive

    @incentive.setter
    def incentive(self, value):
        self._incentive = value
    @property
    def incentive_mode(self):
        return self._incentive_mode

    @incentive_mode.setter
    def incentive_mode(self, value):
        self._incentive_mode = value
    @property
    def incentive_rule(self):
        return self._incentive_rule

    @incentive_rule.setter
    def incentive_rule(self, value):
        self._incentive_rule = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def operate_user_id(self):
        return self._operate_user_id

    @operate_user_id.setter
    def operate_user_id(self, value):
        self._operate_user_id = value
    @property
    def organizer_id(self):
        return self._organizer_id

    @organizer_id.setter
    def organizer_id(self, value):
        self._organizer_id = value
    @property
    def organizer_name(self):
        return self._organizer_name

    @organizer_name.setter
    def organizer_name(self, value):
        self._organizer_name = value
    @property
    def organizer_type(self):
        return self._organizer_type

    @organizer_type.setter
    def organizer_type(self, value):
        self._organizer_type = value
    @property
    def plan_info(self):
        return self._plan_info

    @plan_info.setter
    def plan_info(self, value):
        if isinstance(value, PlanInfo):
            self._plan_info = value
        else:
            self._plan_info = PlanInfo.from_alipay_dict(value)
    @property
    def task_desc(self):
        return self._task_desc

    @task_desc.setter
    def task_desc(self, value):
        self._task_desc = value
    @property
    def task_end_time(self):
        return self._task_end_time

    @task_end_time.setter
    def task_end_time(self, value):
        self._task_end_time = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_start_time(self):
        return self._task_start_time

    @task_start_time.setter
    def task_start_time(self, value):
        self._task_start_time = value
    @property
    def task_template_id(self):
        return self._task_template_id

    @task_template_id.setter
    def task_template_id(self, value):
        self._task_template_id = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.applet_id:
            if hasattr(self.applet_id, 'to_alipay_dict'):
                params['applet_id'] = self.applet_id.to_alipay_dict()
            else:
                params['applet_id'] = self.applet_id
        if self.create_biz_no:
            if hasattr(self.create_biz_no, 'to_alipay_dict'):
                params['create_biz_no'] = self.create_biz_no.to_alipay_dict()
            else:
                params['create_biz_no'] = self.create_biz_no
        if self.funder_id:
            if hasattr(self.funder_id, 'to_alipay_dict'):
                params['funder_id'] = self.funder_id.to_alipay_dict()
            else:
                params['funder_id'] = self.funder_id
        if self.funder_type:
            if hasattr(self.funder_type, 'to_alipay_dict'):
                params['funder_type'] = self.funder_type.to_alipay_dict()
            else:
                params['funder_type'] = self.funder_type
        if self.incentive:
            if hasattr(self.incentive, 'to_alipay_dict'):
                params['incentive'] = self.incentive.to_alipay_dict()
            else:
                params['incentive'] = self.incentive
        if self.incentive_mode:
            if hasattr(self.incentive_mode, 'to_alipay_dict'):
                params['incentive_mode'] = self.incentive_mode.to_alipay_dict()
            else:
                params['incentive_mode'] = self.incentive_mode
        if self.incentive_rule:
            if hasattr(self.incentive_rule, 'to_alipay_dict'):
                params['incentive_rule'] = self.incentive_rule.to_alipay_dict()
            else:
                params['incentive_rule'] = self.incentive_rule
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.operate_user_id:
            if hasattr(self.operate_user_id, 'to_alipay_dict'):
                params['operate_user_id'] = self.operate_user_id.to_alipay_dict()
            else:
                params['operate_user_id'] = self.operate_user_id
        if self.organizer_id:
            if hasattr(self.organizer_id, 'to_alipay_dict'):
                params['organizer_id'] = self.organizer_id.to_alipay_dict()
            else:
                params['organizer_id'] = self.organizer_id
        if self.organizer_name:
            if hasattr(self.organizer_name, 'to_alipay_dict'):
                params['organizer_name'] = self.organizer_name.to_alipay_dict()
            else:
                params['organizer_name'] = self.organizer_name
        if self.organizer_type:
            if hasattr(self.organizer_type, 'to_alipay_dict'):
                params['organizer_type'] = self.organizer_type.to_alipay_dict()
            else:
                params['organizer_type'] = self.organizer_type
        if self.plan_info:
            if hasattr(self.plan_info, 'to_alipay_dict'):
                params['plan_info'] = self.plan_info.to_alipay_dict()
            else:
                params['plan_info'] = self.plan_info
        if self.task_desc:
            if hasattr(self.task_desc, 'to_alipay_dict'):
                params['task_desc'] = self.task_desc.to_alipay_dict()
            else:
                params['task_desc'] = self.task_desc
        if self.task_end_time:
            if hasattr(self.task_end_time, 'to_alipay_dict'):
                params['task_end_time'] = self.task_end_time.to_alipay_dict()
            else:
                params['task_end_time'] = self.task_end_time
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_start_time:
            if hasattr(self.task_start_time, 'to_alipay_dict'):
                params['task_start_time'] = self.task_start_time.to_alipay_dict()
            else:
                params['task_start_time'] = self.task_start_time
        if self.task_template_id:
            if hasattr(self.task_template_id, 'to_alipay_dict'):
                params['task_template_id'] = self.task_template_id.to_alipay_dict()
            else:
                params['task_template_id'] = self.task_template_id
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceYuntaskCreateormodifyModel()
        if 'applet_id' in d:
            o.applet_id = d['applet_id']
        if 'create_biz_no' in d:
            o.create_biz_no = d['create_biz_no']
        if 'funder_id' in d:
            o.funder_id = d['funder_id']
        if 'funder_type' in d:
            o.funder_type = d['funder_type']
        if 'incentive' in d:
            o.incentive = d['incentive']
        if 'incentive_mode' in d:
            o.incentive_mode = d['incentive_mode']
        if 'incentive_rule' in d:
            o.incentive_rule = d['incentive_rule']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'operate_user_id' in d:
            o.operate_user_id = d['operate_user_id']
        if 'organizer_id' in d:
            o.organizer_id = d['organizer_id']
        if 'organizer_name' in d:
            o.organizer_name = d['organizer_name']
        if 'organizer_type' in d:
            o.organizer_type = d['organizer_type']
        if 'plan_info' in d:
            o.plan_info = d['plan_info']
        if 'task_desc' in d:
            o.task_desc = d['task_desc']
        if 'task_end_time' in d:
            o.task_end_time = d['task_end_time']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_start_time' in d:
            o.task_start_time = d['task_start_time']
        if 'task_template_id' in d:
            o.task_template_id = d['task_template_id']
        if 'task_type' in d:
            o.task_type = d['task_type']
        return o


