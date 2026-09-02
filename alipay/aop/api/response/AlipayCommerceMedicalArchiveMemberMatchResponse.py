#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MatchedMemberDTO import MatchedMemberDTO


class AlipayCommerceMedicalArchiveMemberMatchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalArchiveMemberMatchResponse, self).__init__()
        self._is_matched_self = None
        self._matched_member_list = None

    @property
    def is_matched_self(self):
        return self._is_matched_self

    @is_matched_self.setter
    def is_matched_self(self, value):
        self._is_matched_self = value
    @property
    def matched_member_list(self):
        return self._matched_member_list

    @matched_member_list.setter
    def matched_member_list(self, value):
        if isinstance(value, list):
            self._matched_member_list = list()
            for i in value:
                if isinstance(i, MatchedMemberDTO):
                    self._matched_member_list.append(i)
                else:
                    self._matched_member_list.append(MatchedMemberDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalArchiveMemberMatchResponse, self).parse_response_content(response_content)
        if 'is_matched_self' in response:
            self.is_matched_self = response['is_matched_self']
        if 'matched_member_list' in response:
            self.matched_member_list = response['matched_member_list']
