#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneHealthGiftQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneHealthGiftQueryResponse, self).__init__()
        self._already_open = None
        self._biz_type = None
        self._delta_sum_insured = None
        self._source_gained_sum_insured = None
        self._sum_insured = None

    @property
    def already_open(self):
        return self._already_open

    @already_open.setter
    def already_open(self, value):
        self._already_open = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def delta_sum_insured(self):
        return self._delta_sum_insured

    @delta_sum_insured.setter
    def delta_sum_insured(self, value):
        self._delta_sum_insured = value
    @property
    def source_gained_sum_insured(self):
        return self._source_gained_sum_insured

    @source_gained_sum_insured.setter
    def source_gained_sum_insured(self, value):
        self._source_gained_sum_insured = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneHealthGiftQueryResponse, self).parse_response_content(response_content)
        if 'already_open' in response:
            self.already_open = response['already_open']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'delta_sum_insured' in response:
            self.delta_sum_insured = response['delta_sum_insured']
        if 'source_gained_sum_insured' in response:
            self.source_gained_sum_insured = response['source_gained_sum_insured']
        if 'sum_insured' in response:
            self.sum_insured = response['sum_insured']
