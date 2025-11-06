#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCircularZftIndirectCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCircularZftIndirectCreateResponse, self).__init__()
        self._prod_confirm = None
        self._relation_openid = None
        self._relation_uid = None
        self._status = None
        self._sub_confirm = None

    @property
    def prod_confirm(self):
        return self._prod_confirm

    @prod_confirm.setter
    def prod_confirm(self, value):
        self._prod_confirm = value
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
    def sub_confirm(self):
        return self._sub_confirm

    @sub_confirm.setter
    def sub_confirm(self, value):
        self._sub_confirm = value

    def parse_response_content(self, response_content):
        response = super(AlipayCircularZftIndirectCreateResponse, self).parse_response_content(response_content)
        if 'prod_confirm' in response:
            self.prod_confirm = response['prod_confirm']
        if 'relation_openid' in response:
            self.relation_openid = response['relation_openid']
        if 'relation_uid' in response:
            self.relation_uid = response['relation_uid']
        if 'status' in response:
            self.status = response['status']
        if 'sub_confirm' in response:
            self.sub_confirm = response['sub_confirm']
