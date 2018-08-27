#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QueryInstBillInfo import QueryInstBillInfo


class AlipayEbppBillSearchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppBillSearchResponse, self).__init__()
        self._cachekey = None
        self._inst_bill_info_list = None

    @property
    def cachekey(self):
        return self._cachekey

    @cachekey.setter
    def cachekey(self, value):
        self._cachekey = value
    @property
    def inst_bill_info_list(self):
        return self._inst_bill_info_list

    @inst_bill_info_list.setter
    def inst_bill_info_list(self, value):
        if isinstance(value, list):
            self._inst_bill_info_list = list()
            for i in value:
                if isinstance(i, QueryInstBillInfo):
                    self._inst_bill_info_list.append(i)
                else:
                    self._inst_bill_info_list.append(QueryInstBillInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppBillSearchResponse, self).parse_response_content(response_content)
        if 'cachekey' in response:
            self.cachekey = response['cachekey']
        if 'inst_bill_info_list' in response:
            self.inst_bill_info_list = response['inst_bill_info_list']
