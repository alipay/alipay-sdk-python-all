#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppletTaskDisplayVO import AppletTaskDisplayVO
from alipay.aop.api.domain.AppletTaskPrizeVO import AppletTaskPrizeVO


class AppletTaskVO(object):

    def __init__(self):
        self._can_access = None
        self._display = None
        self._need_sign_up = None
        self._period_current_complete_num = None
        self._period_total_complete_num = None
        self._prize_list = None
        self._sign_up_begin_time = None
        self._sign_up_end_time = None
        self._task_id = None
        self._task_name = None
        self._task_process_status = None

    @property
    def can_access(self):
        return self._can_access

    @can_access.setter
    def can_access(self, value):
        self._can_access = value
    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, value):
        if isinstance(value, AppletTaskDisplayVO):
            self._display = value
        else:
            self._display = AppletTaskDisplayVO.from_alipay_dict(value)
    @property
    def need_sign_up(self):
        return self._need_sign_up

    @need_sign_up.setter
    def need_sign_up(self, value):
        self._need_sign_up = value
    @property
    def period_current_complete_num(self):
        return self._period_current_complete_num

    @period_current_complete_num.setter
    def period_current_complete_num(self, value):
        self._period_current_complete_num = value
    @property
    def period_total_complete_num(self):
        return self._period_total_complete_num

    @period_total_complete_num.setter
    def period_total_complete_num(self, value):
        self._period_total_complete_num = value
    @property
    def prize_list(self):
        return self._prize_list

    @prize_list.setter
    def prize_list(self, value):
        if isinstance(value, list):
            self._prize_list = list()
            for i in value:
                if isinstance(i, AppletTaskPrizeVO):
                    self._prize_list.append(i)
                else:
                    self._prize_list.append(AppletTaskPrizeVO.from_alipay_dict(i))
    @property
    def sign_up_begin_time(self):
        return self._sign_up_begin_time

    @sign_up_begin_time.setter
    def sign_up_begin_time(self, value):
        self._sign_up_begin_time = value
    @property
    def sign_up_end_time(self):
        return self._sign_up_end_time

    @sign_up_end_time.setter
    def sign_up_end_time(self, value):
        self._sign_up_end_time = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_process_status(self):
        return self._task_process_status

    @task_process_status.setter
    def task_process_status(self, value):
        self._task_process_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_access:
            if hasattr(self.can_access, 'to_alipay_dict'):
                params['can_access'] = self.can_access.to_alipay_dict()
            else:
                params['can_access'] = self.can_access
        if self.display:
            if hasattr(self.display, 'to_alipay_dict'):
                params['display'] = self.display.to_alipay_dict()
            else:
                params['display'] = self.display
        if self.need_sign_up:
            if hasattr(self.need_sign_up, 'to_alipay_dict'):
                params['need_sign_up'] = self.need_sign_up.to_alipay_dict()
            else:
                params['need_sign_up'] = self.need_sign_up
        if self.period_current_complete_num:
            if hasattr(self.period_current_complete_num, 'to_alipay_dict'):
                params['period_current_complete_num'] = self.period_current_complete_num.to_alipay_dict()
            else:
                params['period_current_complete_num'] = self.period_current_complete_num
        if self.period_total_complete_num:
            if hasattr(self.period_total_complete_num, 'to_alipay_dict'):
                params['period_total_complete_num'] = self.period_total_complete_num.to_alipay_dict()
            else:
                params['period_total_complete_num'] = self.period_total_complete_num
        if self.prize_list:
            if isinstance(self.prize_list, list):
                for i in range(0, len(self.prize_list)):
                    element = self.prize_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.prize_list[i] = element.to_alipay_dict()
            if hasattr(self.prize_list, 'to_alipay_dict'):
                params['prize_list'] = self.prize_list.to_alipay_dict()
            else:
                params['prize_list'] = self.prize_list
        if self.sign_up_begin_time:
            if hasattr(self.sign_up_begin_time, 'to_alipay_dict'):
                params['sign_up_begin_time'] = self.sign_up_begin_time.to_alipay_dict()
            else:
                params['sign_up_begin_time'] = self.sign_up_begin_time
        if self.sign_up_end_time:
            if hasattr(self.sign_up_end_time, 'to_alipay_dict'):
                params['sign_up_end_time'] = self.sign_up_end_time.to_alipay_dict()
            else:
                params['sign_up_end_time'] = self.sign_up_end_time
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_process_status:
            if hasattr(self.task_process_status, 'to_alipay_dict'):
                params['task_process_status'] = self.task_process_status.to_alipay_dict()
            else:
                params['task_process_status'] = self.task_process_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppletTaskVO()
        if 'can_access' in d:
            o.can_access = d['can_access']
        if 'display' in d:
            o.display = d['display']
        if 'need_sign_up' in d:
            o.need_sign_up = d['need_sign_up']
        if 'period_current_complete_num' in d:
            o.period_current_complete_num = d['period_current_complete_num']
        if 'period_total_complete_num' in d:
            o.period_total_complete_num = d['period_total_complete_num']
        if 'prize_list' in d:
            o.prize_list = d['prize_list']
        if 'sign_up_begin_time' in d:
            o.sign_up_begin_time = d['sign_up_begin_time']
        if 'sign_up_end_time' in d:
            o.sign_up_end_time = d['sign_up_end_time']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_process_status' in d:
            o.task_process_status = d['task_process_status']
        return o


