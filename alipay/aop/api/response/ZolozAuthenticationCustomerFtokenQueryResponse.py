#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ZhubUidTelPair import ZhubUidTelPair


class ZolozAuthenticationCustomerFtokenQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZolozAuthenticationCustomerFtokenQueryResponse, self).__init__()
        self._age_check_result = None
        self._authimg_base_64 = None
        self._face_id = None
        self._uid = None
        self._uid_tel_pair_list = None

    @property
    def age_check_result(self):
        return self._age_check_result

    @age_check_result.setter
    def age_check_result(self, value):
        self._age_check_result = value
    @property
    def authimg_base_64(self):
        return self._authimg_base_64

    @authimg_base_64.setter
    def authimg_base_64(self, value):
        self._authimg_base_64 = value
    @property
    def face_id(self):
        return self._face_id

    @face_id.setter
    def face_id(self, value):
        self._face_id = value
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
        if 'age_check_result' in response:
            self.age_check_result = response['age_check_result']
        if 'authimg_base_64' in response:
            self.authimg_base_64 = response['authimg_base_64']
        if 'face_id' in response:
            self.face_id = response['face_id']
        if 'uid' in response:
            self.uid = response['uid']
        if 'uid_tel_pair_list' in response:
            self.uid_tel_pair_list = response['uid_tel_pair_list']
