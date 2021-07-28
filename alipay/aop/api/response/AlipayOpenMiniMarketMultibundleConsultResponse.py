#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MarketResult import MarketResult


class AlipayOpenMiniMarketMultibundleConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniMarketMultibundleConsultResponse, self).__init__()
        self._bundle_id = None
        self._market_result_list = None
        self._mini_app_id = None
        self._user_id = None

    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def market_result_list(self):
        return self._market_result_list

    @market_result_list.setter
    def market_result_list(self, value):
        if isinstance(value, list):
            self._market_result_list = list()
            for i in value:
                if isinstance(i, MarketResult):
                    self._market_result_list.append(i)
                else:
                    self._market_result_list.append(MarketResult.from_alipay_dict(i))
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniMarketMultibundleConsultResponse, self).parse_response_content(response_content)
        if 'bundle_id' in response:
            self.bundle_id = response['bundle_id']
        if 'market_result_list' in response:
            self.market_result_list = response['market_result_list']
        if 'mini_app_id' in response:
            self.mini_app_id = response['mini_app_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
