#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SummaryInfo import SummaryInfo


class AlipayOpenPublicSummaryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicSummaryQueryResponse, self).__init__()
        self._public_info_list = None

    @property
    def public_info_list(self):
        return self._public_info_list

    @public_info_list.setter
    def public_info_list(self, value):
        if isinstance(value, list):
            self._public_info_list = list()
            for i in value:
                if isinstance(i, SummaryInfo):
                    self._public_info_list.append(i)
                else:
                    self._public_info_list.append(SummaryInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicSummaryQueryResponse, self).parse_response_content(response_content)
        if 'public_info_list' in response:
            self.public_info_list = response['public_info_list']
