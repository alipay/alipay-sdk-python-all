#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntforestBubbleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestBubbleQueryResponse, self).__init__()
        self._can_collect_energy = None
        self._forest_user = None

    @property
    def can_collect_energy(self):
        return self._can_collect_energy

    @can_collect_energy.setter
    def can_collect_energy(self, value):
        self._can_collect_energy = value
    @property
    def forest_user(self):
        return self._forest_user

    @forest_user.setter
    def forest_user(self, value):
        self._forest_user = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestBubbleQueryResponse, self).parse_response_content(response_content)
        if 'can_collect_energy' in response:
            self.can_collect_energy = response['can_collect_energy']
        if 'forest_user' in response:
            self.forest_user = response['forest_user']
