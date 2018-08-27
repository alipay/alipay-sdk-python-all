#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishDictionary import KbdishDictionary


class KoubeiCateringDishDictionaryQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishDictionaryQueryResponse, self).__init__()
        self._kb_dish_dictionary_list = None

    @property
    def kb_dish_dictionary_list(self):
        return self._kb_dish_dictionary_list

    @kb_dish_dictionary_list.setter
    def kb_dish_dictionary_list(self, value):
        if isinstance(value, list):
            self._kb_dish_dictionary_list = list()
            for i in value:
                if isinstance(i, KbdishDictionary):
                    self._kb_dish_dictionary_list.append(i)
                else:
                    self._kb_dish_dictionary_list.append(KbdishDictionary.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishDictionaryQueryResponse, self).parse_response_content(response_content)
        if 'kb_dish_dictionary_list' in response:
            self.kb_dish_dictionary_list = response['kb_dish_dictionary_list']
