#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicPersonalizedAdvertCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicPersonalizedAdvertCreateResponse, self).__init__()
        self._advert_group = None

    @property
    def advert_group(self):
        return self._advert_group

    @advert_group.setter
    def advert_group(self, value):
        self._advert_group = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicPersonalizedAdvertCreateResponse, self).parse_response_content(response_content)
        if 'advert_group' in response:
            self.advert_group = response['advert_group']
