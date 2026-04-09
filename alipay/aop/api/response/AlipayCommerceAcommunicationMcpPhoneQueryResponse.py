#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderStatus import OrderStatus


class AlipayCommerceAcommunicationMcpPhoneQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationMcpPhoneQueryResponse, self).__init__()
        self._bill_no = None
        self._face = None
        self._gmt_create = None
        self._gmt_finish = None
        self._gmt_pay = None
        self._isp_abbr_cn = None
        self._mobile = None
        self._province = None
        self._status = None
        self._trade_no = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def face(self):
        return self._face

    @face.setter
    def face(self, value):
        self._face = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_finish(self):
        return self._gmt_finish

    @gmt_finish.setter
    def gmt_finish(self, value):
        self._gmt_finish = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def isp_abbr_cn(self):
        return self._isp_abbr_cn

    @isp_abbr_cn.setter
    def isp_abbr_cn(self, value):
        self._isp_abbr_cn = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if isinstance(value, OrderStatus):
            self._status = value
        else:
            self._status = OrderStatus.from_alipay_dict(value)
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationMcpPhoneQueryResponse, self).parse_response_content(response_content)
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'face' in response:
            self.face = response['face']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_finish' in response:
            self.gmt_finish = response['gmt_finish']
        if 'gmt_pay' in response:
            self.gmt_pay = response['gmt_pay']
        if 'isp_abbr_cn' in response:
            self.isp_abbr_cn = response['isp_abbr_cn']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'province' in response:
            self.province = response['province']
        if 'status' in response:
            self.status = response['status']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
