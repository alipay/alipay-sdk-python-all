#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MemberVO import MemberVO


class AlipayCommerceMedicalEbbenefitMemberQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalEbbenefitMemberQueryResponse, self).__init__()
        self._member = None

    @property
    def member(self):
        return self._member

    @member.setter
    def member(self, value):
        if isinstance(value, list):
            self._member = list()
            for i in value:
                if isinstance(i, MemberVO):
                    self._member.append(i)
                else:
                    self._member.append(MemberVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalEbbenefitMemberQueryResponse, self).parse_response_content(response_content)
        if 'member' in response:
            self.member = response['member']
