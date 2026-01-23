#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VerifyResultInfo import VerifyResultInfo
from alipay.aop.api.domain.VerifyResultInfo import VerifyResultInfo
from alipay.aop.api.domain.VerifyResultInfo import VerifyResultInfo


class AlipayOfflineProviderNpassporterVerifyresultinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderNpassporterVerifyresultinfoQueryResponse, self).__init__()
        self._default_verify_issue_info_list = None
        self._recent_verify_issue_info_list = None
        self._verify_issue_info_list = None

    @property
    def default_verify_issue_info_list(self):
        return self._default_verify_issue_info_list

    @default_verify_issue_info_list.setter
    def default_verify_issue_info_list(self, value):
        if isinstance(value, list):
            self._default_verify_issue_info_list = list()
            for i in value:
                if isinstance(i, VerifyResultInfo):
                    self._default_verify_issue_info_list.append(i)
                else:
                    self._default_verify_issue_info_list.append(VerifyResultInfo.from_alipay_dict(i))
    @property
    def recent_verify_issue_info_list(self):
        return self._recent_verify_issue_info_list

    @recent_verify_issue_info_list.setter
    def recent_verify_issue_info_list(self, value):
        if isinstance(value, list):
            self._recent_verify_issue_info_list = list()
            for i in value:
                if isinstance(i, VerifyResultInfo):
                    self._recent_verify_issue_info_list.append(i)
                else:
                    self._recent_verify_issue_info_list.append(VerifyResultInfo.from_alipay_dict(i))
    @property
    def verify_issue_info_list(self):
        return self._verify_issue_info_list

    @verify_issue_info_list.setter
    def verify_issue_info_list(self, value):
        if isinstance(value, list):
            self._verify_issue_info_list = list()
            for i in value:
                if isinstance(i, VerifyResultInfo):
                    self._verify_issue_info_list.append(i)
                else:
                    self._verify_issue_info_list.append(VerifyResultInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderNpassporterVerifyresultinfoQueryResponse, self).parse_response_content(response_content)
        if 'default_verify_issue_info_list' in response:
            self.default_verify_issue_info_list = response['default_verify_issue_info_list']
        if 'recent_verify_issue_info_list' in response:
            self.recent_verify_issue_info_list = response['recent_verify_issue_info_list']
        if 'verify_issue_info_list' in response:
            self.verify_issue_info_list = response['verify_issue_info_list']
