#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMemberDataTagQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMemberDataTagQueryResponse, self).__init__()
        self._card_member = None
        self._cate_prefer_label = None
        self._fashion_label = None
        self._taste_prefer_label = None
        self._user_id = None

    @property
    def card_member(self):
        return self._card_member

    @card_member.setter
    def card_member(self, value):
        self._card_member = value
    @property
    def cate_prefer_label(self):
        return self._cate_prefer_label

    @cate_prefer_label.setter
    def cate_prefer_label(self, value):
        self._cate_prefer_label = value
    @property
    def fashion_label(self):
        return self._fashion_label

    @fashion_label.setter
    def fashion_label(self, value):
        self._fashion_label = value
    @property
    def taste_prefer_label(self):
        return self._taste_prefer_label

    @taste_prefer_label.setter
    def taste_prefer_label(self, value):
        self._taste_prefer_label = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMemberDataTagQueryResponse, self).parse_response_content(response_content)
        if 'card_member' in response:
            self.card_member = response['card_member']
        if 'cate_prefer_label' in response:
            self.cate_prefer_label = response['cate_prefer_label']
        if 'fashion_label' in response:
            self.fashion_label = response['fashion_label']
        if 'taste_prefer_label' in response:
            self.taste_prefer_label = response['taste_prefer_label']
        if 'user_id' in response:
            self.user_id = response['user_id']
