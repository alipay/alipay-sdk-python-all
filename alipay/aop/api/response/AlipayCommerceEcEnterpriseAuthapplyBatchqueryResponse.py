#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EnterpriseAuthApplyDTO import EnterpriseAuthApplyDTO


class AlipayCommerceEcEnterpriseAuthapplyBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEnterpriseAuthapplyBatchqueryResponse, self).__init__()
        self._auth_apply_list = None

    @property
    def auth_apply_list(self):
        return self._auth_apply_list

    @auth_apply_list.setter
    def auth_apply_list(self, value):
        if isinstance(value, list):
            self._auth_apply_list = list()
            for i in value:
                if isinstance(i, EnterpriseAuthApplyDTO):
                    self._auth_apply_list.append(i)
                else:
                    self._auth_apply_list.append(EnterpriseAuthApplyDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEnterpriseAuthapplyBatchqueryResponse, self).parse_response_content(response_content)
        if 'auth_apply_list' in response:
            self.auth_apply_list = response['auth_apply_list']
