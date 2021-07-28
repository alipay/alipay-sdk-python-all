#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccessPublicKey import AccessPublicKey


class AlipayEbppCommunityPubkeyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityPubkeyQueryResponse, self).__init__()
        self._e_tag = None
        self._pubkey_list = None

    @property
    def e_tag(self):
        return self._e_tag

    @e_tag.setter
    def e_tag(self, value):
        self._e_tag = value
    @property
    def pubkey_list(self):
        return self._pubkey_list

    @pubkey_list.setter
    def pubkey_list(self, value):
        if isinstance(value, list):
            self._pubkey_list = list()
            for i in value:
                if isinstance(i, AccessPublicKey):
                    self._pubkey_list.append(i)
                else:
                    self._pubkey_list.append(AccessPublicKey.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityPubkeyQueryResponse, self).parse_response_content(response_content)
        if 'e_tag' in response:
            self.e_tag = response['e_tag']
        if 'pubkey_list' in response:
            self.pubkey_list = response['pubkey_list']
