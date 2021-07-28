#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JointAccountQuotaRespDTO import JointAccountQuotaRespDTO


class AlipayFundJointaccountQuotaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountQuotaQueryResponse, self).__init__()
        self._account_id = None
        self._account_quota = None
        self._biz_scene = None
        self._member_id = None
        self._product_code = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def account_quota(self):
        return self._account_quota

    @account_quota.setter
    def account_quota(self, value):
        if isinstance(value, list):
            self._account_quota = list()
            for i in value:
                if isinstance(i, JointAccountQuotaRespDTO):
                    self._account_quota.append(i)
                else:
                    self._account_quota.append(JointAccountQuotaRespDTO.from_alipay_dict(i))
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountQuotaQueryResponse, self).parse_response_content(response_content)
        if 'account_id' in response:
            self.account_id = response['account_id']
        if 'account_quota' in response:
            self.account_quota = response['account_quota']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'member_id' in response:
            self.member_id = response['member_id']
        if 'product_code' in response:
            self.product_code = response['product_code']
