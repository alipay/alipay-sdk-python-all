#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChildCertInfo import ChildCertInfo
from alipay.aop.api.domain.NextUrl import NextUrl
from alipay.aop.api.domain.RelationVO import RelationVO


class AlipayCommerceKidsAccountConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceKidsAccountConsultResponse, self).__init__()
        self._can_open = None
        self._child_info = None
        self._next_url = None
        self._relation_limit = None
        self._relation_list = None

    @property
    def can_open(self):
        return self._can_open

    @can_open.setter
    def can_open(self, value):
        self._can_open = value
    @property
    def child_info(self):
        return self._child_info

    @child_info.setter
    def child_info(self, value):
        if isinstance(value, ChildCertInfo):
            self._child_info = value
        else:
            self._child_info = ChildCertInfo.from_alipay_dict(value)
    @property
    def next_url(self):
        return self._next_url

    @next_url.setter
    def next_url(self, value):
        if isinstance(value, NextUrl):
            self._next_url = value
        else:
            self._next_url = NextUrl.from_alipay_dict(value)
    @property
    def relation_limit(self):
        return self._relation_limit

    @relation_limit.setter
    def relation_limit(self, value):
        self._relation_limit = value
    @property
    def relation_list(self):
        return self._relation_list

    @relation_list.setter
    def relation_list(self, value):
        if isinstance(value, list):
            self._relation_list = list()
            for i in value:
                if isinstance(i, RelationVO):
                    self._relation_list.append(i)
                else:
                    self._relation_list.append(RelationVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceKidsAccountConsultResponse, self).parse_response_content(response_content)
        if 'can_open' in response:
            self.can_open = response['can_open']
        if 'child_info' in response:
            self.child_info = response['child_info']
        if 'next_url' in response:
            self.next_url = response['next_url']
        if 'relation_limit' in response:
            self.relation_limit = response['relation_limit']
        if 'relation_list' in response:
            self.relation_list = response['relation_list']
