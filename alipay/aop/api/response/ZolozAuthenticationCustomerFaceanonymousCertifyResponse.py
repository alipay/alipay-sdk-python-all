#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZolozAuthenticationCustomerFaceanonymousCertifyResponse(AlipayResponse):

    def __init__(self):
        super(ZolozAuthenticationCustomerFaceanonymousCertifyResponse, self).__init__()
        self._attack = None
        self._far_threshold = None
        self._joint_quality = None
        self._not_same_face_threshold = None
        self._passed = None
        self._same_face_threshold = None
        self._server_min_quality = None
        self._similarity = None

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack = value
    @property
    def far_threshold(self):
        return self._far_threshold

    @far_threshold.setter
    def far_threshold(self, value):
        self._far_threshold = value
    @property
    def joint_quality(self):
        return self._joint_quality

    @joint_quality.setter
    def joint_quality(self, value):
        self._joint_quality = value
    @property
    def not_same_face_threshold(self):
        return self._not_same_face_threshold

    @not_same_face_threshold.setter
    def not_same_face_threshold(self, value):
        self._not_same_face_threshold = value
    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value
    @property
    def same_face_threshold(self):
        return self._same_face_threshold

    @same_face_threshold.setter
    def same_face_threshold(self, value):
        self._same_face_threshold = value
    @property
    def server_min_quality(self):
        return self._server_min_quality

    @server_min_quality.setter
    def server_min_quality(self, value):
        self._server_min_quality = value
    @property
    def similarity(self):
        return self._similarity

    @similarity.setter
    def similarity(self, value):
        self._similarity = value

    def parse_response_content(self, response_content):
        response = super(ZolozAuthenticationCustomerFaceanonymousCertifyResponse, self).parse_response_content(response_content)
        if 'attack' in response:
            self.attack = response['attack']
        if 'far_threshold' in response:
            self.far_threshold = response['far_threshold']
        if 'joint_quality' in response:
            self.joint_quality = response['joint_quality']
        if 'not_same_face_threshold' in response:
            self.not_same_face_threshold = response['not_same_face_threshold']
        if 'passed' in response:
            self.passed = response['passed']
        if 'same_face_threshold' in response:
            self.same_face_threshold = response['same_face_threshold']
        if 'server_min_quality' in response:
            self.server_min_quality = response['server_min_quality']
        if 'similarity' in response:
            self.similarity = response['similarity']
