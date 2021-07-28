#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayGongyiAddressTest import AlipayGongyiAddressTest
from alipay.aop.api.domain.OuterShopDO import OuterShopDO
from alipay.aop.api.domain.AlipayGongyiModelTest import AlipayGongyiModelTest


class AlipayOpenAppGongyiTestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppGongyiTestQueryResponse, self).__init__()
        self._createdate = None
        self._shopaddress = None
        self._shopinfo = None
        self._shopname = None
        self._shoprecord = None

    @property
    def createdate(self):
        return self._createdate

    @createdate.setter
    def createdate(self, value):
        self._createdate = value
    @property
    def shopaddress(self):
        return self._shopaddress

    @shopaddress.setter
    def shopaddress(self, value):
        if isinstance(value, AlipayGongyiAddressTest):
            self._shopaddress = value
        else:
            self._shopaddress = AlipayGongyiAddressTest.from_alipay_dict(value)
    @property
    def shopinfo(self):
        return self._shopinfo

    @shopinfo.setter
    def shopinfo(self, value):
        if isinstance(value, OuterShopDO):
            self._shopinfo = value
        else:
            self._shopinfo = OuterShopDO.from_alipay_dict(value)
    @property
    def shopname(self):
        return self._shopname

    @shopname.setter
    def shopname(self, value):
        self._shopname = value
    @property
    def shoprecord(self):
        return self._shoprecord

    @shoprecord.setter
    def shoprecord(self, value):
        if isinstance(value, AlipayGongyiModelTest):
            self._shoprecord = value
        else:
            self._shoprecord = AlipayGongyiModelTest.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppGongyiTestQueryResponse, self).parse_response_content(response_content)
        if 'createdate' in response:
            self.createdate = response['createdate']
        if 'shopaddress' in response:
            self.shopaddress = response['shopaddress']
        if 'shopinfo' in response:
            self.shopinfo = response['shopinfo']
        if 'shopname' in response:
            self.shopname = response['shopname']
        if 'shoprecord' in response:
            self.shoprecord = response['shoprecord']
