#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromotePageStatistic import PromotePageStatistic


class AlipayDataDataserviceAdPromotepagestatisticQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdPromotepagestatisticQueryResponse, self).__init__()
        self._collectinfo_list = None

    @property
    def collectinfo_list(self):
        return self._collectinfo_list

    @collectinfo_list.setter
    def collectinfo_list(self, value):
        if isinstance(value, list):
            self._collectinfo_list = list()
            for i in value:
                if isinstance(i, PromotePageStatistic):
                    self._collectinfo_list.append(i)
                else:
                    self._collectinfo_list.append(PromotePageStatistic.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdPromotepagestatisticQueryResponse, self).parse_response_content(response_content)
        if 'collectinfo_list' in response:
            self.collectinfo_list = response['collectinfo_list']
