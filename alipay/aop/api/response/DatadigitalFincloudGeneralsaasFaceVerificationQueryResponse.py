#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudGeneralsaasFaceVerificationQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudGeneralsaasFaceVerificationQueryResponse, self).__init__()
        self._alive_photo = None
        self._attack_flag = None
        self._certify_state = None
        self._quality = None
        self._score = None

    @property
    def alive_photo(self):
        return self._alive_photo

    @alive_photo.setter
    def alive_photo(self, value):
        self._alive_photo = value
    @property
    def attack_flag(self):
        return self._attack_flag

    @attack_flag.setter
    def attack_flag(self, value):
        self._attack_flag = value
    @property
    def certify_state(self):
        return self._certify_state

    @certify_state.setter
    def certify_state(self, value):
        self._certify_state = value
    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, value):
        self._quality = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudGeneralsaasFaceVerificationQueryResponse, self).parse_response_content(response_content)
        if 'alive_photo' in response:
            self.alive_photo = response['alive_photo']
        if 'attack_flag' in response:
            self.attack_flag = response['attack_flag']
        if 'certify_state' in response:
            self.certify_state = response['certify_state']
        if 'quality' in response:
            self.quality = response['quality']
        if 'score' in response:
            self.score = response['score']
