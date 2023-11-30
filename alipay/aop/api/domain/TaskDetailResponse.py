#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrizeResponse import PrizeResponse


class TaskDetailResponse(object):

    def __init__(self):
        self._creator = None
        self._creator_open_id = None
        self._merchant_pid = None
        self._prize_response = None
        self._second_merchant_appid = None
        self._task_condition = None
        self._task_contract_period = None
        self._task_end = None
        self._task_free = None
        self._task_id = None
        self._task_join_count = None
        self._task_name = None
        self._task_start = None
        self._task_status = None
        self._task_title = None
        self._task_type = None

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def creator_open_id(self):
        return self._creator_open_id

    @creator_open_id.setter
    def creator_open_id(self, value):
        self._creator_open_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def prize_response(self):
        return self._prize_response

    @prize_response.setter
    def prize_response(self, value):
        if isinstance(value, PrizeResponse):
            self._prize_response = value
        else:
            self._prize_response = PrizeResponse.from_alipay_dict(value)
    @property
    def second_merchant_appid(self):
        return self._second_merchant_appid

    @second_merchant_appid.setter
    def second_merchant_appid(self, value):
        self._second_merchant_appid = value
    @property
    def task_condition(self):
        return self._task_condition

    @task_condition.setter
    def task_condition(self, value):
        self._task_condition = value
    @property
    def task_contract_period(self):
        return self._task_contract_period

    @task_contract_period.setter
    def task_contract_period(self, value):
        self._task_contract_period = value
    @property
    def task_end(self):
        return self._task_end

    @task_end.setter
    def task_end(self, value):
        self._task_end = value
    @property
    def task_free(self):
        return self._task_free

    @task_free.setter
    def task_free(self, value):
        self._task_free = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_join_count(self):
        return self._task_join_count

    @task_join_count.setter
    def task_join_count(self, value):
        self._task_join_count = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def task_start(self):
        return self._task_start

    @task_start.setter
    def task_start(self, value):
        self._task_start = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value
    @property
    def task_title(self):
        return self._task_title

    @task_title.setter
    def task_title(self, value):
        self._task_title = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.creator_open_id:
            if hasattr(self.creator_open_id, 'to_alipay_dict'):
                params['creator_open_id'] = self.creator_open_id.to_alipay_dict()
            else:
                params['creator_open_id'] = self.creator_open_id
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.prize_response:
            if hasattr(self.prize_response, 'to_alipay_dict'):
                params['prize_response'] = self.prize_response.to_alipay_dict()
            else:
                params['prize_response'] = self.prize_response
        if self.second_merchant_appid:
            if hasattr(self.second_merchant_appid, 'to_alipay_dict'):
                params['second_merchant_appid'] = self.second_merchant_appid.to_alipay_dict()
            else:
                params['second_merchant_appid'] = self.second_merchant_appid
        if self.task_condition:
            if hasattr(self.task_condition, 'to_alipay_dict'):
                params['task_condition'] = self.task_condition.to_alipay_dict()
            else:
                params['task_condition'] = self.task_condition
        if self.task_contract_period:
            if hasattr(self.task_contract_period, 'to_alipay_dict'):
                params['task_contract_period'] = self.task_contract_period.to_alipay_dict()
            else:
                params['task_contract_period'] = self.task_contract_period
        if self.task_end:
            if hasattr(self.task_end, 'to_alipay_dict'):
                params['task_end'] = self.task_end.to_alipay_dict()
            else:
                params['task_end'] = self.task_end
        if self.task_free:
            if hasattr(self.task_free, 'to_alipay_dict'):
                params['task_free'] = self.task_free.to_alipay_dict()
            else:
                params['task_free'] = self.task_free
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.task_join_count:
            if hasattr(self.task_join_count, 'to_alipay_dict'):
                params['task_join_count'] = self.task_join_count.to_alipay_dict()
            else:
                params['task_join_count'] = self.task_join_count
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.task_start:
            if hasattr(self.task_start, 'to_alipay_dict'):
                params['task_start'] = self.task_start.to_alipay_dict()
            else:
                params['task_start'] = self.task_start
        if self.task_status:
            if hasattr(self.task_status, 'to_alipay_dict'):
                params['task_status'] = self.task_status.to_alipay_dict()
            else:
                params['task_status'] = self.task_status
        if self.task_title:
            if hasattr(self.task_title, 'to_alipay_dict'):
                params['task_title'] = self.task_title.to_alipay_dict()
            else:
                params['task_title'] = self.task_title
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
        o = TaskDetailResponse()
        if 'creator' in d:
            o.creator = d['creator']
        if 'creator_open_id' in d:
            o.creator_open_id = d['creator_open_id']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'prize_response' in d:
            o.prize_response = d['prize_response']
        if 'second_merchant_appid' in d:
            o.second_merchant_appid = d['second_merchant_appid']
        if 'task_condition' in d:
            o.task_condition = d['task_condition']
        if 'task_contract_period' in d:
            o.task_contract_period = d['task_contract_period']
        if 'task_end' in d:
            o.task_end = d['task_end']
        if 'task_free' in d:
            o.task_free = d['task_free']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'task_join_count' in d:
            o.task_join_count = d['task_join_count']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'task_start' in d:
            o.task_start = d['task_start']
        if 'task_status' in d:
            o.task_status = d['task_status']
        if 'task_title' in d:
            o.task_title = d['task_title']
        if 'task_type' in d:
            o.task_type = d['task_type']
        return o


