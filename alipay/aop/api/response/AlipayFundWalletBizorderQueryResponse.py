#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletBizorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletBizorderQueryResponse, self).__init__()
        self._bill_no = None
        self._biz_amount = None
        self._biz_type = None
        self._display_name = None
        self._ext_info = None
        self._gmt_create = None
        self._gmt_modified = None
        self._memo = None
        self._order_id = None
        self._status = None
        self._sub_biz_type = None
        self._title = None
        self._wallet_id = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def biz_amount(self):
        return self._biz_amount

    @biz_amount.setter
    def biz_amount(self, value):
        self._biz_amount = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def wallet_id(self):
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, value):
        self._wallet_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletBizorderQueryResponse, self).parse_response_content(response_content)
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'biz_amount' in response:
            self.biz_amount = response['biz_amount']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'display_name' in response:
            self.display_name = response['display_name']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'memo' in response:
            self.memo = response['memo']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'status' in response:
            self.status = response['status']
        if 'sub_biz_type' in response:
            self.sub_biz_type = response['sub_biz_type']
        if 'title' in response:
            self.title = response['title']
        if 'wallet_id' in response:
            self.wallet_id = response['wallet_id']
