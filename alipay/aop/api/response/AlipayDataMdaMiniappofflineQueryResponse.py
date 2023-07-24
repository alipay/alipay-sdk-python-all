#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaMiniappofflineQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaMiniappofflineQueryResponse, self).__init__()
        self._journey_planning = None
        self._journey_planning_trend = None
        self._match_focus = None
        self._obtain_pass = None
        self._pass_travel_user_cnt = None
        self._pass_travel_user_trend = None
        self._pass_use_scene = None
        self._ticket_service = None
        self._use_pass = None
        self._user_distribution = None

    @property
    def journey_planning(self):
        return self._journey_planning

    @journey_planning.setter
    def journey_planning(self, value):
        self._journey_planning = value
    @property
    def journey_planning_trend(self):
        return self._journey_planning_trend

    @journey_planning_trend.setter
    def journey_planning_trend(self, value):
        self._journey_planning_trend = value
    @property
    def match_focus(self):
        return self._match_focus

    @match_focus.setter
    def match_focus(self, value):
        self._match_focus = value
    @property
    def obtain_pass(self):
        return self._obtain_pass

    @obtain_pass.setter
    def obtain_pass(self, value):
        self._obtain_pass = value
    @property
    def pass_travel_user_cnt(self):
        return self._pass_travel_user_cnt

    @pass_travel_user_cnt.setter
    def pass_travel_user_cnt(self, value):
        self._pass_travel_user_cnt = value
    @property
    def pass_travel_user_trend(self):
        return self._pass_travel_user_trend

    @pass_travel_user_trend.setter
    def pass_travel_user_trend(self, value):
        self._pass_travel_user_trend = value
    @property
    def pass_use_scene(self):
        return self._pass_use_scene

    @pass_use_scene.setter
    def pass_use_scene(self, value):
        self._pass_use_scene = value
    @property
    def ticket_service(self):
        return self._ticket_service

    @ticket_service.setter
    def ticket_service(self, value):
        self._ticket_service = value
    @property
    def use_pass(self):
        return self._use_pass

    @use_pass.setter
    def use_pass(self, value):
        self._use_pass = value
    @property
    def user_distribution(self):
        return self._user_distribution

    @user_distribution.setter
    def user_distribution(self, value):
        self._user_distribution = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaMiniappofflineQueryResponse, self).parse_response_content(response_content)
        if 'journey_planning' in response:
            self.journey_planning = response['journey_planning']
        if 'journey_planning_trend' in response:
            self.journey_planning_trend = response['journey_planning_trend']
        if 'match_focus' in response:
            self.match_focus = response['match_focus']
        if 'obtain_pass' in response:
            self.obtain_pass = response['obtain_pass']
        if 'pass_travel_user_cnt' in response:
            self.pass_travel_user_cnt = response['pass_travel_user_cnt']
        if 'pass_travel_user_trend' in response:
            self.pass_travel_user_trend = response['pass_travel_user_trend']
        if 'pass_use_scene' in response:
            self.pass_use_scene = response['pass_use_scene']
        if 'ticket_service' in response:
            self.ticket_service = response['ticket_service']
        if 'use_pass' in response:
            self.use_pass = response['use_pass']
        if 'user_distribution' in response:
            self.user_distribution = response['user_distribution']
