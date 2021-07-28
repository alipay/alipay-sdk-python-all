#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JointAccountMemberRespDTO import JointAccountMemberRespDTO


class AlipayFundJointaccountMemberQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountMemberQueryResponse, self).__init__()
        self._account_id = None
        self._biz_scene = None
        self._member_list = None
        self._page_num = None
        self._page_size = None
        self._product_code = None
        self._total_page_count = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def member_list(self):
        return self._member_list

    @member_list.setter
    def member_list(self, value):
        if isinstance(value, list):
            self._member_list = list()
            for i in value:
                if isinstance(i, JointAccountMemberRespDTO):
                    self._member_list.append(i)
                else:
                    self._member_list.append(JointAccountMemberRespDTO.from_alipay_dict(i))
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
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def total_page_count(self):
        return self._total_page_count

    @total_page_count.setter
    def total_page_count(self, value):
        self._total_page_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountMemberQueryResponse, self).parse_response_content(response_content)
        if 'account_id' in response:
            self.account_id = response['account_id']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'member_list' in response:
            self.member_list = response['member_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'total_page_count' in response:
            self.total_page_count = response['total_page_count']
