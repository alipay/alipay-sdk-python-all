#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduRosterInfo import EduRosterInfo


class AlipayCommerceEducateRosterInfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateRosterInfoBatchqueryResponse, self).__init__()
        self._roster_list = None
        self._total_num = None

    @property
    def roster_list(self):
        return self._roster_list

    @roster_list.setter
    def roster_list(self, value):
        if isinstance(value, list):
            self._roster_list = list()
            for i in value:
                if isinstance(i, EduRosterInfo):
                    self._roster_list.append(i)
                else:
                    self._roster_list.append(EduRosterInfo.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateRosterInfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'roster_list' in response:
            self.roster_list = response['roster_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
