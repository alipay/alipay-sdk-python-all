#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupMemberInfo import GroupMemberInfo


class AlipaySocialBaseGroupQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseGroupQueryResponse, self).__init__()
        self._group_id = None
        self._group_member_count = None
        self._group_members = None
        self._group_name = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_member_count(self):
        return self._group_member_count

    @group_member_count.setter
    def group_member_count(self, value):
        self._group_member_count = value
    @property
    def group_members(self):
        return self._group_members

    @group_members.setter
    def group_members(self, value):
        if isinstance(value, list):
            self._group_members = list()
            for i in value:
                if isinstance(i, GroupMemberInfo):
                    self._group_members.append(i)
                else:
                    self._group_members.append(GroupMemberInfo.from_alipay_dict(i))
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseGroupQueryResponse, self).parse_response_content(response_content)
        if 'group_id' in response:
            self.group_id = response['group_id']
        if 'group_member_count' in response:
            self.group_member_count = response['group_member_count']
        if 'group_members' in response:
            self.group_members = response['group_members']
        if 'group_name' in response:
            self.group_name = response['group_name']
