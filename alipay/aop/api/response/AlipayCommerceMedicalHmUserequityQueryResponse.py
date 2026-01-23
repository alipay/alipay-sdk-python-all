#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HmEquityInfo import HmEquityInfo


class AlipayCommerceMedicalHmUserequityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHmUserequityQueryResponse, self).__init__()
        self._equity_info_list = None

    @property
    def equity_info_list(self):
        return self._equity_info_list

    @equity_info_list.setter
    def equity_info_list(self, value):
        if isinstance(value, list):
            self._equity_info_list = list()
            for i in value:
                if isinstance(i, HmEquityInfo):
                    self._equity_info_list.append(i)
                else:
                    self._equity_info_list.append(HmEquityInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHmUserequityQueryResponse, self).parse_response_content(response_content)
        if 'equity_info_list' in response:
            self.equity_info_list = response['equity_info_list']
