#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RiskCheckLabel import RiskCheckLabel


class AlipayCloudTraasContentTextDetectResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudTraasContentTextDetectResponse, self).__init__()
        self._request_id = None
        self._risk_check_labels = None
        self._suggestion = None
        self._sync = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def risk_check_labels(self):
        return self._risk_check_labels

    @risk_check_labels.setter
    def risk_check_labels(self, value):
        if isinstance(value, list):
            self._risk_check_labels = list()
            for i in value:
                if isinstance(i, RiskCheckLabel):
                    self._risk_check_labels.append(i)
                else:
                    self._risk_check_labels.append(RiskCheckLabel.from_alipay_dict(i))
    @property
    def suggestion(self):
        return self._suggestion

    @suggestion.setter
    def suggestion(self, value):
        self._suggestion = value
    @property
    def sync(self):
        return self._sync

    @sync.setter
    def sync(self, value):
        self._sync = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudTraasContentTextDetectResponse, self).parse_response_content(response_content)
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'risk_check_labels' in response:
            self.risk_check_labels = response['risk_check_labels']
        if 'suggestion' in response:
            self.suggestion = response['suggestion']
        if 'sync' in response:
            self.sync = response['sync']
