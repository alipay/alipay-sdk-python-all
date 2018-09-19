#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiSignQueryResponse import OpenApiSignQueryResponse


class AlipayUserAgreementBatchQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementBatchQueryResponse, self).__init__()
        self._usage_agreement_info_list = None

    @property
    def usage_agreement_info_list(self):
        return self._usage_agreement_info_list

    @usage_agreement_info_list.setter
    def usage_agreement_info_list(self, value):
        if isinstance(value, list):
            self._usage_agreement_info_list = list()
            for i in value:
                if isinstance(i, OpenApiSignQueryResponse):
                    self._usage_agreement_info_list.append(i)
                else:
                    self._usage_agreement_info_list.append(OpenApiSignQueryResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementBatchQueryResponse, self).parse_response_content(response_content)
        if 'usage_agreement_info_list' in response:
            self.usage_agreement_info_list = response['usage_agreement_info_list']
