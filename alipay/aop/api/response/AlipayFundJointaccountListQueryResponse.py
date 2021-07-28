#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JointAccountDTO import JointAccountDTO


class AlipayFundJointaccountListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountListQueryResponse, self).__init__()
        self._account_list = None
        self._biz_scene = None
        self._product_code = None

    @property
    def account_list(self):
        return self._account_list

    @account_list.setter
    def account_list(self, value):
        if isinstance(value, list):
            self._account_list = list()
            for i in value:
                if isinstance(i, JointAccountDTO):
                    self._account_list.append(i)
                else:
                    self._account_list.append(JointAccountDTO.from_alipay_dict(i))
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountListQueryResponse, self).parse_response_content(response_content)
        if 'account_list' in response:
            self.account_list = response['account_list']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'product_code' in response:
            self.product_code = response['product_code']
