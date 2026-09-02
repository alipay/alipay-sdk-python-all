#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndustryInvoiceChannelOrderInfo import IndustryInvoiceChannelOrderInfo


class IndustryInvoiceChannelInfo(object):

    def __init__(self):
        self._channel_code = None
        self._channel_order_info_list = None
        self._out_channel_merchant_id = None

    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def channel_order_info_list(self):
        return self._channel_order_info_list

    @channel_order_info_list.setter
    def channel_order_info_list(self, value):
        if isinstance(value, list):
            self._channel_order_info_list = list()
            for i in value:
                if isinstance(i, IndustryInvoiceChannelOrderInfo):
                    self._channel_order_info_list.append(i)
                else:
                    self._channel_order_info_list.append(IndustryInvoiceChannelOrderInfo.from_alipay_dict(i))
    @property
    def out_channel_merchant_id(self):
        return self._out_channel_merchant_id

    @out_channel_merchant_id.setter
    def out_channel_merchant_id(self, value):
        self._out_channel_merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.channel_order_info_list:
            if isinstance(self.channel_order_info_list, list):
                for i in range(0, len(self.channel_order_info_list)):
                    element = self.channel_order_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.channel_order_info_list[i] = element.to_alipay_dict()
            if hasattr(self.channel_order_info_list, 'to_alipay_dict'):
                params['channel_order_info_list'] = self.channel_order_info_list.to_alipay_dict()
            else:
                params['channel_order_info_list'] = self.channel_order_info_list
        if self.out_channel_merchant_id:
            if hasattr(self.out_channel_merchant_id, 'to_alipay_dict'):
                params['out_channel_merchant_id'] = self.out_channel_merchant_id.to_alipay_dict()
            else:
                params['out_channel_merchant_id'] = self.out_channel_merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryInvoiceChannelInfo()
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'channel_order_info_list' in d:
            o.channel_order_info_list = d['channel_order_info_list']
        if 'out_channel_merchant_id' in d:
            o.out_channel_merchant_id = d['out_channel_merchant_id']
        return o


