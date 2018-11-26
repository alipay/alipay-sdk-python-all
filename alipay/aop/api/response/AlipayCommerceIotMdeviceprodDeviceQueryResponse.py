#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotMdeviceprodDeviceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotMdeviceprodDeviceQueryResponse, self).__init__()
        self._bind_status = None
        self._biz_tid = None
        self._biz_type = None
        self._ext_info = None
        self._isv_pid = None
        self._item_id = None
        self._merchant_pid = None
        self._shop_id = None
        self._status = None
        self._supplier_sn = None

    @property
    def bind_status(self):
        return self._bind_status

    @bind_status.setter
    def bind_status(self, value):
        self._bind_status = value
    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def supplier_sn(self):
        return self._supplier_sn

    @supplier_sn.setter
    def supplier_sn(self, value):
        self._supplier_sn = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotMdeviceprodDeviceQueryResponse, self).parse_response_content(response_content)
        if 'bind_status' in response:
            self.bind_status = response['bind_status']
        if 'biz_tid' in response:
            self.biz_tid = response['biz_tid']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'isv_pid' in response:
            self.isv_pid = response['isv_pid']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'merchant_pid' in response:
            self.merchant_pid = response['merchant_pid']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'status' in response:
            self.status = response['status']
        if 'supplier_sn' in response:
            self.supplier_sn = response['supplier_sn']
