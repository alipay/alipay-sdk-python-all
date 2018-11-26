#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiServindustryExerciseMemberCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiServindustryExerciseMemberCreateResponse, self).__init__()
        self._fitness_id = None
        self._member_id = None

    @property
    def fitness_id(self):
        return self._fitness_id

    @fitness_id.setter
    def fitness_id(self, value):
        self._fitness_id = value
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiServindustryExerciseMemberCreateResponse, self).parse_response_content(response_content)
        if 'fitness_id' in response:
            self.fitness_id = response['fitness_id']
        if 'member_id' in response:
            self.member_id = response['member_id']
