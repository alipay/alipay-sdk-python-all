#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OBBatchCustomerIdentityDTO import OBBatchCustomerIdentityDTO


class AnttechOceanbaseObcustomercoreBatchuserentityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseObcustomercoreBatchuserentityQueryResponse, self).__init__()
        self._customer_identity_list = None

    @property
    def customer_identity_list(self):
        return self._customer_identity_list

    @customer_identity_list.setter
    def customer_identity_list(self, value):
        if isinstance(value, list):
            self._customer_identity_list = list()
            for i in value:
                if isinstance(i, OBBatchCustomerIdentityDTO):
                    self._customer_identity_list.append(i)
                else:
                    self._customer_identity_list.append(OBBatchCustomerIdentityDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseObcustomercoreBatchuserentityQueryResponse, self).parse_response_content(response_content)
        if 'customer_identity_list' in response:
            self.customer_identity_list = response['customer_identity_list']
