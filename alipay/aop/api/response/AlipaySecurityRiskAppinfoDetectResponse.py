#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskAppinfoDetectResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskAppinfoDetectResponse, self).__init__()
        self._app_risk_info_list = None
        self._push = None
        self._request_id = None

    @property
    def app_risk_info_list(self):
        return self._app_risk_info_list

    @app_risk_info_list.setter
    def app_risk_info_list(self, value):
        self._app_risk_info_list = value
    @property
    def push(self):
        return self._push

    @push.setter
    def push(self, value):
        self._push = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskAppinfoDetectResponse, self).parse_response_content(response_content)
        if 'app_risk_info_list' in response:
            self.app_risk_info_list = response['app_risk_info_list']
        if 'push' in response:
            self.push = response['push']
        if 'request_id' in response:
            self.request_id = response['request_id']
