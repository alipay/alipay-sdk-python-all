#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpEsgScoreQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpEsgScoreQueryResponse, self).__init__()
        self._ep_cert_no = None
        self._ep_name = None
        self._esg_score = None
        self._evaluate_time = None

    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def esg_score(self):
        return self._esg_score

    @esg_score.setter
    def esg_score(self, value):
        self._esg_score = value
    @property
    def evaluate_time(self):
        return self._evaluate_time

    @evaluate_time.setter
    def evaluate_time(self, value):
        self._evaluate_time = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpEsgScoreQueryResponse, self).parse_response_content(response_content)
        if 'ep_cert_no' in response:
            self.ep_cert_no = response['ep_cert_no']
        if 'ep_name' in response:
            self.ep_name = response['ep_name']
        if 'esg_score' in response:
            self.esg_score = response['esg_score']
        if 'evaluate_time' in response:
            self.evaluate_time = response['evaluate_time']
