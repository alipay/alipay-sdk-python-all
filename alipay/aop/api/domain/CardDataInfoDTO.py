#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardExtInfoDTO import CardExtInfoDTO


class CardDataInfoDTO(object):

    def __init__(self):
        self._card_data_id = None
        self._card_ext_info = None
        self._card_introduce = None
        self._card_key_words = None
        self._card_level = None
        self._card_logo = None
        self._card_name = None
        self._card_title = None
        self._card_url = None
        self._index = None
        self._parent_card_id = None
        self._parent_card_name = None

    @property
    def card_data_id(self):
        return self._card_data_id

    @card_data_id.setter
    def card_data_id(self, value):
        self._card_data_id = value
    @property
    def card_ext_info(self):
        return self._card_ext_info

    @card_ext_info.setter
    def card_ext_info(self, value):
        if isinstance(value, list):
            self._card_ext_info = list()
            for i in value:
                if isinstance(i, CardExtInfoDTO):
                    self._card_ext_info.append(i)
                else:
                    self._card_ext_info.append(CardExtInfoDTO.from_alipay_dict(i))
    @property
    def card_introduce(self):
        return self._card_introduce

    @card_introduce.setter
    def card_introduce(self, value):
        self._card_introduce = value
    @property
    def card_key_words(self):
        return self._card_key_words

    @card_key_words.setter
    def card_key_words(self, value):
        if isinstance(value, list):
            self._card_key_words = list()
            for i in value:
                self._card_key_words.append(i)
    @property
    def card_level(self):
        return self._card_level

    @card_level.setter
    def card_level(self, value):
        self._card_level = value
    @property
    def card_logo(self):
        return self._card_logo

    @card_logo.setter
    def card_logo(self, value):
        self._card_logo = value
    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def card_title(self):
        return self._card_title

    @card_title.setter
    def card_title(self, value):
        self._card_title = value
    @property
    def card_url(self):
        return self._card_url

    @card_url.setter
    def card_url(self, value):
        self._card_url = value
    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value
    @property
    def parent_card_id(self):
        return self._parent_card_id

    @parent_card_id.setter
    def parent_card_id(self, value):
        self._parent_card_id = value
    @property
    def parent_card_name(self):
        return self._parent_card_name

    @parent_card_name.setter
    def parent_card_name(self, value):
        self._parent_card_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_data_id:
            if hasattr(self.card_data_id, 'to_alipay_dict'):
                params['card_data_id'] = self.card_data_id.to_alipay_dict()
            else:
                params['card_data_id'] = self.card_data_id
        if self.card_ext_info:
            if isinstance(self.card_ext_info, list):
                for i in range(0, len(self.card_ext_info)):
                    element = self.card_ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_ext_info[i] = element.to_alipay_dict()
            if hasattr(self.card_ext_info, 'to_alipay_dict'):
                params['card_ext_info'] = self.card_ext_info.to_alipay_dict()
            else:
                params['card_ext_info'] = self.card_ext_info
        if self.card_introduce:
            if hasattr(self.card_introduce, 'to_alipay_dict'):
                params['card_introduce'] = self.card_introduce.to_alipay_dict()
            else:
                params['card_introduce'] = self.card_introduce
        if self.card_key_words:
            if isinstance(self.card_key_words, list):
                for i in range(0, len(self.card_key_words)):
                    element = self.card_key_words[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_key_words[i] = element.to_alipay_dict()
            if hasattr(self.card_key_words, 'to_alipay_dict'):
                params['card_key_words'] = self.card_key_words.to_alipay_dict()
            else:
                params['card_key_words'] = self.card_key_words
        if self.card_level:
            if hasattr(self.card_level, 'to_alipay_dict'):
                params['card_level'] = self.card_level.to_alipay_dict()
            else:
                params['card_level'] = self.card_level
        if self.card_logo:
            if hasattr(self.card_logo, 'to_alipay_dict'):
                params['card_logo'] = self.card_logo.to_alipay_dict()
            else:
                params['card_logo'] = self.card_logo
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        if self.card_title:
            if hasattr(self.card_title, 'to_alipay_dict'):
                params['card_title'] = self.card_title.to_alipay_dict()
            else:
                params['card_title'] = self.card_title
        if self.card_url:
            if hasattr(self.card_url, 'to_alipay_dict'):
                params['card_url'] = self.card_url.to_alipay_dict()
            else:
                params['card_url'] = self.card_url
        if self.index:
            if hasattr(self.index, 'to_alipay_dict'):
                params['index'] = self.index.to_alipay_dict()
            else:
                params['index'] = self.index
        if self.parent_card_id:
            if hasattr(self.parent_card_id, 'to_alipay_dict'):
                params['parent_card_id'] = self.parent_card_id.to_alipay_dict()
            else:
                params['parent_card_id'] = self.parent_card_id
        if self.parent_card_name:
            if hasattr(self.parent_card_name, 'to_alipay_dict'):
                params['parent_card_name'] = self.parent_card_name.to_alipay_dict()
            else:
                params['parent_card_name'] = self.parent_card_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardDataInfoDTO()
        if 'card_data_id' in d:
            o.card_data_id = d['card_data_id']
        if 'card_ext_info' in d:
            o.card_ext_info = d['card_ext_info']
        if 'card_introduce' in d:
            o.card_introduce = d['card_introduce']
        if 'card_key_words' in d:
            o.card_key_words = d['card_key_words']
        if 'card_level' in d:
            o.card_level = d['card_level']
        if 'card_logo' in d:
            o.card_logo = d['card_logo']
        if 'card_name' in d:
            o.card_name = d['card_name']
        if 'card_title' in d:
            o.card_title = d['card_title']
        if 'card_url' in d:
            o.card_url = d['card_url']
        if 'index' in d:
            o.index = d['index']
        if 'parent_card_id' in d:
            o.parent_card_id = d['parent_card_id']
        if 'parent_card_name' in d:
            o.parent_card_name = d['parent_card_name']
        return o


