#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SignInBonusStrategy import SignInBonusStrategy


class AlipayMarketingCampaignPlaysigninConfigQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignPlaysigninConfigQueryResponse, self).__init__()
        self._bonus_receive_type = None
        self._bonus_send_strategy_type = None
        self._bonus_strategies = None
        self._need_signup = None
        self._receive_time_expression = None
        self._signin_dimesion_type = None
        self._signin_upper_num = None
        self._signup_end_time = None
        self._signup_start_time = None

    @property
    def bonus_receive_type(self):
        return self._bonus_receive_type

    @bonus_receive_type.setter
    def bonus_receive_type(self, value):
        self._bonus_receive_type = value
    @property
    def bonus_send_strategy_type(self):
        return self._bonus_send_strategy_type

    @bonus_send_strategy_type.setter
    def bonus_send_strategy_type(self, value):
        self._bonus_send_strategy_type = value
    @property
    def bonus_strategies(self):
        return self._bonus_strategies

    @bonus_strategies.setter
    def bonus_strategies(self, value):
        if isinstance(value, list):
            self._bonus_strategies = list()
            for i in value:
                if isinstance(i, SignInBonusStrategy):
                    self._bonus_strategies.append(i)
                else:
                    self._bonus_strategies.append(SignInBonusStrategy.from_alipay_dict(i))
    @property
    def need_signup(self):
        return self._need_signup

    @need_signup.setter
    def need_signup(self, value):
        self._need_signup = value
    @property
    def receive_time_expression(self):
        return self._receive_time_expression

    @receive_time_expression.setter
    def receive_time_expression(self, value):
        self._receive_time_expression = value
    @property
    def signin_dimesion_type(self):
        return self._signin_dimesion_type

    @signin_dimesion_type.setter
    def signin_dimesion_type(self, value):
        self._signin_dimesion_type = value
    @property
    def signin_upper_num(self):
        return self._signin_upper_num

    @signin_upper_num.setter
    def signin_upper_num(self, value):
        self._signin_upper_num = value
    @property
    def signup_end_time(self):
        return self._signup_end_time

    @signup_end_time.setter
    def signup_end_time(self, value):
        self._signup_end_time = value
    @property
    def signup_start_time(self):
        return self._signup_start_time

    @signup_start_time.setter
    def signup_start_time(self, value):
        self._signup_start_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignPlaysigninConfigQueryResponse, self).parse_response_content(response_content)
        if 'bonus_receive_type' in response:
            self.bonus_receive_type = response['bonus_receive_type']
        if 'bonus_send_strategy_type' in response:
            self.bonus_send_strategy_type = response['bonus_send_strategy_type']
        if 'bonus_strategies' in response:
            self.bonus_strategies = response['bonus_strategies']
        if 'need_signup' in response:
            self.need_signup = response['need_signup']
        if 'receive_time_expression' in response:
            self.receive_time_expression = response['receive_time_expression']
        if 'signin_dimesion_type' in response:
            self.signin_dimesion_type = response['signin_dimesion_type']
        if 'signin_upper_num' in response:
            self.signin_upper_num = response['signin_upper_num']
        if 'signup_end_time' in response:
            self.signup_end_time = response['signup_end_time']
        if 'signup_start_time' in response:
            self.signup_start_time = response['signup_start_time']
