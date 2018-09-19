#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossCsChannelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossCsChannelQueryResponse, self).__init__()
        self._att = None
        self._comment = None
        self._connection_rate = None
        self._curr_agent_talking = None
        self._curr_agents_logged_in = None
        self._curr_number_waiting_calls = None
        self._current_not_ready_agents = None
        self._current_ready_agents = None
        self._row_key = None
        self._visitor_inflow = None
        self._visitor_response = None
        self._visitor_response_transfer = None

    @property
    def att(self):
        return self._att

    @att.setter
    def att(self, value):
        self._att = value
    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def connection_rate(self):
        return self._connection_rate

    @connection_rate.setter
    def connection_rate(self, value):
        self._connection_rate = value
    @property
    def curr_agent_talking(self):
        return self._curr_agent_talking

    @curr_agent_talking.setter
    def curr_agent_talking(self, value):
        self._curr_agent_talking = value
    @property
    def curr_agents_logged_in(self):
        return self._curr_agents_logged_in

    @curr_agents_logged_in.setter
    def curr_agents_logged_in(self, value):
        self._curr_agents_logged_in = value
    @property
    def curr_number_waiting_calls(self):
        return self._curr_number_waiting_calls

    @curr_number_waiting_calls.setter
    def curr_number_waiting_calls(self, value):
        self._curr_number_waiting_calls = value
    @property
    def current_not_ready_agents(self):
        return self._current_not_ready_agents

    @current_not_ready_agents.setter
    def current_not_ready_agents(self, value):
        self._current_not_ready_agents = value
    @property
    def current_ready_agents(self):
        return self._current_ready_agents

    @current_ready_agents.setter
    def current_ready_agents(self, value):
        self._current_ready_agents = value
    @property
    def row_key(self):
        return self._row_key

    @row_key.setter
    def row_key(self, value):
        self._row_key = value
    @property
    def visitor_inflow(self):
        return self._visitor_inflow

    @visitor_inflow.setter
    def visitor_inflow(self, value):
        self._visitor_inflow = value
    @property
    def visitor_response(self):
        return self._visitor_response

    @visitor_response.setter
    def visitor_response(self, value):
        self._visitor_response = value
    @property
    def visitor_response_transfer(self):
        return self._visitor_response_transfer

    @visitor_response_transfer.setter
    def visitor_response_transfer(self, value):
        self._visitor_response_transfer = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossCsChannelQueryResponse, self).parse_response_content(response_content)
        if 'att' in response:
            self.att = response['att']
        if 'comment' in response:
            self.comment = response['comment']
        if 'connection_rate' in response:
            self.connection_rate = response['connection_rate']
        if 'curr_agent_talking' in response:
            self.curr_agent_talking = response['curr_agent_talking']
        if 'curr_agents_logged_in' in response:
            self.curr_agents_logged_in = response['curr_agents_logged_in']
        if 'curr_number_waiting_calls' in response:
            self.curr_number_waiting_calls = response['curr_number_waiting_calls']
        if 'current_not_ready_agents' in response:
            self.current_not_ready_agents = response['current_not_ready_agents']
        if 'current_ready_agents' in response:
            self.current_ready_agents = response['current_ready_agents']
        if 'row_key' in response:
            self.row_key = response['row_key']
        if 'visitor_inflow' in response:
            self.visitor_inflow = response['visitor_inflow']
        if 'visitor_response' in response:
            self.visitor_response = response['visitor_response']
        if 'visitor_response_transfer' in response:
            self.visitor_response_transfer = response['visitor_response_transfer']
