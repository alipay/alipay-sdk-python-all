#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QuotaModifyDetail import QuotaModifyDetail


class AlipayFundAgreementQuotaModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAgreementQuotaModifyResponse, self).__init__()
        self._quota_modify_detail_list = None

    @property
    def quota_modify_detail_list(self):
        return self._quota_modify_detail_list

    @quota_modify_detail_list.setter
    def quota_modify_detail_list(self, value):
        if isinstance(value, list):
            self._quota_modify_detail_list = list()
            for i in value:
                if isinstance(i, QuotaModifyDetail):
                    self._quota_modify_detail_list.append(i)
                else:
                    self._quota_modify_detail_list.append(QuotaModifyDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundAgreementQuotaModifyResponse, self).parse_response_content(response_content)
        if 'quota_modify_detail_list' in response:
            self.quota_modify_detail_list = response['quota_modify_detail_list']
