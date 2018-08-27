#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceRiskDigitalidentityQueryResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceRiskDigitalidentityQueryResponse, self).__init__()
        self._ato_score = None
        self._deviceid = None
        self._emulator = None
        self._fake_score = None
        self._root = None
        self._rub_score = None
        self._unique_id = None

    @property
    def ato_score(self):
        return self._ato_score

    @ato_score.setter
    def ato_score(self, value):
        self._ato_score = value
    @property
    def deviceid(self):
        return self._deviceid

    @deviceid.setter
    def deviceid(self, value):
        self._deviceid = value
    @property
    def emulator(self):
        return self._emulator

    @emulator.setter
    def emulator(self, value):
        self._emulator = value
    @property
    def fake_score(self):
        return self._fake_score

    @fake_score.setter
    def fake_score(self, value):
        self._fake_score = value
    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value
    @property
    def rub_score(self):
        return self._rub_score

    @rub_score.setter
    def rub_score(self, value):
        self._rub_score = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceRiskDigitalidentityQueryResponse, self).parse_response_content(response_content)
        if 'ato_score' in response:
            self.ato_score = response['ato_score']
        if 'deviceid' in response:
            self.deviceid = response['deviceid']
        if 'emulator' in response:
            self.emulator = response['emulator']
        if 'fake_score' in response:
            self.fake_score = response['fake_score']
        if 'root' in response:
            self.root = response['root']
        if 'rub_score' in response:
            self.rub_score = response['rub_score']
        if 'unique_id' in response:
            self.unique_id = response['unique_id']
