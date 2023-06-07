#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAccountAvatarPictureCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAccountAvatarPictureCreateResponse, self).__init__()
        self._pic_url = None

    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAccountAvatarPictureCreateResponse, self).parse_response_content(response_content)
        if 'pic_url' in response:
            self.pic_url = response['pic_url']
