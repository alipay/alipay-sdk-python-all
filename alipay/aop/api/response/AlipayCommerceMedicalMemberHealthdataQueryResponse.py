#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMemberHealthdataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMemberHealthdataQueryResponse, self).__init__()
        self._avatar = None
        self._has_device = None
        self._health_condition = None
        self._nick = None
        self._source = None

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def has_device(self):
        return self._has_device

    @has_device.setter
    def has_device(self, value):
        self._has_device = value
    @property
    def health_condition(self):
        return self._health_condition

    @health_condition.setter
    def health_condition(self, value):
        self._health_condition = value
    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, value):
        self._nick = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMemberHealthdataQueryResponse, self).parse_response_content(response_content)
        if 'avatar' in response:
            self.avatar = response['avatar']
        if 'has_device' in response:
            self.has_device = response['has_device']
        if 'health_condition' in response:
            self.health_condition = response['health_condition']
        if 'nick' in response:
            self.nick = response['nick']
        if 'source' in response:
            self.source = response['source']
