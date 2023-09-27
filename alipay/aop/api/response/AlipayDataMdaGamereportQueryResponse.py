#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaGamereportQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaGamereportQueryResponse, self).__init__()
        self._online_watch_cnt = None
        self._online_watch_unt = None
        self._pass_cnt = None
        self._pass_unt = None
        self._ticket_cnt = None
        self._ticket_ratio = None
        self._ticket_spectator_cnt = None
        self._ticket_spectator_unt = None
        self._total_service_cnt = None
        self._total_service_unt = None

    @property
    def online_watch_cnt(self):
        return self._online_watch_cnt

    @online_watch_cnt.setter
    def online_watch_cnt(self, value):
        self._online_watch_cnt = value
    @property
    def online_watch_unt(self):
        return self._online_watch_unt

    @online_watch_unt.setter
    def online_watch_unt(self, value):
        self._online_watch_unt = value
    @property
    def pass_cnt(self):
        return self._pass_cnt

    @pass_cnt.setter
    def pass_cnt(self, value):
        self._pass_cnt = value
    @property
    def pass_unt(self):
        return self._pass_unt

    @pass_unt.setter
    def pass_unt(self, value):
        self._pass_unt = value
    @property
    def ticket_cnt(self):
        return self._ticket_cnt

    @ticket_cnt.setter
    def ticket_cnt(self, value):
        self._ticket_cnt = value
    @property
    def ticket_ratio(self):
        return self._ticket_ratio

    @ticket_ratio.setter
    def ticket_ratio(self, value):
        self._ticket_ratio = value
    @property
    def ticket_spectator_cnt(self):
        return self._ticket_spectator_cnt

    @ticket_spectator_cnt.setter
    def ticket_spectator_cnt(self, value):
        self._ticket_spectator_cnt = value
    @property
    def ticket_spectator_unt(self):
        return self._ticket_spectator_unt

    @ticket_spectator_unt.setter
    def ticket_spectator_unt(self, value):
        self._ticket_spectator_unt = value
    @property
    def total_service_cnt(self):
        return self._total_service_cnt

    @total_service_cnt.setter
    def total_service_cnt(self, value):
        self._total_service_cnt = value
    @property
    def total_service_unt(self):
        return self._total_service_unt

    @total_service_unt.setter
    def total_service_unt(self, value):
        self._total_service_unt = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaGamereportQueryResponse, self).parse_response_content(response_content)
        if 'online_watch_cnt' in response:
            self.online_watch_cnt = response['online_watch_cnt']
        if 'online_watch_unt' in response:
            self.online_watch_unt = response['online_watch_unt']
        if 'pass_cnt' in response:
            self.pass_cnt = response['pass_cnt']
        if 'pass_unt' in response:
            self.pass_unt = response['pass_unt']
        if 'ticket_cnt' in response:
            self.ticket_cnt = response['ticket_cnt']
        if 'ticket_ratio' in response:
            self.ticket_ratio = response['ticket_ratio']
        if 'ticket_spectator_cnt' in response:
            self.ticket_spectator_cnt = response['ticket_spectator_cnt']
        if 'ticket_spectator_unt' in response:
            self.ticket_spectator_unt = response['ticket_spectator_unt']
        if 'total_service_cnt' in response:
            self.total_service_cnt = response['total_service_cnt']
        if 'total_service_unt' in response:
            self.total_service_unt = response['total_service_unt']
