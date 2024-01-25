#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppEnvShare import AppEnvShare


class AlipayCloudCloudrunEnvShareQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunEnvShareQueryResponse, self).__init__()
        self._app_env_shares = None
        self._result_msg = None

    @property
    def app_env_shares(self):
        return self._app_env_shares

    @app_env_shares.setter
    def app_env_shares(self, value):
        if isinstance(value, AppEnvShare):
            self._app_env_shares = value
        else:
            self._app_env_shares = AppEnvShare.from_alipay_dict(value)
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunEnvShareQueryResponse, self).parse_response_content(response_content)
        if 'app_env_shares' in response:
            self.app_env_shares = response['app_env_shares']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
