#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityPhase import ActivityPhase


class AlipayCommerceTransportChargerCobrandcardactivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportChargerCobrandcardactivityQueryResponse, self).__init__()
        self._activity_id = None
        self._activity_phases = None
        self._current_count = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_phases(self):
        return self._activity_phases

    @activity_phases.setter
    def activity_phases(self, value):
        if isinstance(value, list):
            self._activity_phases = list()
            for i in value:
                if isinstance(i, ActivityPhase):
                    self._activity_phases.append(i)
                else:
                    self._activity_phases.append(ActivityPhase.from_alipay_dict(i))
    @property
    def current_count(self):
        return self._current_count

    @current_count.setter
    def current_count(self, value):
        self._current_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportChargerCobrandcardactivityQueryResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'activity_phases' in response:
            self.activity_phases = response['activity_phases']
        if 'current_count' in response:
            self.current_count = response['current_count']
