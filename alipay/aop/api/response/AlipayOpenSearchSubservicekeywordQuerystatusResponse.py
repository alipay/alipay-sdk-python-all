#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KeyWordInfo import KeyWordInfo


class AlipayOpenSearchSubservicekeywordQuerystatusResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSearchSubservicekeywordQuerystatusResponse, self).__init__()
        self._key_words = None

    @property
    def key_words(self):
        return self._key_words

    @key_words.setter
    def key_words(self, value):
        if isinstance(value, list):
            self._key_words = list()
            for i in value:
                if isinstance(i, KeyWordInfo):
                    self._key_words.append(i)
                else:
                    self._key_words.append(KeyWordInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSearchSubservicekeywordQuerystatusResponse, self).parse_response_content(response_content)
        if 'key_words' in response:
            self.key_words = response['key_words']
