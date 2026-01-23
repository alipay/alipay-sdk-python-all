#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentKolDailyReportVO import RentKolDailyReportVO


class ZhimaOpenAppKolReportQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaOpenAppKolReportQueryResponse, self).__init__()
        self._report_list = None

    @property
    def report_list(self):
        return self._report_list

    @report_list.setter
    def report_list(self, value):
        if isinstance(value, list):
            self._report_list = list()
            for i in value:
                if isinstance(i, RentKolDailyReportVO):
                    self._report_list.append(i)
                else:
                    self._report_list.append(RentKolDailyReportVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZhimaOpenAppKolReportQueryResponse, self).parse_response_content(response_content)
        if 'report_list' in response:
            self.report_list = response['report_list']
