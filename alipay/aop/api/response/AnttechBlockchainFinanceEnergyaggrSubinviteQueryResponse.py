#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LoadInfoNode import LoadInfoNode
from alipay.aop.api.domain.BidResult import BidResult
from alipay.aop.api.domain.DeclareStrategy import DeclareStrategy
from alipay.aop.api.domain.EvaluateResult import EvaluateResult
from alipay.aop.api.domain.LoadInfoNode import LoadInfoNode
from alipay.aop.api.domain.ResponseDeclare import ResponseDeclare


class AnttechBlockchainFinanceEnergyaggrSubinviteQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceEnergyaggrSubinviteQueryResponse, self).__init__()
        self._base_line = None
        self._bid_result = None
        self._declare_start_time = None
        self._declare_strategy = None
        self._evaluate_result = None
        self._invite_id = None
        self._invite_name = None
        self._invite_release_time = None
        self._invite_type = None
        self._market_demand = None
        self._response_declare = None
        self._response_end_time = None
        self._response_start_time = None
        self._south_declare_end_time = None
        self._status = None
        self._sub_invite_id = None

    @property
    def base_line(self):
        return self._base_line

    @base_line.setter
    def base_line(self, value):
        if isinstance(value, list):
            self._base_line = list()
            for i in value:
                if isinstance(i, LoadInfoNode):
                    self._base_line.append(i)
                else:
                    self._base_line.append(LoadInfoNode.from_alipay_dict(i))
    @property
    def bid_result(self):
        return self._bid_result

    @bid_result.setter
    def bid_result(self, value):
        if isinstance(value, BidResult):
            self._bid_result = value
        else:
            self._bid_result = BidResult.from_alipay_dict(value)
    @property
    def declare_start_time(self):
        return self._declare_start_time

    @declare_start_time.setter
    def declare_start_time(self, value):
        self._declare_start_time = value
    @property
    def declare_strategy(self):
        return self._declare_strategy

    @declare_strategy.setter
    def declare_strategy(self, value):
        if isinstance(value, DeclareStrategy):
            self._declare_strategy = value
        else:
            self._declare_strategy = DeclareStrategy.from_alipay_dict(value)
    @property
    def evaluate_result(self):
        return self._evaluate_result

    @evaluate_result.setter
    def evaluate_result(self, value):
        if isinstance(value, EvaluateResult):
            self._evaluate_result = value
        else:
            self._evaluate_result = EvaluateResult.from_alipay_dict(value)
    @property
    def invite_id(self):
        return self._invite_id

    @invite_id.setter
    def invite_id(self, value):
        self._invite_id = value
    @property
    def invite_name(self):
        return self._invite_name

    @invite_name.setter
    def invite_name(self, value):
        self._invite_name = value
    @property
    def invite_release_time(self):
        return self._invite_release_time

    @invite_release_time.setter
    def invite_release_time(self, value):
        self._invite_release_time = value
    @property
    def invite_type(self):
        return self._invite_type

    @invite_type.setter
    def invite_type(self, value):
        self._invite_type = value
    @property
    def market_demand(self):
        return self._market_demand

    @market_demand.setter
    def market_demand(self, value):
        if isinstance(value, list):
            self._market_demand = list()
            for i in value:
                if isinstance(i, LoadInfoNode):
                    self._market_demand.append(i)
                else:
                    self._market_demand.append(LoadInfoNode.from_alipay_dict(i))
    @property
    def response_declare(self):
        return self._response_declare

    @response_declare.setter
    def response_declare(self, value):
        if isinstance(value, ResponseDeclare):
            self._response_declare = value
        else:
            self._response_declare = ResponseDeclare.from_alipay_dict(value)
    @property
    def response_end_time(self):
        return self._response_end_time

    @response_end_time.setter
    def response_end_time(self, value):
        self._response_end_time = value
    @property
    def response_start_time(self):
        return self._response_start_time

    @response_start_time.setter
    def response_start_time(self, value):
        self._response_start_time = value
    @property
    def south_declare_end_time(self):
        return self._south_declare_end_time

    @south_declare_end_time.setter
    def south_declare_end_time(self, value):
        self._south_declare_end_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_invite_id(self):
        return self._sub_invite_id

    @sub_invite_id.setter
    def sub_invite_id(self, value):
        self._sub_invite_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceEnergyaggrSubinviteQueryResponse, self).parse_response_content(response_content)
        if 'base_line' in response:
            self.base_line = response['base_line']
        if 'bid_result' in response:
            self.bid_result = response['bid_result']
        if 'declare_start_time' in response:
            self.declare_start_time = response['declare_start_time']
        if 'declare_strategy' in response:
            self.declare_strategy = response['declare_strategy']
        if 'evaluate_result' in response:
            self.evaluate_result = response['evaluate_result']
        if 'invite_id' in response:
            self.invite_id = response['invite_id']
        if 'invite_name' in response:
            self.invite_name = response['invite_name']
        if 'invite_release_time' in response:
            self.invite_release_time = response['invite_release_time']
        if 'invite_type' in response:
            self.invite_type = response['invite_type']
        if 'market_demand' in response:
            self.market_demand = response['market_demand']
        if 'response_declare' in response:
            self.response_declare = response['response_declare']
        if 'response_end_time' in response:
            self.response_end_time = response['response_end_time']
        if 'response_start_time' in response:
            self.response_start_time = response['response_start_time']
        if 'south_declare_end_time' in response:
            self.south_declare_end_time = response['south_declare_end_time']
        if 'status' in response:
            self.status = response['status']
        if 'sub_invite_id' in response:
            self.sub_invite_id = response['sub_invite_id']
