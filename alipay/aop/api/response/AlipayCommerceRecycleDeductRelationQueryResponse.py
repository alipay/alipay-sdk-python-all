#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecycleDeductQueryVO import RecycleDeductQueryVO
from alipay.aop.api.domain.RecycleDeductSignVO import RecycleDeductSignVO


class AlipayCommerceRecycleDeductRelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleDeductRelationQueryResponse, self).__init__()
        self._deduct_list = None
        self._sign_list = None

    @property
    def deduct_list(self):
        return self._deduct_list

    @deduct_list.setter
    def deduct_list(self, value):
        if isinstance(value, list):
            self._deduct_list = list()
            for i in value:
                if isinstance(i, RecycleDeductQueryVO):
                    self._deduct_list.append(i)
                else:
                    self._deduct_list.append(RecycleDeductQueryVO.from_alipay_dict(i))
    @property
    def sign_list(self):
        return self._sign_list

    @sign_list.setter
    def sign_list(self, value):
        if isinstance(value, list):
            self._sign_list = list()
            for i in value:
                if isinstance(i, RecycleDeductSignVO):
                    self._sign_list.append(i)
                else:
                    self._sign_list.append(RecycleDeductSignVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleDeductRelationQueryResponse, self).parse_response_content(response_content)
        if 'deduct_list' in response:
            self.deduct_list = response['deduct_list']
        if 'sign_list' in response:
            self.sign_list = response['sign_list']
