#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCircularAgreementSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCircularAgreementSignResponse, self).__init__()
        self._bind_wallet_id = None
        self._bind_wallet_type = None
        self._relation_openid = None
        self._relation_uid = None
        self._status = None
        self._url = None

    @property
    def bind_wallet_id(self):
        return self._bind_wallet_id

    @bind_wallet_id.setter
    def bind_wallet_id(self, value):
        self._bind_wallet_id = value
    @property
    def bind_wallet_type(self):
        return self._bind_wallet_type

    @bind_wallet_type.setter
    def bind_wallet_type(self, value):
        self._bind_wallet_type = value
    @property
    def relation_openid(self):
        return self._relation_openid

    @relation_openid.setter
    def relation_openid(self, value):
        self._relation_openid = value
    @property
    def relation_uid(self):
        return self._relation_uid

    @relation_uid.setter
    def relation_uid(self, value):
        self._relation_uid = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCircularAgreementSignResponse, self).parse_response_content(response_content)
        if 'bind_wallet_id' in response:
            self.bind_wallet_id = response['bind_wallet_id']
        if 'bind_wallet_type' in response:
            self.bind_wallet_type = response['bind_wallet_type']
        if 'relation_openid' in response:
            self.relation_openid = response['relation_openid']
        if 'relation_uid' in response:
            self.relation_uid = response['relation_uid']
        if 'status' in response:
            self.status = response['status']
        if 'url' in response:
            self.url = response['url']
