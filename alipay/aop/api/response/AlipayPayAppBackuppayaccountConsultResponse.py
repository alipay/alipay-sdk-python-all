#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayAppBackuppayaccountConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppBackuppayaccountConsultResponse, self).__init__()
        self._hidden_login_id = None
        self._open_same_person = None

    @property
    def hidden_login_id(self):
        return self._hidden_login_id

    @hidden_login_id.setter
    def hidden_login_id(self, value):
        self._hidden_login_id = value
    @property
    def open_same_person(self):
        return self._open_same_person

    @open_same_person.setter
    def open_same_person(self, value):
        self._open_same_person = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppBackuppayaccountConsultResponse, self).parse_response_content(response_content)
        if 'hidden_login_id' in response:
            self.hidden_login_id = response['hidden_login_id']
        if 'open_same_person' in response:
            self.open_same_person = response['open_same_person']
