#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduMpPrizeSendOrder import EduMpPrizeSendOrder


class AlipayCommerceEducateCampaignDrawcampTriggerResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCampaignDrawcampTriggerResponse, self).__init__()
        self._camp_id = None
        self._prize_id = None
        self._prize_name = None
        self._send_order_list = None
        self._trigger_result = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def send_order_list(self):
        return self._send_order_list

    @send_order_list.setter
    def send_order_list(self, value):
        if isinstance(value, list):
            self._send_order_list = list()
            for i in value:
                if isinstance(i, EduMpPrizeSendOrder):
                    self._send_order_list.append(i)
                else:
                    self._send_order_list.append(EduMpPrizeSendOrder.from_alipay_dict(i))
    @property
    def trigger_result(self):
        return self._trigger_result

    @trigger_result.setter
    def trigger_result(self, value):
        self._trigger_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCampaignDrawcampTriggerResponse, self).parse_response_content(response_content)
        if 'camp_id' in response:
            self.camp_id = response['camp_id']
        if 'prize_id' in response:
            self.prize_id = response['prize_id']
        if 'prize_name' in response:
            self.prize_name = response['prize_name']
        if 'send_order_list' in response:
            self.send_order_list = response['send_order_list']
        if 'trigger_result' in response:
            self.trigger_result = response['trigger_result']
