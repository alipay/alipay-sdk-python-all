#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupInfo import GroupInfo


class AlipaySocialBaseChatGroupsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseChatGroupsQueryResponse, self).__init__()
        self._group_infos = None
        self._has_more = None
        self._last_key = None

    @property
    def group_infos(self):
        return self._group_infos

    @group_infos.setter
    def group_infos(self, value):
        if isinstance(value, list):
            self._group_infos = list()
            for i in value:
                if isinstance(i, GroupInfo):
                    self._group_infos.append(i)
                else:
                    self._group_infos.append(GroupInfo.from_alipay_dict(i))
    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def last_key(self):
        return self._last_key

    @last_key.setter
    def last_key(self, value):
        self._last_key = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseChatGroupsQueryResponse, self).parse_response_content(response_content)
        if 'group_infos' in response:
            self.group_infos = response['group_infos']
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'last_key' in response:
            self.last_key = response['last_key']
