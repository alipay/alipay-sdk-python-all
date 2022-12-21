#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JointAccountQuotaRespDTO import JointAccountQuotaRespDTO


class AlipayFundEnterprisepayQuotaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundEnterprisepayQuotaQueryResponse, self).__init__()
        self._quota_list = None

    @property
    def quota_list(self):
        return self._quota_list

    @quota_list.setter
    def quota_list(self, value):
        if isinstance(value, list):
            self._quota_list = list()
            for i in value:
                if isinstance(i, JointAccountQuotaRespDTO):
                    self._quota_list.append(i)
                else:
                    self._quota_list.append(JointAccountQuotaRespDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundEnterprisepayQuotaQueryResponse, self).parse_response_content(response_content)
        if 'quota_list' in response:
            self.quota_list = response['quota_list']
