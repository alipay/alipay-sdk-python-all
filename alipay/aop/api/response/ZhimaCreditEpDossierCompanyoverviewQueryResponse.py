#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CompanyOverviewInfo import CompanyOverviewInfo


class ZhimaCreditEpDossierCompanyoverviewQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpDossierCompanyoverviewQueryResponse, self).__init__()
        self._company_overview_info = None

    @property
    def company_overview_info(self):
        return self._company_overview_info

    @company_overview_info.setter
    def company_overview_info(self, value):
        if isinstance(value, CompanyOverviewInfo):
            self._company_overview_info = value
        else:
            self._company_overview_info = CompanyOverviewInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpDossierCompanyoverviewQueryResponse, self).parse_response_content(response_content)
        if 'company_overview_info' in response:
            self.company_overview_info = response['company_overview_info']
