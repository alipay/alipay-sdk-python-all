#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaTorchreplaycenterreaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaTorchreplaycenterreaQueryResponse, self).__init__()
        self._internal_china_replay_cnt = None
        self._south_and_central_asia_torch_replay_cnt = None
        self._west_and_southeast_asia_torch_replay_cnt = None

    @property
    def internal_china_replay_cnt(self):
        return self._internal_china_replay_cnt

    @internal_china_replay_cnt.setter
    def internal_china_replay_cnt(self, value):
        self._internal_china_replay_cnt = value
    @property
    def south_and_central_asia_torch_replay_cnt(self):
        return self._south_and_central_asia_torch_replay_cnt

    @south_and_central_asia_torch_replay_cnt.setter
    def south_and_central_asia_torch_replay_cnt(self, value):
        self._south_and_central_asia_torch_replay_cnt = value
    @property
    def west_and_southeast_asia_torch_replay_cnt(self):
        return self._west_and_southeast_asia_torch_replay_cnt

    @west_and_southeast_asia_torch_replay_cnt.setter
    def west_and_southeast_asia_torch_replay_cnt(self, value):
        self._west_and_southeast_asia_torch_replay_cnt = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaTorchreplaycenterreaQueryResponse, self).parse_response_content(response_content)
        if 'internal_china_replay_cnt' in response:
            self.internal_china_replay_cnt = response['internal_china_replay_cnt']
        if 'south_and_central_asia_torch_replay_cnt' in response:
            self.south_and_central_asia_torch_replay_cnt = response['south_and_central_asia_torch_replay_cnt']
        if 'west_and_southeast_asia_torch_replay_cnt' in response:
            self.west_and_southeast_asia_torch_replay_cnt = response['west_and_southeast_asia_torch_replay_cnt']
