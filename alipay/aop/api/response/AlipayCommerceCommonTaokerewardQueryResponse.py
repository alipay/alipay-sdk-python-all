#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaoKeRewardRecordDTO import TaoKeRewardRecordDTO


class AlipayCommerceCommonTaokerewardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommonTaokerewardQueryResponse, self).__init__()
        self._reward_record_list = None

    @property
    def reward_record_list(self):
        return self._reward_record_list

    @reward_record_list.setter
    def reward_record_list(self, value):
        if isinstance(value, list):
            self._reward_record_list = list()
            for i in value:
                if isinstance(i, TaoKeRewardRecordDTO):
                    self._reward_record_list.append(i)
                else:
                    self._reward_record_list.append(TaoKeRewardRecordDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommonTaokerewardQueryResponse, self).parse_response_content(response_content)
        if 'reward_record_list' in response:
            self.reward_record_list = response['reward_record_list']
