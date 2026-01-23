#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryCareertrainingUseractivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCareertrainingUseractivityQueryResponse, self).__init__()
        self._activity_end_time = None
        self._activity_start_time = None
        self._activity_status = None
        self._can_join = None

    @property
    def activity_end_time(self):
        return self._activity_end_time

    @activity_end_time.setter
    def activity_end_time(self, value):
        self._activity_end_time = value
    @property
    def activity_start_time(self):
        return self._activity_start_time

    @activity_start_time.setter
    def activity_start_time(self, value):
        self._activity_start_time = value
    @property
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value
    @property
    def can_join(self):
        return self._can_join

    @can_join.setter
    def can_join(self, value):
        self._can_join = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCareertrainingUseractivityQueryResponse, self).parse_response_content(response_content)
        if 'activity_end_time' in response:
            self.activity_end_time = response['activity_end_time']
        if 'activity_start_time' in response:
            self.activity_start_time = response['activity_start_time']
        if 'activity_status' in response:
            self.activity_status = response['activity_status']
        if 'can_join' in response:
            self.can_join = response['can_join']
