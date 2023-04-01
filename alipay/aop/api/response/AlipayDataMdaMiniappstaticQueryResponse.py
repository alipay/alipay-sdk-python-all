#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaMiniappstaticQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaMiniappstaticQueryResponse, self).__init__()
        self._accommodation = None
        self._fine_food = None
        self._focus_ag = None
        self._language_version = None
        self._one_yard_trip = None
        self._scenic_spot = None
        self._service_scenario = None
        self._service_scenario_map = None

    @property
    def accommodation(self):
        return self._accommodation

    @accommodation.setter
    def accommodation(self, value):
        self._accommodation = value
    @property
    def fine_food(self):
        return self._fine_food

    @fine_food.setter
    def fine_food(self, value):
        self._fine_food = value
    @property
    def focus_ag(self):
        return self._focus_ag

    @focus_ag.setter
    def focus_ag(self, value):
        self._focus_ag = value
    @property
    def language_version(self):
        return self._language_version

    @language_version.setter
    def language_version(self, value):
        self._language_version = value
    @property
    def one_yard_trip(self):
        return self._one_yard_trip

    @one_yard_trip.setter
    def one_yard_trip(self, value):
        self._one_yard_trip = value
    @property
    def scenic_spot(self):
        return self._scenic_spot

    @scenic_spot.setter
    def scenic_spot(self, value):
        self._scenic_spot = value
    @property
    def service_scenario(self):
        return self._service_scenario

    @service_scenario.setter
    def service_scenario(self, value):
        self._service_scenario = value
    @property
    def service_scenario_map(self):
        return self._service_scenario_map

    @service_scenario_map.setter
    def service_scenario_map(self, value):
        self._service_scenario_map = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaMiniappstaticQueryResponse, self).parse_response_content(response_content)
        if 'accommodation' in response:
            self.accommodation = response['accommodation']
        if 'fine_food' in response:
            self.fine_food = response['fine_food']
        if 'focus_ag' in response:
            self.focus_ag = response['focus_ag']
        if 'language_version' in response:
            self.language_version = response['language_version']
        if 'one_yard_trip' in response:
            self.one_yard_trip = response['one_yard_trip']
        if 'scenic_spot' in response:
            self.scenic_spot = response['scenic_spot']
        if 'service_scenario' in response:
            self.service_scenario = response['service_scenario']
        if 'service_scenario_map' in response:
            self.service_scenario_map = response['service_scenario_map']
