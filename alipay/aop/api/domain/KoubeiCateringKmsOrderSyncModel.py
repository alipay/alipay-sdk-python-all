#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KdsDishInfoDTO import KdsDishInfoDTO
from alipay.aop.api.domain.KdsOrderInfoDTO import KdsOrderInfoDTO


class KoubeiCateringKmsOrderSyncModel(object):

    def __init__(self):
        self._action = None
        self._biz_channel = None
        self._kds_dish_info_list = None
        self._kds_order_info = None
        self._order_no = None
        self._out_order_no = None
        self._shop_id = None
        self._source = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def biz_channel(self):
        return self._biz_channel

    @biz_channel.setter
    def biz_channel(self, value):
        self._biz_channel = value
    @property
    def kds_dish_info_list(self):
        return self._kds_dish_info_list

    @kds_dish_info_list.setter
    def kds_dish_info_list(self, value):
        if isinstance(value, list):
            self._kds_dish_info_list = list()
            for i in value:
                if isinstance(i, KdsDishInfoDTO):
                    self._kds_dish_info_list.append(i)
                else:
                    self._kds_dish_info_list.append(KdsDishInfoDTO.from_alipay_dict(i))
    @property
    def kds_order_info(self):
        return self._kds_order_info

    @kds_order_info.setter
    def kds_order_info(self, value):
        if isinstance(value, KdsOrderInfoDTO):
            self._kds_order_info = value
        else:
            self._kds_order_info = KdsOrderInfoDTO.from_alipay_dict(value)
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.biz_channel:
            if hasattr(self.biz_channel, 'to_alipay_dict'):
                params['biz_channel'] = self.biz_channel.to_alipay_dict()
            else:
                params['biz_channel'] = self.biz_channel
        if self.kds_dish_info_list:
            if isinstance(self.kds_dish_info_list, list):
                for i in range(0, len(self.kds_dish_info_list)):
                    element = self.kds_dish_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.kds_dish_info_list[i] = element.to_alipay_dict()
            if hasattr(self.kds_dish_info_list, 'to_alipay_dict'):
                params['kds_dish_info_list'] = self.kds_dish_info_list.to_alipay_dict()
            else:
                params['kds_dish_info_list'] = self.kds_dish_info_list
        if self.kds_order_info:
            if hasattr(self.kds_order_info, 'to_alipay_dict'):
                params['kds_order_info'] = self.kds_order_info.to_alipay_dict()
            else:
                params['kds_order_info'] = self.kds_order_info
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringKmsOrderSyncModel()
        if 'action' in d:
            o.action = d['action']
        if 'biz_channel' in d:
            o.biz_channel = d['biz_channel']
        if 'kds_dish_info_list' in d:
            o.kds_dish_info_list = d['kds_dish_info_list']
        if 'kds_order_info' in d:
            o.kds_order_info = d['kds_order_info']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'source' in d:
            o.source = d['source']
        return o


