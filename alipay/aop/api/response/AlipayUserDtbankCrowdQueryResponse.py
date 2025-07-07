#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserDtbankCrowdQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDtbankCrowdQueryResponse, self).__init__()
        self._create_time = None
        self._crowd_id = None
        self._crowd_status = None
        self._expire_time = None
        self._express_inst_id = None
        self._file_info_url = None
        self._match_user_total_count = None
        self._proxy_bank_inst_id = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value
    @property
    def crowd_status(self):
        return self._crowd_status

    @crowd_status.setter
    def crowd_status(self, value):
        self._crowd_status = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def express_inst_id(self):
        return self._express_inst_id

    @express_inst_id.setter
    def express_inst_id(self, value):
        self._express_inst_id = value
    @property
    def file_info_url(self):
        return self._file_info_url

    @file_info_url.setter
    def file_info_url(self, value):
        self._file_info_url = value
    @property
    def match_user_total_count(self):
        return self._match_user_total_count

    @match_user_total_count.setter
    def match_user_total_count(self, value):
        self._match_user_total_count = value
    @property
    def proxy_bank_inst_id(self):
        return self._proxy_bank_inst_id

    @proxy_bank_inst_id.setter
    def proxy_bank_inst_id(self, value):
        self._proxy_bank_inst_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserDtbankCrowdQueryResponse, self).parse_response_content(response_content)
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'crowd_id' in response:
            self.crowd_id = response['crowd_id']
        if 'crowd_status' in response:
            self.crowd_status = response['crowd_status']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'express_inst_id' in response:
            self.express_inst_id = response['express_inst_id']
        if 'file_info_url' in response:
            self.file_info_url = response['file_info_url']
        if 'match_user_total_count' in response:
            self.match_user_total_count = response['match_user_total_count']
        if 'proxy_bank_inst_id' in response:
            self.proxy_bank_inst_id = response['proxy_bank_inst_id']
