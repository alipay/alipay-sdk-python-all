#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMultimediaResourceMasstokenGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMultimediaResourceMasstokenGetResponse, self).__init__()
        self._create_time = None
        self._dead_time = None
        self._mass_token = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def dead_time(self):
        return self._dead_time

    @dead_time.setter
    def dead_time(self, value):
        self._dead_time = value
    @property
    def mass_token(self):
        return self._mass_token

    @mass_token.setter
    def mass_token(self, value):
        self._mass_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayMultimediaResourceMasstokenGetResponse, self).parse_response_content(response_content)
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'dead_time' in response:
            self.dead_time = response['dead_time']
        if 'mass_token' in response:
            self.mass_token = response['mass_token']
