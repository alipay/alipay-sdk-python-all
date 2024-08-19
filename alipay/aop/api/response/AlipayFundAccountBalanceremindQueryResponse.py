#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccountModelDTO import AccountModelDTO
from alipay.aop.api.domain.RemindPersonInfoDTO import RemindPersonInfoDTO
from alipay.aop.api.domain.ScheduleInfoDTO import ScheduleInfoDTO


class AlipayFundAccountBalanceremindQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAccountBalanceremindQueryResponse, self).__init__()
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

    def parse_response_content(self, response_content):
        response = super(AlipayFundAccountBalanceremindQueryResponse, self).parse_response_content(response_content)
        if 'max_remind_balance' in response:
            self.max_remind_balance = response['max_remind_balance']
        if 'min_remind_balance' in response:
            self.min_remind_balance = response['min_remind_balance']
        if 'monitor_user_id' in response:
            self.monitor_user_id = response['monitor_user_id']
        if 'monitor_user_open_id' in response:
            self.monitor_user_open_id = response['monitor_user_open_id']
        if 'plan_id' in response:
            self.plan_id = response['plan_id']
        if 'plan_name' in response:
            self.plan_name = response['plan_name']
        if 'plan_version' in response:
            self.plan_version = response['plan_version']
        if 'remind_account_info' in response:
            self.remind_account_info = response['remind_account_info']
        if 'remind_person_list' in response:
            self.remind_person_list = response['remind_person_list']
        if 'schedule_info_list' in response:
            self.schedule_info_list = response['schedule_info_list']
        if 'status' in response:
            self.status = response['status']
        if 'third_biz_scene' in response:
            self.third_biz_scene = response['third_biz_scene']
