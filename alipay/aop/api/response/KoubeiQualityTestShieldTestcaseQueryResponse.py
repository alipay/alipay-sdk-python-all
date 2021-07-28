#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TestCaseDomain import TestCaseDomain


class KoubeiQualityTestShieldTestcaseQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiQualityTestShieldTestcaseQueryResponse, self).__init__()
        self._case_list = None
        self._ext_infos = None

    @property
    def case_list(self):
        return self._case_list

    @case_list.setter
    def case_list(self, value):
        if isinstance(value, list):
            self._case_list = list()
            for i in value:
                if isinstance(i, TestCaseDomain):
                    self._case_list.append(i)
                else:
                    self._case_list.append(TestCaseDomain.from_alipay_dict(i))
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value

    def parse_response_content(self, response_content):
        response = super(KoubeiQualityTestShieldTestcaseQueryResponse, self).parse_response_content(response_content)
        if 'case_list' in response:
            self.case_list = response['case_list']
        if 'ext_infos' in response:
            self.ext_infos = response['ext_infos']
