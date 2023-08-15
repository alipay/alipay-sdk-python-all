#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaTorchreplayrightstatQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaTorchreplayrightstatQueryResponse, self).__init__()
        self._offline_torch_replay_city_today_cnt = None
        self._offline_torch_replay_city_total_cnt = None
        self._offline_torch_replay_today_cnt = None
        self._offline_torch_replay_total_cnt = None
        self._offline_torchbearer_portrait = None
        self._offline_torchbearer_today_list = None

    @property
    def offline_torch_replay_city_today_cnt(self):
        return self._offline_torch_replay_city_today_cnt

    @offline_torch_replay_city_today_cnt.setter
    def offline_torch_replay_city_today_cnt(self, value):
        self._offline_torch_replay_city_today_cnt = value
    @property
    def offline_torch_replay_city_total_cnt(self):
        return self._offline_torch_replay_city_total_cnt

    @offline_torch_replay_city_total_cnt.setter
    def offline_torch_replay_city_total_cnt(self, value):
        self._offline_torch_replay_city_total_cnt = value
    @property
    def offline_torch_replay_today_cnt(self):
        return self._offline_torch_replay_today_cnt

    @offline_torch_replay_today_cnt.setter
    def offline_torch_replay_today_cnt(self, value):
        self._offline_torch_replay_today_cnt = value
    @property
    def offline_torch_replay_total_cnt(self):
        return self._offline_torch_replay_total_cnt

    @offline_torch_replay_total_cnt.setter
    def offline_torch_replay_total_cnt(self, value):
        self._offline_torch_replay_total_cnt = value
    @property
    def offline_torchbearer_portrait(self):
        return self._offline_torchbearer_portrait

    @offline_torchbearer_portrait.setter
    def offline_torchbearer_portrait(self, value):
        self._offline_torchbearer_portrait = value
    @property
    def offline_torchbearer_today_list(self):
        return self._offline_torchbearer_today_list

    @offline_torchbearer_today_list.setter
    def offline_torchbearer_today_list(self, value):
        self._offline_torchbearer_today_list = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaTorchreplayrightstatQueryResponse, self).parse_response_content(response_content)
        if 'offline_torch_replay_city_today_cnt' in response:
            self.offline_torch_replay_city_today_cnt = response['offline_torch_replay_city_today_cnt']
        if 'offline_torch_replay_city_total_cnt' in response:
            self.offline_torch_replay_city_total_cnt = response['offline_torch_replay_city_total_cnt']
        if 'offline_torch_replay_today_cnt' in response:
            self.offline_torch_replay_today_cnt = response['offline_torch_replay_today_cnt']
        if 'offline_torch_replay_total_cnt' in response:
            self.offline_torch_replay_total_cnt = response['offline_torch_replay_total_cnt']
        if 'offline_torchbearer_portrait' in response:
            self.offline_torchbearer_portrait = response['offline_torchbearer_portrait']
        if 'offline_torchbearer_today_list' in response:
            self.offline_torchbearer_today_list = response['offline_torchbearer_today_list']
