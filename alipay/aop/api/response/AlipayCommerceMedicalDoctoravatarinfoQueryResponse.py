#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalDoctoravatarinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalDoctoravatarinfoQueryResponse, self).__init__()
        self._avatar = None
        self._discovery_page_avatar = None
        self._status = None
        self._welcome_card_avatar = None

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def discovery_page_avatar(self):
        return self._discovery_page_avatar

    @discovery_page_avatar.setter
    def discovery_page_avatar(self, value):
        self._discovery_page_avatar = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def welcome_card_avatar(self):
        return self._welcome_card_avatar

    @welcome_card_avatar.setter
    def welcome_card_avatar(self, value):
        self._welcome_card_avatar = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalDoctoravatarinfoQueryResponse, self).parse_response_content(response_content)
        if 'avatar' in response:
            self.avatar = response['avatar']
        if 'discovery_page_avatar' in response:
            self.discovery_page_avatar = response['discovery_page_avatar']
        if 'status' in response:
            self.status = response['status']
        if 'welcome_card_avatar' in response:
            self.welcome_card_avatar = response['welcome_card_avatar']
