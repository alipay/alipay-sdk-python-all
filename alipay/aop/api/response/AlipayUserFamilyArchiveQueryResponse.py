#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FamilyArchiveDetail import FamilyArchiveDetail


class AlipayUserFamilyArchiveQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserFamilyArchiveQueryResponse, self).__init__()
        self._archive_list = None

    @property
    def archive_list(self):
        return self._archive_list

    @archive_list.setter
    def archive_list(self, value):
        if isinstance(value, list):
            self._archive_list = list()
            for i in value:
                if isinstance(i, FamilyArchiveDetail):
                    self._archive_list.append(i)
                else:
                    self._archive_list.append(FamilyArchiveDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserFamilyArchiveQueryResponse, self).parse_response_content(response_content)
        if 'archive_list' in response:
            self.archive_list = response['archive_list']
