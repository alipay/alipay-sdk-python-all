#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RiskFinishInfo import RiskFinishInfo


class AlipaySecurityProdRisktaskFinishinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdRisktaskFinishinfoQueryResponse, self).__init__()
        self._finish_info_list = None

    @property
    def finish_info_list(self):
        return self._finish_info_list

    @finish_info_list.setter
    def finish_info_list(self, value):
        if isinstance(value, list):
            self._finish_info_list = list()
            for i in value:
                if isinstance(i, RiskFinishInfo):
                    self._finish_info_list.append(i)
                else:
                    self._finish_info_list.append(RiskFinishInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdRisktaskFinishinfoQueryResponse, self).parse_response_content(response_content)
        if 'finish_info_list' in response:
            self.finish_info_list = response['finish_info_list']
