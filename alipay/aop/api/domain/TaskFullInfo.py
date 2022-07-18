#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrizeBaseInfo import PrizeBaseInfo
from alipay.aop.api.domain.TaskBaseInfo import TaskBaseInfo
from alipay.aop.api.domain.TaskMaterialInfo import TaskMaterialInfo
from alipay.aop.api.domain.PrizeBaseInfo import PrizeBaseInfo


class TaskFullInfo(object):

    def __init__(self):
        self._access_limit_count = None
        self._last_acc_time = None
        self._last_complete_time = None
        self._last_receive_expire_time = None
        self._last_signup_expire_time = None
        self._last_signup_time = None
        self._need_sign_up = None
        self._period_current_complete_num = None
        self._period_total_complete_num = None
        self._periodic_accessed_num = None
        self._periodic_dimension = None
        self._prize_detail_list = None
        self._send_camp_trigger_type = None
        self._task_base_info = None
        self._task_id = None
        self._task_material = None
        self._task_process_status = None
        self._valid_prize_list = None

    @property
    def access_limit_count(self):
        return self._access_limit_count

    @access_limit_count.setter
    def access_limit_count(self, value):
        self._access_limit_count = value
    @property
    def last_acc_time(self):
        return self._last_acc_time

    @last_acc_time.setter
    def last_acc_time(self, value):
        self._last_acc_time = value
    @property
    def last_complete_time(self):
        return self._last_complete_time

    @last_complete_time.setter
    def last_complete_time(self, value):
        self._last_complete_time = value
    @property
    def last_receive_expire_time(self):
        return self._last_receive_expire_time

    @last_receive_expire_time.setter
    def last_receive_expire_time(self, value):
        self._last_receive_expire_time = value
    @property
    def last_signup_expire_time(self):
        return self._last_signup_expire_time

    @last_signup_expire_time.setter
    def last_signup_expire_time(self, value):
        self._last_signup_expire_time = value
    @property
    def last_signup_time(self):
        return self._last_signup_time

    @last_signup_time.setter
    def last_signup_time(self, value):
        self._last_signup_time = value
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
    def periodic_accessed_num(self):
        return self._periodic_accessed_num

    @periodic_accessed_num.setter
    def periodic_accessed_num(self, value):
        self._periodic_accessed_num = value
    @property
    def periodic_dimension(self):
        return self._periodic_dimension

    @periodic_dimension.setter
    def periodic_dimension(self, value):
        self._periodic_dimension = value
    @property
    def prize_detail_list(self):
        return self._prize_detail_list

    @prize_detail_list.setter
    def prize_detail_list(self, value):
        if isinstance(value, list):
            self._prize_detail_list = list()
            for i in value:
                if isinstance(i, PrizeBaseInfo):
                    self._prize_detail_list.append(i)
                else:
                    self._prize_detail_list.append(PrizeBaseInfo.from_alipay_dict(i))
    @property
    def send_camp_trigger_type(self):
        return self._send_camp_trigger_type

    @send_camp_trigger_type.setter
    def send_camp_trigger_type(self, value):
        self._send_camp_trigger_type = value
    @property
    def task_base_info(self):
        return self._task_base_info

    @task_base_info.setter
    def task_base_info(self, value):
        if isinstance(value, TaskBaseInfo):
            self._task_base_info = value
        else:
            self._task_base_info = TaskBaseInfo.from_alipay_dict(value)
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_material(self):
        return self._task_material

    @task_material.setter
    def task_material(self, value):
        if isinstance(value, TaskMaterialInfo):
            self._task_material = value
        else:
            self._task_material = TaskMaterialInfo.from_alipay_dict(value)
    @property
    def task_process_status(self):
        return self._task_process_status

    @task_process_status.setter
    def task_process_status(self, value):
        self._task_process_status = value
    @property
    def valid_prize_list(self):
        return self._valid_prize_list

    @valid_prize_list.setter
    def valid_prize_list(self, value):
        if isinstance(value, list):
            self._valid_prize_list = list()
            for i in value:
                if isinstance(i, PrizeBaseInfo):
                    self._valid_prize_list.append(i)
                else:
                    self._valid_prize_list.append(PrizeBaseInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.access_limit_count:
            if hasattr(self.access_limit_count, 'to_alipay_dict'):
                params['access_limit_count'] = self.access_limit_count.to_alipay_dict()
            else:
                params['access_limit_count'] = self.access_limit_count
        if self.last_acc_time:
            if hasattr(self.last_acc_time, 'to_alipay_dict'):
                params['last_acc_time'] = self.last_acc_time.to_alipay_dict()
            else:
                params['last_acc_time'] = self.last_acc_time
        if self.last_complete_time:
            if hasattr(self.last_complete_time, 'to_alipay_dict'):
                params['last_complete_time'] = self.last_complete_time.to_alipay_dict()
            else:
                params['last_complete_time'] = self.last_complete_time
        if self.last_receive_expire_time:
            if hasattr(self.last_receive_expire_time, 'to_alipay_dict'):
                params['last_receive_expire_time'] = self.last_receive_expire_time.to_alipay_dict()
            else:
                params['last_receive_expire_time'] = self.last_receive_expire_time
        if self.last_signup_expire_time:
            if hasattr(self.last_signup_expire_time, 'to_alipay_dict'):
                params['last_signup_expire_time'] = self.last_signup_expire_time.to_alipay_dict()
            else:
                params['last_signup_expire_time'] = self.last_signup_expire_time
        if self.last_signup_time:
            if hasattr(self.last_signup_time, 'to_alipay_dict'):
                params['last_signup_time'] = self.last_signup_time.to_alipay_dict()
            else:
                params['last_signup_time'] = self.last_signup_time
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
        if self.periodic_accessed_num:
            if hasattr(self.periodic_accessed_num, 'to_alipay_dict'):
                params['periodic_accessed_num'] = self.periodic_accessed_num.to_alipay_dict()
            else:
                params['periodic_accessed_num'] = self.periodic_accessed_num
        if self.periodic_dimension:
            if hasattr(self.periodic_dimension, 'to_alipay_dict'):
                params['periodic_dimension'] = self.periodic_dimension.to_alipay_dict()
            else:
                params['periodic_dimension'] = self.periodic_dimension
        if self.prize_detail_list:
            if isinstance(self.prize_detail_list, list):
                for i in range(0, len(self.prize_detail_list)):
                    element = self.prize_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.prize_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.prize_detail_list, 'to_alipay_dict'):
                params['prize_detail_list'] = self.prize_detail_list.to_alipay_dict()
            else:
                params['prize_detail_list'] = self.prize_detail_list
        if self.send_camp_trigger_type:
            if hasattr(self.send_camp_trigger_type, 'to_alipay_dict'):
                params['send_camp_trigger_type'] = self.send_camp_trigger_type.to_alipay_dict()
            else:
                params['send_camp_trigger_type'] = self.send_camp_trigger_type
        if self.task_base_info:
            if hasattr(self.task_base_info, 'to_alipay_dict'):
                params['task_base_info'] = self.task_base_info.to_alipay_dict()
            else:
                params['task_base_info'] = self.task_base_info
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.task_material:
            if hasattr(self.task_material, 'to_alipay_dict'):
                params['task_material'] = self.task_material.to_alipay_dict()
            else:
                params['task_material'] = self.task_material
        if self.task_process_status:
            if hasattr(self.task_process_status, 'to_alipay_dict'):
                params['task_process_status'] = self.task_process_status.to_alipay_dict()
            else:
                params['task_process_status'] = self.task_process_status
        if self.valid_prize_list:
            if isinstance(self.valid_prize_list, list):
                for i in range(0, len(self.valid_prize_list)):
                    element = self.valid_prize_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.valid_prize_list[i] = element.to_alipay_dict()
            if hasattr(self.valid_prize_list, 'to_alipay_dict'):
                params['valid_prize_list'] = self.valid_prize_list.to_alipay_dict()
            else:
                params['valid_prize_list'] = self.valid_prize_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskFullInfo()
        if 'access_limit_count' in d:
            o.access_limit_count = d['access_limit_count']
        if 'last_acc_time' in d:
            o.last_acc_time = d['last_acc_time']
        if 'last_complete_time' in d:
            o.last_complete_time = d['last_complete_time']
        if 'last_receive_expire_time' in d:
            o.last_receive_expire_time = d['last_receive_expire_time']
        if 'last_signup_expire_time' in d:
            o.last_signup_expire_time = d['last_signup_expire_time']
        if 'last_signup_time' in d:
            o.last_signup_time = d['last_signup_time']
        if 'need_sign_up' in d:
            o.need_sign_up = d['need_sign_up']
        if 'period_current_complete_num' in d:
            o.period_current_complete_num = d['period_current_complete_num']
        if 'period_total_complete_num' in d:
            o.period_total_complete_num = d['period_total_complete_num']
        if 'periodic_accessed_num' in d:
            o.periodic_accessed_num = d['periodic_accessed_num']
        if 'periodic_dimension' in d:
            o.periodic_dimension = d['periodic_dimension']
        if 'prize_detail_list' in d:
            o.prize_detail_list = d['prize_detail_list']
        if 'send_camp_trigger_type' in d:
            o.send_camp_trigger_type = d['send_camp_trigger_type']
        if 'task_base_info' in d:
            o.task_base_info = d['task_base_info']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'task_material' in d:
            o.task_material = d['task_material']
        if 'task_process_status' in d:
            o.task_process_status = d['task_process_status']
        if 'valid_prize_list' in d:
            o.valid_prize_list = d['valid_prize_list']
        return o


