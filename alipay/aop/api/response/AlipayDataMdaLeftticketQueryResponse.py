#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaLeftticketQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaLeftticketQueryResponse, self).__init__()
        self._ticket_channel = None
        self._ticket_city = None
        self._ticket_project = None
        self._ticket_radio = None
        self._today_ticket_cnt = None
        self._total_ticket_cnt = None

    @property
    def ticket_channel(self):
        return self._ticket_channel

    @ticket_channel.setter
    def ticket_channel(self, value):
        self._ticket_channel = value
    @property
    def ticket_city(self):
        return self._ticket_city

    @ticket_city.setter
    def ticket_city(self, value):
        self._ticket_city = value
    @property
    def ticket_project(self):
        return self._ticket_project

    @ticket_project.setter
    def ticket_project(self, value):
        self._ticket_project = value
    @property
    def ticket_radio(self):
        return self._ticket_radio

    @ticket_radio.setter
    def ticket_radio(self, value):
        self._ticket_radio = value
    @property
    def today_ticket_cnt(self):
        return self._today_ticket_cnt

    @today_ticket_cnt.setter
    def today_ticket_cnt(self, value):
        self._today_ticket_cnt = value
    @property
    def total_ticket_cnt(self):
        return self._total_ticket_cnt

    @total_ticket_cnt.setter
    def total_ticket_cnt(self, value):
        self._total_ticket_cnt = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaLeftticketQueryResponse, self).parse_response_content(response_content)
        if 'ticket_channel' in response:
            self.ticket_channel = response['ticket_channel']
        if 'ticket_city' in response:
            self.ticket_city = response['ticket_city']
        if 'ticket_project' in response:
            self.ticket_project = response['ticket_project']
        if 'ticket_radio' in response:
            self.ticket_radio = response['ticket_radio']
        if 'today_ticket_cnt' in response:
            self.today_ticket_cnt = response['today_ticket_cnt']
        if 'total_ticket_cnt' in response:
            self.total_ticket_cnt = response['total_ticket_cnt']
