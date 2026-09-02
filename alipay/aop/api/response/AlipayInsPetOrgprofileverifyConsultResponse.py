#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsPetOrgprofileverifyConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsPetOrgprofileverifyConsultResponse, self).__init__()
        self._same_pet_result = None
        self._score = None
        self._status = None

    @property
    def same_pet_result(self):
        return self._same_pet_result

    @same_pet_result.setter
    def same_pet_result(self, value):
        self._same_pet_result = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsPetOrgprofileverifyConsultResponse, self).parse_response_content(response_content)
        if 'same_pet_result' in response:
            self.same_pet_result = response['same_pet_result']
        if 'score' in response:
            self.score = response['score']
        if 'status' in response:
            self.status = response['status']
