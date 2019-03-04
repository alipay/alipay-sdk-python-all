#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignDrawcampTriggerResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignDrawcampTriggerResponse, self).__init__()
        self._camp_id = None
        self._camp_log_id = None
        self._display_name = None
        self._extend_field = None
        self._out_prize_id = None
        self._prize_flag = None
        self._prize_id = None
        self._prize_name = None
        self._repeat_trigger_flag = None
        self._trigger_result = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def camp_log_id(self):
        return self._camp_log_id

    @camp_log_id.setter
    def camp_log_id(self, value):
        self._camp_log_id = value
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def out_prize_id(self):
        return self._out_prize_id

    @out_prize_id.setter
    def out_prize_id(self, value):
        self._out_prize_id = value
    @property
    def prize_flag(self):
        return self._prize_flag

    @prize_flag.setter
    def prize_flag(self, value):
        self._prize_flag = value
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
    def repeat_trigger_flag(self):
        return self._repeat_trigger_flag

    @repeat_trigger_flag.setter
    def repeat_trigger_flag(self, value):
        self._repeat_trigger_flag = value
    @property
    def trigger_result(self):
        return self._trigger_result

    @trigger_result.setter
    def trigger_result(self, value):
        self._trigger_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignDrawcampTriggerResponse, self).parse_response_content(response_content)
        if 'camp_id' in response:
            self.camp_id = response['camp_id']
        if 'camp_log_id' in response:
            self.camp_log_id = response['camp_log_id']
        if 'display_name' in response:
            self.display_name = response['display_name']
        if 'extend_field' in response:
            self.extend_field = response['extend_field']
        if 'out_prize_id' in response:
            self.out_prize_id = response['out_prize_id']
        if 'prize_flag' in response:
            self.prize_flag = response['prize_flag']
        if 'prize_id' in response:
            self.prize_id = response['prize_id']
        if 'prize_name' in response:
            self.prize_name = response['prize_name']
        if 'repeat_trigger_flag' in response:
            self.repeat_trigger_flag = response['repeat_trigger_flag']
        if 'trigger_result' in response:
            self.trigger_result = response['trigger_result']
