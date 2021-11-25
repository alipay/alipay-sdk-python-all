#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdAntlescenterEsignresultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlescenterEsignresultQueryResponse, self).__init__()
        self._app_name = None
        self._business_unique_id = None
        self._oss_file_addr = None
        self._seal_request_id = None
        self._status = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def business_unique_id(self):
        return self._business_unique_id

    @business_unique_id.setter
    def business_unique_id(self, value):
        self._business_unique_id = value
    @property
    def oss_file_addr(self):
        return self._oss_file_addr

    @oss_file_addr.setter
    def oss_file_addr(self, value):
        self._oss_file_addr = value
    @property
    def seal_request_id(self):
        return self._seal_request_id

    @seal_request_id.setter
    def seal_request_id(self, value):
        self._seal_request_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlescenterEsignresultQueryResponse, self).parse_response_content(response_content)
        if 'app_name' in response:
            self.app_name = response['app_name']
        if 'business_unique_id' in response:
            self.business_unique_id = response['business_unique_id']
        if 'oss_file_addr' in response:
            self.oss_file_addr = response['oss_file_addr']
        if 'seal_request_id' in response:
            self.seal_request_id = response['seal_request_id']
        if 'status' in response:
            self.status = response['status']
