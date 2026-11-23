#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RegisterHospitalInfoDTO import RegisterHospitalInfoDTO
from alipay.aop.api.domain.RegisterIsvDisplayVO import RegisterIsvDisplayVO


class AlipayCommerceMedicalRegisterHospitallistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterHospitallistQueryResponse, self).__init__()
        self._chat_id = None
        self._has_more = None
        self._hospital_list = None
        self._isv_display = None
        self._page_key = None
        self._res_prop = None
        self._second_page_key = None
        self._sort_type = None
        self._total_count = None
        self._type = None

    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def hospital_list(self):
        return self._hospital_list

    @hospital_list.setter
    def hospital_list(self, value):
        if isinstance(value, list):
            self._hospital_list = list()
            for i in value:
                if isinstance(i, RegisterHospitalInfoDTO):
                    self._hospital_list.append(i)
                else:
                    self._hospital_list.append(RegisterHospitalInfoDTO.from_alipay_dict(i))
    @property
    def isv_display(self):
        return self._isv_display

    @isv_display.setter
    def isv_display(self, value):
        if isinstance(value, RegisterIsvDisplayVO):
            self._isv_display = value
        else:
            self._isv_display = RegisterIsvDisplayVO.from_alipay_dict(value)
    @property
    def page_key(self):
        return self._page_key

    @page_key.setter
    def page_key(self, value):
        self._page_key = value
    @property
    def res_prop(self):
        return self._res_prop

    @res_prop.setter
    def res_prop(self, value):
        self._res_prop = value
    @property
    def second_page_key(self):
        return self._second_page_key

    @second_page_key.setter
    def second_page_key(self, value):
        self._second_page_key = value
    @property
    def sort_type(self):
        return self._sort_type

    @sort_type.setter
    def sort_type(self, value):
        self._sort_type = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterHospitallistQueryResponse, self).parse_response_content(response_content)
        if 'chat_id' in response:
            self.chat_id = response['chat_id']
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'hospital_list' in response:
            self.hospital_list = response['hospital_list']
        if 'isv_display' in response:
            self.isv_display = response['isv_display']
        if 'page_key' in response:
            self.page_key = response['page_key']
        if 'res_prop' in response:
            self.res_prop = response['res_prop']
        if 'second_page_key' in response:
            self.second_page_key = response['second_page_key']
        if 'sort_type' in response:
            self.sort_type = response['sort_type']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'type' in response:
            self.type = response['type']
