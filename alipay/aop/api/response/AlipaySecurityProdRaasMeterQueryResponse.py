#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RaasMeterSyncData import RaasMeterSyncData


class AlipaySecurityProdRaasMeterQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdRaasMeterQueryResponse, self).__init__()
        self._biz_report_datas = None
        self._total_num = None

    @property
    def biz_report_datas(self):
        return self._biz_report_datas

    @biz_report_datas.setter
    def biz_report_datas(self, value):
        if isinstance(value, list):
            self._biz_report_datas = list()
            for i in value:
                if isinstance(i, RaasMeterSyncData):
                    self._biz_report_datas.append(i)
                else:
                    self._biz_report_datas.append(RaasMeterSyncData.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdRaasMeterQueryResponse, self).parse_response_content(response_content)
        if 'biz_report_datas' in response:
            self.biz_report_datas = response['biz_report_datas']
        if 'total_num' in response:
            self.total_num = response['total_num']
