#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaWelfareagofflineQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaWelfareagofflineQueryResponse, self).__init__()
        self._donate_flame_cnt = None
        self._donate_school = None
        self._flame_cnt = None
        self._total_donate_user = None
        self._total_obtain_user = None

    @property
    def donate_flame_cnt(self):
        return self._donate_flame_cnt

    @donate_flame_cnt.setter
    def donate_flame_cnt(self, value):
        self._donate_flame_cnt = value
    @property
    def donate_school(self):
        return self._donate_school

    @donate_school.setter
    def donate_school(self, value):
        self._donate_school = value
    @property
    def flame_cnt(self):
        return self._flame_cnt

    @flame_cnt.setter
    def flame_cnt(self, value):
        self._flame_cnt = value
    @property
    def total_donate_user(self):
        return self._total_donate_user

    @total_donate_user.setter
    def total_donate_user(self, value):
        self._total_donate_user = value
    @property
    def total_obtain_user(self):
        return self._total_obtain_user

    @total_obtain_user.setter
    def total_obtain_user(self, value):
        self._total_obtain_user = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaWelfareagofflineQueryResponse, self).parse_response_content(response_content)
        if 'donate_flame_cnt' in response:
            self.donate_flame_cnt = response['donate_flame_cnt']
        if 'donate_school' in response:
            self.donate_school = response['donate_school']
        if 'flame_cnt' in response:
            self.flame_cnt = response['flame_cnt']
        if 'total_donate_user' in response:
            self.total_donate_user = response['total_donate_user']
        if 'total_obtain_user' in response:
            self.total_obtain_user = response['total_obtain_user']
