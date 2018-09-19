#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceRiskDeviceidentityQueryResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceRiskDeviceidentityQueryResponse, self).__init__()
        self._ato_score = None
        self._fake_score = None
        self._rub_score = None
        self._umid = None
        self._unique_id = None

    @property
    def ato_score(self):
        return self._ato_score

    @ato_score.setter
    def ato_score(self, value):
        self._ato_score = value
    @property
    def fake_score(self):
        return self._fake_score

    @fake_score.setter
    def fake_score(self, value):
        self._fake_score = value
    @property
    def rub_score(self):
        return self._rub_score

    @rub_score.setter
    def rub_score(self, value):
        self._rub_score = value
    @property
    def umid(self):
        return self._umid

    @umid.setter
    def umid(self, value):
        self._umid = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceRiskDeviceidentityQueryResponse, self).parse_response_content(response_content)
        if 'ato_score' in response:
            self.ato_score = response['ato_score']
        if 'fake_score' in response:
            self.fake_score = response['fake_score']
        if 'rub_score' in response:
            self.rub_score = response['rub_score']
        if 'umid' in response:
            self.umid = response['umid']
        if 'unique_id' in response:
            self.unique_id = response['unique_id']
