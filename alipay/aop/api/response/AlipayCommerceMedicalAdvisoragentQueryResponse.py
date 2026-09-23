#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Doctors import Doctors


class AlipayCommerceMedicalAdvisoragentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalAdvisoragentQueryResponse, self).__init__()
        self._chat_id = None
        self._doctors = None
        self._session_id = None
        self._suggestions = None
        self._text = None

    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def doctors(self):
        return self._doctors

    @doctors.setter
    def doctors(self, value):
        if isinstance(value, Doctors):
            self._doctors = value
        else:
            self._doctors = Doctors.from_alipay_dict(value)
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def suggestions(self):
        return self._suggestions

    @suggestions.setter
    def suggestions(self, value):
        self._suggestions = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalAdvisoragentQueryResponse, self).parse_response_content(response_content)
        if 'chat_id' in response:
            self.chat_id = response['chat_id']
        if 'doctors' in response:
            self.doctors = response['doctors']
        if 'session_id' in response:
            self.session_id = response['session_id']
        if 'suggestions' in response:
            self.suggestions = response['suggestions']
        if 'text' in response:
            self.text = response['text']
