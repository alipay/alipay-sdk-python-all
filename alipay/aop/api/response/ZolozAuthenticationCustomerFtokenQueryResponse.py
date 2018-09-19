#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ZhubUidTelPair import ZhubUidTelPair


class ZolozAuthenticationCustomerFtokenQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZolozAuthenticationCustomerFtokenQueryResponse, self).__init__()
        self._authimg_base_64 = None
        self._uid = None
        self._uid_tel_pair_list = None

    @property
    def authimg_base_64(self):
        return self._authimg_base_64

    @authimg_base_64.setter
    def authimg_base_64(self, value):
        self._authimg_base_64 = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def uid_tel_pair_list(self):
        return self._uid_tel_pair_list

    @uid_tel_pair_list.setter
    def uid_tel_pair_list(self, value):
        if isinstance(value, list):
            self._uid_tel_pair_list = list()
            for i in value:
                if isinstance(i, ZhubUidTelPair):
                    self._uid_tel_pair_list.append(i)
                else:
                    self._uid_tel_pair_list.append(ZhubUidTelPair.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZolozAuthenticationCustomerFtokenQueryResponse, self).parse_response_content(response_content)
        if 'authimg_base_64' in response:
            self.authimg_base_64 = response['authimg_base_64']
        if 'uid' in response:
            self.uid = response['uid']
        if 'uid_tel_pair_list' in response:
            self.uid_tel_pair_list = response['uid_tel_pair_list']
