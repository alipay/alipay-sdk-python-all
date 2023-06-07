#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubAntSignResult import SubAntSignResult


class AlipayBossProdAntCasignCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntCasignCreateResponse, self).__init__()
        self._biz_no = None
        self._sign_flow_id = None
        self._sub_ant_sign_result_list = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def sign_flow_id(self):
        return self._sign_flow_id

    @sign_flow_id.setter
    def sign_flow_id(self, value):
        self._sign_flow_id = value
    @property
    def sub_ant_sign_result_list(self):
        return self._sub_ant_sign_result_list

    @sub_ant_sign_result_list.setter
    def sub_ant_sign_result_list(self, value):
        if isinstance(value, list):
            self._sub_ant_sign_result_list = list()
            for i in value:
                if isinstance(i, SubAntSignResult):
                    self._sub_ant_sign_result_list.append(i)
                else:
                    self._sub_ant_sign_result_list.append(SubAntSignResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntCasignCreateResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'sign_flow_id' in response:
            self.sign_flow_id = response['sign_flow_id']
        if 'sub_ant_sign_result_list' in response:
            self.sub_ant_sign_result_list = response['sub_ant_sign_result_list']
