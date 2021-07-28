#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LogisticsCompanyDTO import LogisticsCompanyDTO


class AlipayOpenInstantdeliveryLogisticsBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenInstantdeliveryLogisticsBatchqueryResponse, self).__init__()
        self._logistics_companys = None

    @property
    def logistics_companys(self):
        return self._logistics_companys

    @logistics_companys.setter
    def logistics_companys(self, value):
        if isinstance(value, list):
            self._logistics_companys = list()
            for i in value:
                if isinstance(i, LogisticsCompanyDTO):
                    self._logistics_companys.append(i)
                else:
                    self._logistics_companys.append(LogisticsCompanyDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenInstantdeliveryLogisticsBatchqueryResponse, self).parse_response_content(response_content)
        if 'logistics_companys' in response:
            self.logistics_companys = response['logistics_companys']
