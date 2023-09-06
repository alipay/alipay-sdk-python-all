#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SportsRecordInfo import SportsRecordInfo


class AlipayUserSportsrecordQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserSportsrecordQueryResponse, self).__init__()
        self._has_more = None
        self._record_list = None

    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def record_list(self):
        return self._record_list

    @record_list.setter
    def record_list(self, value):
        if isinstance(value, list):
            self._record_list = list()
            for i in value:
                if isinstance(i, SportsRecordInfo):
                    self._record_list.append(i)
                else:
                    self._record_list.append(SportsRecordInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserSportsrecordQueryResponse, self).parse_response_content(response_content)
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'record_list' in response:
            self.record_list = response['record_list']
