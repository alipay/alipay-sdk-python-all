#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignDiscountInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignDiscountInfoQueryResponse, self).__init__()
        self._agents = None
        self._alert_detail_list = None
        self._alert_users = None
        self._budget_amount = None
        self._creator = None
        self._discount_desc = None
        self._discount_id = None
        self._discount_name = None
        self._end_time = None
        self._owner = None
        self._price_calc_type = None
        self._remaining_budget_amount = None
        self._start_time = None
        self._status = None
        self._used_budget_amount = None

    @property
    def agents(self):
        return self._agents

    @agents.setter
    def agents(self, value):
        if isinstance(value, list):
            self._agents = list()
            for i in value:
                self._agents.append(i)
    @property
    def alert_detail_list(self):
        return self._alert_detail_list

    @alert_detail_list.setter
    def alert_detail_list(self, value):
        if isinstance(value, list):
            self._alert_detail_list = list()
            for i in value:
                self._alert_detail_list.append(i)
    @property
    def alert_users(self):
        return self._alert_users

    @alert_users.setter
    def alert_users(self, value):
        if isinstance(value, list):
            self._alert_users = list()
            for i in value:
                self._alert_users.append(i)
    @property
    def budget_amount(self):
        return self._budget_amount

    @budget_amount.setter
    def budget_amount(self, value):
        self._budget_amount = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def discount_desc(self):
        return self._discount_desc

    @discount_desc.setter
    def discount_desc(self, value):
        self._discount_desc = value
    @property
    def discount_id(self):
        return self._discount_id

    @discount_id.setter
    def discount_id(self, value):
        self._discount_id = value
    @property
    def discount_name(self):
        return self._discount_name

    @discount_name.setter
    def discount_name(self, value):
        self._discount_name = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def price_calc_type(self):
        return self._price_calc_type

    @price_calc_type.setter
    def price_calc_type(self, value):
        self._price_calc_type = value
    @property
    def remaining_budget_amount(self):
        return self._remaining_budget_amount

    @remaining_budget_amount.setter
    def remaining_budget_amount(self, value):
        self._remaining_budget_amount = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def used_budget_amount(self):
        return self._used_budget_amount

    @used_budget_amount.setter
    def used_budget_amount(self, value):
        self._used_budget_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignDiscountInfoQueryResponse, self).parse_response_content(response_content)
        if 'agents' in response:
            self.agents = response['agents']
        if 'alert_detail_list' in response:
            self.alert_detail_list = response['alert_detail_list']
        if 'alert_users' in response:
            self.alert_users = response['alert_users']
        if 'budget_amount' in response:
            self.budget_amount = response['budget_amount']
        if 'creator' in response:
            self.creator = response['creator']
        if 'discount_desc' in response:
            self.discount_desc = response['discount_desc']
        if 'discount_id' in response:
            self.discount_id = response['discount_id']
        if 'discount_name' in response:
            self.discount_name = response['discount_name']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'owner' in response:
            self.owner = response['owner']
        if 'price_calc_type' in response:
            self.price_calc_type = response['price_calc_type']
        if 'remaining_budget_amount' in response:
            self.remaining_budget_amount = response['remaining_budget_amount']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'status' in response:
            self.status = response['status']
        if 'used_budget_amount' in response:
            self.used_budget_amount = response['used_budget_amount']
