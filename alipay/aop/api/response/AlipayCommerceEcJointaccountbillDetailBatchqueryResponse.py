#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JointAccountBillDetail import JointAccountBillDetail


class AlipayCommerceEcJointaccountbillDetailBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcJointaccountbillDetailBatchqueryResponse, self).__init__()
        self._bill_list = None
        self._biz_scene = None
        self._enterprise_id = None
        self._has_next_page = None
        self._page_num = None
        self._page_size = None

    @property
    def bill_list(self):
        return self._bill_list

    @bill_list.setter
    def bill_list(self, value):
        if isinstance(value, list):
            self._bill_list = list()
            for i in value:
                if isinstance(i, JointAccountBillDetail):
                    self._bill_list.append(i)
                else:
                    self._bill_list.append(JointAccountBillDetail.from_alipay_dict(i))
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def has_next_page(self):
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, value):
        self._has_next_page = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcJointaccountbillDetailBatchqueryResponse, self).parse_response_content(response_content)
        if 'bill_list' in response:
            self.bill_list = response['bill_list']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'enterprise_id' in response:
            self.enterprise_id = response['enterprise_id']
        if 'has_next_page' in response:
            self.has_next_page = response['has_next_page']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
