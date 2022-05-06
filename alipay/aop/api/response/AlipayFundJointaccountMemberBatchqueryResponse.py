#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JointAccountMemberDTO import JointAccountMemberDTO


class AlipayFundJointaccountMemberBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountMemberBatchqueryResponse, self).__init__()
        self._account_id = None
        self._member_list = None
        self._page_num = None
        self._page_size = None
        self._total_count = None
        self._total_page_count = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def member_list(self):
        return self._member_list

    @member_list.setter
    def member_list(self, value):
        if isinstance(value, list):
            self._member_list = list()
            for i in value:
                if isinstance(i, JointAccountMemberDTO):
                    self._member_list.append(i)
                else:
                    self._member_list.append(JointAccountMemberDTO.from_alipay_dict(i))
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_page_count(self):
        return self._total_page_count

    @total_page_count.setter
    def total_page_count(self, value):
        self._total_page_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountMemberBatchqueryResponse, self).parse_response_content(response_content)
        if 'account_id' in response:
            self.account_id = response['account_id']
        if 'member_list' in response:
            self.member_list = response['member_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'total_page_count' in response:
            self.total_page_count = response['total_page_count']
