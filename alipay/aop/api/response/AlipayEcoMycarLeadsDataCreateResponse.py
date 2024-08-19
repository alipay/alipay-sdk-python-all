#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarLeadsDataCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarLeadsDataCreateResponse, self).__init__()
        self._leads_id = None
        self._leads_time = None
        self._open_id = None
        self._out_leads_id = None
        self._user_id = None

    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def leads_time(self):
        return self._leads_time

    @leads_time.setter
    def leads_time(self, value):
        self._leads_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_leads_id(self):
        return self._out_leads_id

    @out_leads_id.setter
    def out_leads_id(self, value):
        self._out_leads_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarLeadsDataCreateResponse, self).parse_response_content(response_content)
        if 'leads_id' in response:
            self.leads_id = response['leads_id']
        if 'leads_time' in response:
            self.leads_time = response['leads_time']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'out_leads_id' in response:
            self.out_leads_id = response['out_leads_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
