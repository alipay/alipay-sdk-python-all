#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccountModelDTO import AccountModelDTO
from alipay.aop.api.domain.RemindPersonInfoDTO import RemindPersonInfoDTO
from alipay.aop.api.domain.ScheduleInfoDTO import ScheduleInfoDTO


class BalanceRemindPlanDTO(object):

    def __init__(self):
        self._max_remind_balance = None
        self._min_remind_balance = None
        self._monitor_user_id = None
        self._monitor_user_open_id = None
        self._plan_id = None
        self._plan_name = None
        self._plan_version = None
        self._remind_account_info = None
        self._remind_person_list = None
        self._schedule_info_list = None
        self._status = None
        self._third_biz_scene = None

    @property
    def max_remind_balance(self):
        return self._max_remind_balance

    @max_remind_balance.setter
    def max_remind_balance(self, value):
        self._max_remind_balance = value
    @property
    def min_remind_balance(self):
        return self._min_remind_balance

    @min_remind_balance.setter
    def min_remind_balance(self, value):
        self._min_remind_balance = value
    @property
    def monitor_user_id(self):
        return self._monitor_user_id

    @monitor_user_id.setter
    def monitor_user_id(self, value):
        self._monitor_user_id = value
    @property
    def monitor_user_open_id(self):
        return self._monitor_user_open_id

    @monitor_user_open_id.setter
    def monitor_user_open_id(self, value):
        self._monitor_user_open_id = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def plan_version(self):
        return self._plan_version

    @plan_version.setter
    def plan_version(self, value):
        self._plan_version = value
    @property
    def remind_account_info(self):
        return self._remind_account_info

    @remind_account_info.setter
    def remind_account_info(self, value):
        if isinstance(value, AccountModelDTO):
            self._remind_account_info = value
        else:
            self._remind_account_info = AccountModelDTO.from_alipay_dict(value)
    @property
    def remind_person_list(self):
        return self._remind_person_list

    @remind_person_list.setter
    def remind_person_list(self, value):
        if isinstance(value, list):
            self._remind_person_list = list()
            for i in value:
                if isinstance(i, RemindPersonInfoDTO):
                    self._remind_person_list.append(i)
                else:
                    self._remind_person_list.append(RemindPersonInfoDTO.from_alipay_dict(i))
    @property
    def schedule_info_list(self):
        return self._schedule_info_list

    @schedule_info_list.setter
    def schedule_info_list(self, value):
        if isinstance(value, list):
            self._schedule_info_list = list()
            for i in value:
                if isinstance(i, ScheduleInfoDTO):
                    self._schedule_info_list.append(i)
                else:
                    self._schedule_info_list.append(ScheduleInfoDTO.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def third_biz_scene(self):
        return self._third_biz_scene

    @third_biz_scene.setter
    def third_biz_scene(self, value):
        self._third_biz_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_remind_balance:
            if hasattr(self.max_remind_balance, 'to_alipay_dict'):
                params['max_remind_balance'] = self.max_remind_balance.to_alipay_dict()
            else:
                params['max_remind_balance'] = self.max_remind_balance
        if self.min_remind_balance:
            if hasattr(self.min_remind_balance, 'to_alipay_dict'):
                params['min_remind_balance'] = self.min_remind_balance.to_alipay_dict()
            else:
                params['min_remind_balance'] = self.min_remind_balance
        if self.monitor_user_id:
            if hasattr(self.monitor_user_id, 'to_alipay_dict'):
                params['monitor_user_id'] = self.monitor_user_id.to_alipay_dict()
            else:
                params['monitor_user_id'] = self.monitor_user_id
        if self.monitor_user_open_id:
            if hasattr(self.monitor_user_open_id, 'to_alipay_dict'):
                params['monitor_user_open_id'] = self.monitor_user_open_id.to_alipay_dict()
            else:
                params['monitor_user_open_id'] = self.monitor_user_open_id
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
        if self.plan_version:
            if hasattr(self.plan_version, 'to_alipay_dict'):
                params['plan_version'] = self.plan_version.to_alipay_dict()
            else:
                params['plan_version'] = self.plan_version
        if self.remind_account_info:
            if hasattr(self.remind_account_info, 'to_alipay_dict'):
                params['remind_account_info'] = self.remind_account_info.to_alipay_dict()
            else:
                params['remind_account_info'] = self.remind_account_info
        if self.remind_person_list:
            if isinstance(self.remind_person_list, list):
                for i in range(0, len(self.remind_person_list)):
                    element = self.remind_person_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.remind_person_list[i] = element.to_alipay_dict()
            if hasattr(self.remind_person_list, 'to_alipay_dict'):
                params['remind_person_list'] = self.remind_person_list.to_alipay_dict()
            else:
                params['remind_person_list'] = self.remind_person_list
        if self.schedule_info_list:
            if isinstance(self.schedule_info_list, list):
                for i in range(0, len(self.schedule_info_list)):
                    element = self.schedule_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.schedule_info_list[i] = element.to_alipay_dict()
            if hasattr(self.schedule_info_list, 'to_alipay_dict'):
                params['schedule_info_list'] = self.schedule_info_list.to_alipay_dict()
            else:
                params['schedule_info_list'] = self.schedule_info_list
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.third_biz_scene:
            if hasattr(self.third_biz_scene, 'to_alipay_dict'):
                params['third_biz_scene'] = self.third_biz_scene.to_alipay_dict()
            else:
                params['third_biz_scene'] = self.third_biz_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BalanceRemindPlanDTO()
        if 'max_remind_balance' in d:
            o.max_remind_balance = d['max_remind_balance']
        if 'min_remind_balance' in d:
            o.min_remind_balance = d['min_remind_balance']
        if 'monitor_user_id' in d:
            o.monitor_user_id = d['monitor_user_id']
        if 'monitor_user_open_id' in d:
            o.monitor_user_open_id = d['monitor_user_open_id']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'plan_version' in d:
            o.plan_version = d['plan_version']
        if 'remind_account_info' in d:
            o.remind_account_info = d['remind_account_info']
        if 'remind_person_list' in d:
            o.remind_person_list = d['remind_person_list']
        if 'schedule_info_list' in d:
            o.schedule_info_list = d['schedule_info_list']
        if 'status' in d:
            o.status = d['status']
        if 'third_biz_scene' in d:
            o.third_biz_scene = d['third_biz_scene']
        return o


