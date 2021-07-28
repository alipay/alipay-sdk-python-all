#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MemberStatusRespDTO import MemberStatusRespDTO


class AlipayFundJointaccountMemberConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountMemberConsultResponse, self).__init__()
        self._account_id = None
        self._code = None
        self._member_list = None
        self._msg = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def member_list(self):
        return self._member_list

    @member_list.setter
    def member_list(self, value):
        if isinstance(value, list):
            self._member_list = list()
            for i in value:
                if isinstance(i, MemberStatusRespDTO):
                    self._member_list.append(i)
                else:
                    self._member_list.append(MemberStatusRespDTO.from_alipay_dict(i))
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountMemberConsultResponse, self).parse_response_content(response_content)
        if 'account_id' in response:
            self.account_id = response['account_id']
        if 'code' in response:
            self.code = response['code']
        if 'member_list' in response:
            self.member_list = response['member_list']
        if 'msg' in response:
            self.msg = response['msg']
