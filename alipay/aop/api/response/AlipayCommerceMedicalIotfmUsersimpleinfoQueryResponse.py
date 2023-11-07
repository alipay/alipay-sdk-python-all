#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IotFmInsuCityVO import IotFmInsuCityVO


class AlipayCommerceMedicalIotfmUsersimpleinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIotfmUsersimpleinfoQueryResponse, self).__init__()
        self._fm_city_code = None
        self._fm_ins_city_code = None
        self._fm_insu_city_list = None
        self._fm_open_id = None
        self._fm_user_id = None
        self._fm_user_name = None

    @property
    def fm_city_code(self):
        return self._fm_city_code

    @fm_city_code.setter
    def fm_city_code(self, value):
        self._fm_city_code = value
    @property
    def fm_ins_city_code(self):
        return self._fm_ins_city_code

    @fm_ins_city_code.setter
    def fm_ins_city_code(self, value):
        self._fm_ins_city_code = value
    @property
    def fm_insu_city_list(self):
        return self._fm_insu_city_list

    @fm_insu_city_list.setter
    def fm_insu_city_list(self, value):
        if isinstance(value, list):
            self._fm_insu_city_list = list()
            for i in value:
                if isinstance(i, IotFmInsuCityVO):
                    self._fm_insu_city_list.append(i)
                else:
                    self._fm_insu_city_list.append(IotFmInsuCityVO.from_alipay_dict(i))
    @property
    def fm_open_id(self):
        return self._fm_open_id

    @fm_open_id.setter
    def fm_open_id(self, value):
        self._fm_open_id = value
    @property
    def fm_user_id(self):
        return self._fm_user_id

    @fm_user_id.setter
    def fm_user_id(self, value):
        self._fm_user_id = value
    @property
    def fm_user_name(self):
        return self._fm_user_name

    @fm_user_name.setter
    def fm_user_name(self, value):
        self._fm_user_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalIotfmUsersimpleinfoQueryResponse, self).parse_response_content(response_content)
        if 'fm_city_code' in response:
            self.fm_city_code = response['fm_city_code']
        if 'fm_ins_city_code' in response:
            self.fm_ins_city_code = response['fm_ins_city_code']
        if 'fm_insu_city_list' in response:
            self.fm_insu_city_list = response['fm_insu_city_list']
        if 'fm_open_id' in response:
            self.fm_open_id = response['fm_open_id']
        if 'fm_user_id' in response:
            self.fm_user_id = response['fm_user_id']
        if 'fm_user_name' in response:
            self.fm_user_name = response['fm_user_name']
