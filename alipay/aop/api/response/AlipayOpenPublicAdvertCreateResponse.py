#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicAdvertCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicAdvertCreateResponse, self).__init__()
        self._advert_group = None
        self._advert_id = None

    @property
    def advert_group(self):
        return self._advert_group

    @advert_group.setter
    def advert_group(self, value):
        self._advert_group = value
    @property
    def advert_id(self):
        return self._advert_id

    @advert_id.setter
    def advert_id(self, value):
        self._advert_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicAdvertCreateResponse, self).parse_response_content(response_content)
        if 'advert_group' in response:
            self.advert_group = response['advert_group']
        if 'advert_id' in response:
            self.advert_id = response['advert_id']
