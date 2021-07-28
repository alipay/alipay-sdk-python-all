#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JointAccountQuotaRespDTO import JointAccountQuotaRespDTO
from alipay.aop.api.domain.AuthorizedRuleDTO import AuthorizedRuleDTO


class AlipayFundJointaccountDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountDetailQueryResponse, self).__init__()
        self._account_id = None
        self._account_name = None
        self._account_quota = None
        self._authorized_rule = None
        self._biz_scene = None
        self._product_code = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
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
    def authorized_rule(self):
        return self._authorized_rule

    @authorized_rule.setter
    def authorized_rule(self, value):
        if isinstance(value, AuthorizedRuleDTO):
            self._authorized_rule = value
        else:
            self._authorized_rule = AuthorizedRuleDTO.from_alipay_dict(value)
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
        response = super(AlipayFundJointaccountDetailQueryResponse, self).parse_response_content(response_content)
        if 'account_id' in response:
            self.account_id = response['account_id']
        if 'account_name' in response:
            self.account_name = response['account_name']
        if 'account_quota' in response:
            self.account_quota = response['account_quota']
        if 'authorized_rule' in response:
            self.authorized_rule = response['authorized_rule']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'product_code' in response:
            self.product_code = response['product_code']
