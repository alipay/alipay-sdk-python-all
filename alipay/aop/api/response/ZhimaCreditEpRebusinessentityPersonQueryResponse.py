#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RebusinessEntityRelation import RebusinessEntityRelation


class ZhimaCreditEpRebusinessentityPersonQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpRebusinessentityPersonQueryResponse, self).__init__()
        self._data = None
        self._person_name = None
        self._uscc = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, RebusinessEntityRelation):
            self._data = value
        else:
            self._data = RebusinessEntityRelation.from_alipay_dict(value)
    @property
    def person_name(self):
        return self._person_name

    @person_name.setter
    def person_name(self, value):
        self._person_name = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpRebusinessentityPersonQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'person_name' in response:
            self.person_name = response['person_name']
        if 'uscc' in response:
            self.uscc = response['uscc']
