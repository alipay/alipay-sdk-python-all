#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppCustomGrayGroupDto import MiniAppCustomGrayGroupDto
from alipay.aop.api.domain.MiniAppCustomGrayMemberInfoDto import MiniAppCustomGrayMemberInfoDto


class AlipayOpenMiniInnerversionCustomgrayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionCustomgrayQueryResponse, self).__init__()
        self._gray_groups = None
        self._member_infos = None
        self._total_count = None

    @property
    def gray_groups(self):
        return self._gray_groups

    @gray_groups.setter
    def gray_groups(self, value):
        if isinstance(value, MiniAppCustomGrayGroupDto):
            self._gray_groups = value
        else:
            self._gray_groups = MiniAppCustomGrayGroupDto.from_alipay_dict(value)
    @property
    def member_infos(self):
        return self._member_infos

    @member_infos.setter
    def member_infos(self, value):
        if isinstance(value, list):
            self._member_infos = list()
            for i in value:
                if isinstance(i, MiniAppCustomGrayMemberInfoDto):
                    self._member_infos.append(i)
                else:
                    self._member_infos.append(MiniAppCustomGrayMemberInfoDto.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionCustomgrayQueryResponse, self).parse_response_content(response_content)
        if 'gray_groups' in response:
            self.gray_groups = response['gray_groups']
        if 'member_infos' in response:
            self.member_infos = response['member_infos']
        if 'total_count' in response:
            self.total_count = response['total_count']
