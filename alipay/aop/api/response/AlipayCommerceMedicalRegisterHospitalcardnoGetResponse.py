#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalRegisterHospitalcardnoGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterHospitalcardnoGetResponse, self).__init__()
        self._card_no = None
        self._how_to_get_url = None
        self._main_title = None
        self._res_prop = None
        self._show_card_flag = None
        self._sub_title = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def how_to_get_url(self):
        return self._how_to_get_url

    @how_to_get_url.setter
    def how_to_get_url(self, value):
        self._how_to_get_url = value
    @property
    def main_title(self):
        return self._main_title

    @main_title.setter
    def main_title(self, value):
        self._main_title = value
    @property
    def res_prop(self):
        return self._res_prop

    @res_prop.setter
    def res_prop(self, value):
        self._res_prop = value
    @property
    def show_card_flag(self):
        return self._show_card_flag

    @show_card_flag.setter
    def show_card_flag(self, value):
        self._show_card_flag = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterHospitalcardnoGetResponse, self).parse_response_content(response_content)
        if 'card_no' in response:
            self.card_no = response['card_no']
        if 'how_to_get_url' in response:
            self.how_to_get_url = response['how_to_get_url']
        if 'main_title' in response:
            self.main_title = response['main_title']
        if 'res_prop' in response:
            self.res_prop = response['res_prop']
        if 'show_card_flag' in response:
            self.show_card_flag = response['show_card_flag']
        if 'sub_title' in response:
            self.sub_title = response['sub_title']
