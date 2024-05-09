#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AftersaleItemInfo import AftersaleItemInfo
from alipay.aop.api.domain.LogisticsWaybill import LogisticsWaybill


class AlipayOpenMiniOrderAftersaleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniOrderAftersaleQueryResponse, self).__init__()
        self._action_type = None
        self._aftersale_goods_info_list = None
        self._aftersale_id = None
        self._aftersale_reason = None
        self._logistics_waybills = None
        self._order_id = None
        self._out_aftersale_id = None
        self._path = None
        self._status = None
        self._status_code = None
        self._type = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def aftersale_goods_info_list(self):
        return self._aftersale_goods_info_list

    @aftersale_goods_info_list.setter
    def aftersale_goods_info_list(self, value):
        if isinstance(value, list):
            self._aftersale_goods_info_list = list()
            for i in value:
                if isinstance(i, AftersaleItemInfo):
                    self._aftersale_goods_info_list.append(i)
                else:
                    self._aftersale_goods_info_list.append(AftersaleItemInfo.from_alipay_dict(i))
    @property
    def aftersale_id(self):
        return self._aftersale_id

    @aftersale_id.setter
    def aftersale_id(self, value):
        self._aftersale_id = value
    @property
    def aftersale_reason(self):
        return self._aftersale_reason

    @aftersale_reason.setter
    def aftersale_reason(self, value):
        self._aftersale_reason = value
    @property
    def logistics_waybills(self):
        return self._logistics_waybills

    @logistics_waybills.setter
    def logistics_waybills(self, value):
        if isinstance(value, list):
            self._logistics_waybills = list()
            for i in value:
                if isinstance(i, LogisticsWaybill):
                    self._logistics_waybills.append(i)
                else:
                    self._logistics_waybills.append(LogisticsWaybill.from_alipay_dict(i))
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_aftersale_id(self):
        return self._out_aftersale_id

    @out_aftersale_id.setter
    def out_aftersale_id(self, value):
        self._out_aftersale_id = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniOrderAftersaleQueryResponse, self).parse_response_content(response_content)
        if 'action_type' in response:
            self.action_type = response['action_type']
        if 'aftersale_goods_info_list' in response:
            self.aftersale_goods_info_list = response['aftersale_goods_info_list']
        if 'aftersale_id' in response:
            self.aftersale_id = response['aftersale_id']
        if 'aftersale_reason' in response:
            self.aftersale_reason = response['aftersale_reason']
        if 'logistics_waybills' in response:
            self.logistics_waybills = response['logistics_waybills']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_aftersale_id' in response:
            self.out_aftersale_id = response['out_aftersale_id']
        if 'path' in response:
            self.path = response['path']
        if 'status' in response:
            self.status = response['status']
        if 'status_code' in response:
            self.status_code = response['status_code']
        if 'type' in response:
            self.type = response['type']
