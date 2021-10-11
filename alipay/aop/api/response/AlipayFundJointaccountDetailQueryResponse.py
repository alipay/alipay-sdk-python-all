#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JointAccountQuotaRespDTO import JointAccountQuotaRespDTO
from alipay.aop.api.domain.AuthorizedRuleDTO import AuthorizedRuleDTO
from alipay.aop.api.domain.InviteResultDTO import InviteResultDTO
from alipay.aop.api.domain.JointAccountMemberInfoRespDTO import JointAccountMemberInfoRespDTO


class AlipayFundJointaccountDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountDetailQueryResponse, self).__init__()
        self._account_id = None
        self._account_name = None
        self._account_quota = None
        self._account_status = None
        self._agreement_no = None
        self._authorized_rule = None
        self._available_balance = None
        self._biz_scene = None
        self._creator_id = None
        self._creator_out_id = None
        self._freeze_balance = None
        self._invite_result_list = None
        self._member_list = None
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
    def account_status(self):
        return self._account_status

    @account_status.setter
    def account_status(self, value):
        self._account_status = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
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
    def available_balance(self):
        return self._available_balance

    @available_balance.setter
    def available_balance(self, value):
        self._available_balance = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        self._creator_id = value
    @property
    def creator_out_id(self):
        return self._creator_out_id

    @creator_out_id.setter
    def creator_out_id(self, value):
        self._creator_out_id = value
    @property
    def freeze_balance(self):
        return self._freeze_balance

    @freeze_balance.setter
    def freeze_balance(self, value):
        self._freeze_balance = value
    @property
    def invite_result_list(self):
        return self._invite_result_list

    @invite_result_list.setter
    def invite_result_list(self, value):
        if isinstance(value, list):
            self._invite_result_list = list()
            for i in value:
                if isinstance(i, InviteResultDTO):
                    self._invite_result_list.append(i)
                else:
                    self._invite_result_list.append(InviteResultDTO.from_alipay_dict(i))
    @property
    def member_list(self):
        return self._member_list

    @member_list.setter
    def member_list(self, value):
        if isinstance(value, list):
            self._member_list = list()
            for i in value:
                if isinstance(i, JointAccountMemberInfoRespDTO):
                    self._member_list.append(i)
                else:
                    self._member_list.append(JointAccountMemberInfoRespDTO.from_alipay_dict(i))
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
        if 'account_status' in response:
            self.account_status = response['account_status']
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'authorized_rule' in response:
            self.authorized_rule = response['authorized_rule']
        if 'available_balance' in response:
            self.available_balance = response['available_balance']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'creator_id' in response:
            self.creator_id = response['creator_id']
        if 'creator_out_id' in response:
            self.creator_out_id = response['creator_out_id']
        if 'freeze_balance' in response:
            self.freeze_balance = response['freeze_balance']
        if 'invite_result_list' in response:
            self.invite_result_list = response['invite_result_list']
        if 'member_list' in response:
            self.member_list = response['member_list']
        if 'product_code' in response:
            self.product_code = response['product_code']
