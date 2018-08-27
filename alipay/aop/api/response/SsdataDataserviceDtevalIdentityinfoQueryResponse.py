#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class SsdataDataserviceDtevalIdentityinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(SsdataDataserviceDtevalIdentityinfoQueryResponse, self).__init__()
        self._description = None
        self._id_card_no = None
        self._phone = None
        self._status = None
        self._user_name = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def id_card_no(self):
        return self._id_card_no

    @id_card_no.setter
    def id_card_no(self, value):
        self._id_card_no = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(SsdataDataserviceDtevalIdentityinfoQueryResponse, self).parse_response_content(response_content)
        if 'description' in response:
            self.description = response['description']
        if 'id_card_no' in response:
            self.id_card_no = response['id_card_no']
        if 'phone' in response:
            self.phone = response['phone']
        if 'status' in response:
            self.status = response['status']
        if 'user_name' in response:
            self.user_name = response['user_name']
