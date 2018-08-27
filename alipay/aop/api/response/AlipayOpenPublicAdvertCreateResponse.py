#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicAdvertCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicAdvertCreateResponse, self).__init__()
        self._advert_id = None

    @property
    def advert_id(self):
        return self._advert_id

    @advert_id.setter
    def advert_id(self, value):
        self._advert_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicAdvertCreateResponse, self).parse_response_content(response_content)
        if 'advert_id' in response:
            self.advert_id = response['advert_id']
