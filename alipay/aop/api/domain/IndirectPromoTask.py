#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndirectPromoTask(object):

    def __init__(self):
        self._curent_cnt = None
        self._end_time = None
        self._expire_date = None
        self._finish_time = None
        self._group_mid = None
        self._reward_apply_time = None
        self._reward_code = None
        self._reward_desc = None
        self._source_pid = None
        self._take_time = None
        self._target_cnt = None
        self._task_code = None
        self._task_id = None
        self._task_state = None

    @property
    def curent_cnt(self):
        return self._curent_cnt

    @curent_cnt.setter
    def curent_cnt(self, value):
        self._curent_cnt = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def group_mid(self):
        return self._group_mid

    @group_mid.setter
    def group_mid(self, value):
        self._group_mid = value
    @property
    def reward_apply_time(self):
        return self._reward_apply_time

    @reward_apply_time.setter
    def reward_apply_time(self, value):
        self._reward_apply_time = value
    @property
    def reward_code(self):
        return self._reward_code

    @reward_code.setter
    def reward_code(self, value):
        self._reward_code = value
    @property
    def reward_desc(self):
        return self._reward_desc

    @reward_desc.setter
    def reward_desc(self, value):
        self._reward_desc = value
    @property
    def source_pid(self):
        return self._source_pid

    @source_pid.setter
    def source_pid(self, value):
        self._source_pid = value
    @property
    def take_time(self):
        return self._take_time

    @take_time.setter
    def take_time(self, value):
        self._take_time = value
    @property
    def target_cnt(self):
        return self._target_cnt

    @target_cnt.setter
    def target_cnt(self, value):
        self._target_cnt = value
    @property
    def task_code(self):
        return self._task_code

    @task_code.setter
    def task_code(self, value):
        self._task_code = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_state(self):
        return self._task_state

    @task_state.setter
    def task_state(self, value):
        self._task_state = value


    def to_alipay_dict(self):
        params = dict()
        if self.curent_cnt:
            if hasattr(self.curent_cnt, 'to_alipay_dict'):
                params['curent_cnt'] = self.curent_cnt.to_alipay_dict()
            else:
                params['curent_cnt'] = self.curent_cnt
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.finish_time:
            if hasattr(self.finish_time, 'to_alipay_dict'):
                params['finish_time'] = self.finish_time.to_alipay_dict()
            else:
                params['finish_time'] = self.finish_time
        if self.group_mid:
            if hasattr(self.group_mid, 'to_alipay_dict'):
                params['group_mid'] = self.group_mid.to_alipay_dict()
            else:
                params['group_mid'] = self.group_mid
        if self.reward_apply_time:
            if hasattr(self.reward_apply_time, 'to_alipay_dict'):
                params['reward_apply_time'] = self.reward_apply_time.to_alipay_dict()
            else:
                params['reward_apply_time'] = self.reward_apply_time
        if self.reward_code:
            if hasattr(self.reward_code, 'to_alipay_dict'):
                params['reward_code'] = self.reward_code.to_alipay_dict()
            else:
                params['reward_code'] = self.reward_code
        if self.reward_desc:
            if hasattr(self.reward_desc, 'to_alipay_dict'):
                params['reward_desc'] = self.reward_desc.to_alipay_dict()
            else:
                params['reward_desc'] = self.reward_desc
        if self.source_pid:
            if hasattr(self.source_pid, 'to_alipay_dict'):
                params['source_pid'] = self.source_pid.to_alipay_dict()
            else:
                params['source_pid'] = self.source_pid
        if self.take_time:
            if hasattr(self.take_time, 'to_alipay_dict'):
                params['take_time'] = self.take_time.to_alipay_dict()
            else:
                params['take_time'] = self.take_time
        if self.target_cnt:
            if hasattr(self.target_cnt, 'to_alipay_dict'):
                params['target_cnt'] = self.target_cnt.to_alipay_dict()
            else:
                params['target_cnt'] = self.target_cnt
        if self.task_code:
            if hasattr(self.task_code, 'to_alipay_dict'):
                params['task_code'] = self.task_code.to_alipay_dict()
            else:
                params['task_code'] = self.task_code
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.task_state:
            if hasattr(self.task_state, 'to_alipay_dict'):
                params['task_state'] = self.task_state.to_alipay_dict()
            else:
                params['task_state'] = self.task_state
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndirectPromoTask()
        if 'curent_cnt' in d:
            o.curent_cnt = d['curent_cnt']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'group_mid' in d:
            o.group_mid = d['group_mid']
        if 'reward_apply_time' in d:
            o.reward_apply_time = d['reward_apply_time']
        if 'reward_code' in d:
            o.reward_code = d['reward_code']
        if 'reward_desc' in d:
            o.reward_desc = d['reward_desc']
        if 'source_pid' in d:
            o.source_pid = d['source_pid']
        if 'take_time' in d:
            o.take_time = d['take_time']
        if 'target_cnt' in d:
            o.target_cnt = d['target_cnt']
        if 'task_code' in d:
            o.task_code = d['task_code']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'task_state' in d:
            o.task_state = d['task_state']
        return o


