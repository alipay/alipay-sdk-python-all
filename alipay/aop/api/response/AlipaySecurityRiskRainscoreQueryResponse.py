#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InfoCode import InfoCode


class AlipaySecurityRiskRainscoreQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskRainscoreQueryResponse, self).__init__()
        self._infocode = None
        self._label = None
        self._score = None
        self._unique_id = None

    @property
    def infocode(self):
        return self._infocode

    @infocode.setter
    def infocode(self, value):
        if isinstance(value, list):
            self._infocode = list()
            for i in value:
                if isinstance(i, InfoCode):
                    self._infocode.append(i)
                else:
                    self._infocode.append(InfoCode.from_alipay_dict(i))
    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        if isinstance(value, list):
            self._label = list()
            for i in value:
                self._label.append(i)
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskRainscoreQueryResponse, self).parse_response_content(response_content)
        if 'infocode' in response:
            self.infocode = response['infocode']
        if 'label' in response:
            self.label = response['label']
        if 'score' in response:
            self.score = response['score']
        if 'unique_id' in response:
            self.unique_id = response['unique_id']
