#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftSkuinfoSkuidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftSkuinfoSkuidQueryResponse, self).__init__()
        self._quantity = None
        self._quantity_type = None
        self._sku_desc = None
        self._sku_enable_send = None
        self._sku_id = None
        self._sku_mini_fileurl = None
        self._sku_name = None
        self._sku_status = None
        self._sku_type = None

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def quantity_type(self):
        return self._quantity_type

    @quantity_type.setter
    def quantity_type(self, value):
        self._quantity_type = value
    @property
    def sku_desc(self):
        return self._sku_desc

    @sku_desc.setter
    def sku_desc(self, value):
        self._sku_desc = value
    @property
    def sku_enable_send(self):
        return self._sku_enable_send

    @sku_enable_send.setter
    def sku_enable_send(self, value):
        self._sku_enable_send = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_mini_fileurl(self):
        return self._sku_mini_fileurl

    @sku_mini_fileurl.setter
    def sku_mini_fileurl(self, value):
        self._sku_mini_fileurl = value
    @property
    def sku_name(self):
        return self._sku_name

    @sku_name.setter
    def sku_name(self, value):
        self._sku_name = value
    @property
    def sku_status(self):
        return self._sku_status

    @sku_status.setter
    def sku_status(self, value):
        self._sku_status = value
    @property
    def sku_type(self):
        return self._sku_type

    @sku_type.setter
    def sku_type(self, value):
        self._sku_type = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftSkuinfoSkuidQueryResponse, self).parse_response_content(response_content)
        if 'quantity' in response:
            self.quantity = response['quantity']
        if 'quantity_type' in response:
            self.quantity_type = response['quantity_type']
        if 'sku_desc' in response:
            self.sku_desc = response['sku_desc']
        if 'sku_enable_send' in response:
            self.sku_enable_send = response['sku_enable_send']
        if 'sku_id' in response:
            self.sku_id = response['sku_id']
        if 'sku_mini_fileurl' in response:
            self.sku_mini_fileurl = response['sku_mini_fileurl']
        if 'sku_name' in response:
            self.sku_name = response['sku_name']
        if 'sku_status' in response:
            self.sku_status = response['sku_status']
        if 'sku_type' in response:
            self.sku_type = response['sku_type']
