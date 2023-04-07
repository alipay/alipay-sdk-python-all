#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantIndirectPromotaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantIndirectPromotaskQueryResponse, self).__init__()
        self._curent_cnt = None
        self._end_time = None
        self._expire_date = None
        self._finish_time = None
        self._group_mid = None
        self._reward_apply_time = None
        self._reward_code = None
        self._reward_desc = None
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

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantIndirectPromotaskQueryResponse, self).parse_response_content(response_content)
        if 'curent_cnt' in response:
            self.curent_cnt = response['curent_cnt']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'expire_date' in response:
            self.expire_date = response['expire_date']
        if 'finish_time' in response:
            self.finish_time = response['finish_time']
        if 'group_mid' in response:
            self.group_mid = response['group_mid']
        if 'reward_apply_time' in response:
            self.reward_apply_time = response['reward_apply_time']
        if 'reward_code' in response:
            self.reward_code = response['reward_code']
        if 'reward_desc' in response:
            self.reward_desc = response['reward_desc']
        if 'take_time' in response:
            self.take_time = response['take_time']
        if 'target_cnt' in response:
            self.target_cnt = response['target_cnt']
        if 'task_code' in response:
            self.task_code = response['task_code']
        if 'task_id' in response:
            self.task_id = response['task_id']
        if 'task_state' in response:
            self.task_state = response['task_state']
