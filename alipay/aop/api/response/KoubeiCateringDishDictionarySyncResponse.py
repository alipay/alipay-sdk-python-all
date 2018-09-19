#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringDishDictionarySyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishDictionarySyncResponse, self).__init__()
        self._dictionary_id = None

    @property
    def dictionary_id(self):
        return self._dictionary_id

    @dictionary_id.setter
    def dictionary_id(self, value):
        self._dictionary_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishDictionarySyncResponse, self).parse_response_content(response_content)
        if 'dictionary_id' in response:
            self.dictionary_id = response['dictionary_id']
