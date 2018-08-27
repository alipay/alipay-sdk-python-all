#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupInfo import GroupInfo
from alipay.aop.api.domain.MemberInfo import MemberInfo


class AlipaySocialBaseChatGroupCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseChatGroupCreateResponse, self).__init__()
        self._group_info = None
        self._member_infos = None

    @property
    def group_info(self):
        return self._group_info

    @group_info.setter
    def group_info(self, value):
        if isinstance(value, GroupInfo):
            self._group_info = value
        else:
            self._group_info = GroupInfo.from_alipay_dict(value)
    @property
    def member_infos(self):
        return self._member_infos

    @member_infos.setter
    def member_infos(self, value):
        if isinstance(value, list):
            self._member_infos = list()
            for i in value:
                if isinstance(i, MemberInfo):
                    self._member_infos.append(i)
                else:
                    self._member_infos.append(MemberInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseChatGroupCreateResponse, self).parse_response_content(response_content)
        if 'group_info' in response:
            self.group_info = response['group_info']
        if 'member_infos' in response:
            self.member_infos = response['member_infos']
