#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RewardDTO import RewardDTO


class AlipaySocialAntforestWelfareforestTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestWelfareforestTransferResponse, self).__init__()
        self._effect_energy = None
        self._idempotent = None
        self._reward_code_list_after_water = None
        self._reward_info_list = None
        self._rewarded_code_list = None

    @property
    def effect_energy(self):
        return self._effect_energy

    @effect_energy.setter
    def effect_energy(self, value):
        self._effect_energy = value
    @property
    def idempotent(self):
        return self._idempotent

    @idempotent.setter
    def idempotent(self, value):
        self._idempotent = value
    @property
    def reward_code_list_after_water(self):
        return self._reward_code_list_after_water

    @reward_code_list_after_water.setter
    def reward_code_list_after_water(self, value):
        if isinstance(value, list):
            self._reward_code_list_after_water = list()
            for i in value:
                self._reward_code_list_after_water.append(i)
    @property
    def reward_info_list(self):
        return self._reward_info_list

    @reward_info_list.setter
    def reward_info_list(self, value):
        if isinstance(value, list):
            self._reward_info_list = list()
            for i in value:
                if isinstance(i, RewardDTO):
                    self._reward_info_list.append(i)
                else:
                    self._reward_info_list.append(RewardDTO.from_alipay_dict(i))
    @property
    def rewarded_code_list(self):
        return self._rewarded_code_list

    @rewarded_code_list.setter
    def rewarded_code_list(self, value):
        if isinstance(value, list):
            self._rewarded_code_list = list()
            for i in value:
                self._rewarded_code_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestWelfareforestTransferResponse, self).parse_response_content(response_content)
        if 'effect_energy' in response:
            self.effect_energy = response['effect_energy']
        if 'idempotent' in response:
            self.idempotent = response['idempotent']
        if 'reward_code_list_after_water' in response:
            self.reward_code_list_after_water = response['reward_code_list_after_water']
        if 'reward_info_list' in response:
            self.reward_info_list = response['reward_info_list']
        if 'rewarded_code_list' in response:
            self.rewarded_code_list = response['rewarded_code_list']
