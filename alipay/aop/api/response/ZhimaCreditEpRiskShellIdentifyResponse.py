#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShellCompanyFeatureDetail import ShellCompanyFeatureDetail
from alipay.aop.api.domain.ShellCompanyGsChangeDetail import ShellCompanyGsChangeDetail


class ZhimaCreditEpRiskShellIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpRiskShellIdentifyResponse, self).__init__()
        self._shell_company_features = None
        self._shell_company_gs_changes = None

    @property
    def shell_company_features(self):
        return self._shell_company_features

    @shell_company_features.setter
    def shell_company_features(self, value):
        if isinstance(value, list):
            self._shell_company_features = list()
            for i in value:
                if isinstance(i, ShellCompanyFeatureDetail):
                    self._shell_company_features.append(i)
                else:
                    self._shell_company_features.append(ShellCompanyFeatureDetail.from_alipay_dict(i))
    @property
    def shell_company_gs_changes(self):
        return self._shell_company_gs_changes

    @shell_company_gs_changes.setter
    def shell_company_gs_changes(self, value):
        if isinstance(value, list):
            self._shell_company_gs_changes = list()
            for i in value:
                if isinstance(i, ShellCompanyGsChangeDetail):
                    self._shell_company_gs_changes.append(i)
                else:
                    self._shell_company_gs_changes.append(ShellCompanyGsChangeDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpRiskShellIdentifyResponse, self).parse_response_content(response_content)
        if 'shell_company_features' in response:
            self.shell_company_features = response['shell_company_features']
        if 'shell_company_gs_changes' in response:
            self.shell_company_gs_changes = response['shell_company_gs_changes']
