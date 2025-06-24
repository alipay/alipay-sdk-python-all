#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MemberArchiveOpenApiInfoDTO import MemberArchiveOpenApiInfoDTO


class AlipayCommerceMedicalCommercialArchiveQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCommercialArchiveQueryResponse, self).__init__()
        self._member_archive_list = None
        self._total = None

    @property
    def member_archive_list(self):
        return self._member_archive_list

    @member_archive_list.setter
    def member_archive_list(self, value):
        if isinstance(value, list):
            self._member_archive_list = list()
            for i in value:
                if isinstance(i, MemberArchiveOpenApiInfoDTO):
                    self._member_archive_list.append(i)
                else:
                    self._member_archive_list.append(MemberArchiveOpenApiInfoDTO.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCommercialArchiveQueryResponse, self).parse_response_content(response_content)
        if 'member_archive_list' in response:
            self.member_archive_list = response['member_archive_list']
        if 'total' in response:
            self.total = response['total']
