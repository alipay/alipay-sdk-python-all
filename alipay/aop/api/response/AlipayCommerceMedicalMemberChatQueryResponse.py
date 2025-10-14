#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMemberChatQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMemberChatQueryResponse, self).__init__()
        self._avatar = None
        self._doctor_message = None
        self._doctor_url = None
        self._nick_name = None
        self._slogan = None
        self._source = None
        self._unread_message = None

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def doctor_message(self):
        return self._doctor_message

    @doctor_message.setter
    def doctor_message(self, value):
        self._doctor_message = value
    @property
    def doctor_url(self):
        return self._doctor_url

    @doctor_url.setter
    def doctor_url(self, value):
        self._doctor_url = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def slogan(self):
        return self._slogan

    @slogan.setter
    def slogan(self, value):
        self._slogan = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def unread_message(self):
        return self._unread_message

    @unread_message.setter
    def unread_message(self, value):
        self._unread_message = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMemberChatQueryResponse, self).parse_response_content(response_content)
        if 'avatar' in response:
            self.avatar = response['avatar']
        if 'doctor_message' in response:
            self.doctor_message = response['doctor_message']
        if 'doctor_url' in response:
            self.doctor_url = response['doctor_url']
        if 'nick_name' in response:
            self.nick_name = response['nick_name']
        if 'slogan' in response:
            self.slogan = response['slogan']
        if 'source' in response:
            self.source = response['source']
        if 'unread_message' in response:
            self.unread_message = response['unread_message']
