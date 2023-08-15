#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaTorchreplayrightrealQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaTorchreplayrightrealQueryResponse, self).__init__()
        self._online_torch_replay_city_distribute = None
        self._online_torch_replay_today_cnt = None
        self._online_torch_replay_today_user_cnt = None
        self._online_torch_replay_total_cnt = None
        self._online_torch_replay_total_user_cnt = None

    @property
    def online_torch_replay_city_distribute(self):
        return self._online_torch_replay_city_distribute

    @online_torch_replay_city_distribute.setter
    def online_torch_replay_city_distribute(self, value):
        self._online_torch_replay_city_distribute = value
    @property
    def online_torch_replay_today_cnt(self):
        return self._online_torch_replay_today_cnt

    @online_torch_replay_today_cnt.setter
    def online_torch_replay_today_cnt(self, value):
        self._online_torch_replay_today_cnt = value
    @property
    def online_torch_replay_today_user_cnt(self):
        return self._online_torch_replay_today_user_cnt

    @online_torch_replay_today_user_cnt.setter
    def online_torch_replay_today_user_cnt(self, value):
        self._online_torch_replay_today_user_cnt = value
    @property
    def online_torch_replay_total_cnt(self):
        return self._online_torch_replay_total_cnt

    @online_torch_replay_total_cnt.setter
    def online_torch_replay_total_cnt(self, value):
        self._online_torch_replay_total_cnt = value
    @property
    def online_torch_replay_total_user_cnt(self):
        return self._online_torch_replay_total_user_cnt

    @online_torch_replay_total_user_cnt.setter
    def online_torch_replay_total_user_cnt(self, value):
        self._online_torch_replay_total_user_cnt = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaTorchreplayrightrealQueryResponse, self).parse_response_content(response_content)
        if 'online_torch_replay_city_distribute' in response:
            self.online_torch_replay_city_distribute = response['online_torch_replay_city_distribute']
        if 'online_torch_replay_today_cnt' in response:
            self.online_torch_replay_today_cnt = response['online_torch_replay_today_cnt']
        if 'online_torch_replay_today_user_cnt' in response:
            self.online_torch_replay_today_user_cnt = response['online_torch_replay_today_user_cnt']
        if 'online_torch_replay_total_cnt' in response:
            self.online_torch_replay_total_cnt = response['online_torch_replay_total_cnt']
        if 'online_torch_replay_total_user_cnt' in response:
            self.online_torch_replay_total_user_cnt = response['online_torch_replay_total_user_cnt']
