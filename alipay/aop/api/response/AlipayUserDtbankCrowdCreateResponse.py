#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserDtbankCrowdCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDtbankCrowdCreateResponse, self).__init__()
        self._create_time = None
        self._crowd_status = None
        self._express_inst_id = None
        self._out_biz_no = None
        self._proxy_bank_inst_id = None
        self._user_info = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def crowd_status(self):
        return self._crowd_status

    @crowd_status.setter
    def crowd_status(self, value):
        self._crowd_status = value
    @property
    def express_inst_id(self):
        return self._express_inst_id

    @express_inst_id.setter
    def express_inst_id(self, value):
        self._express_inst_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def proxy_bank_inst_id(self):
        return self._proxy_bank_inst_id

    @proxy_bank_inst_id.setter
    def proxy_bank_inst_id(self, value):
        self._proxy_bank_inst_id = value
    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        self._user_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserDtbankCrowdCreateResponse, self).parse_response_content(response_content)
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'crowd_status' in response:
            self.crowd_status = response['crowd_status']
        if 'express_inst_id' in response:
            self.express_inst_id = response['express_inst_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'proxy_bank_inst_id' in response:
            self.proxy_bank_inst_id = response['proxy_bank_inst_id']
        if 'user_info' in response:
            self.user_info = response['user_info']
