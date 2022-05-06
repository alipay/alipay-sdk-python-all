#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BelongGreenMerchantInfo import BelongGreenMerchantInfo


class AlipayCommerceGreenItemenergySendModel(object):

    def __init__(self):
        self._alipay_uid = None
        self._belong_merchant_info = None
        self._goods_id = None
        self._goods_name = None
        self._industry_type = None
        self._order_link = None
        self._qr_code_id = None
        self._scan_time = None

    @property
    def alipay_uid(self):
        return self._alipay_uid

    @alipay_uid.setter
    def alipay_uid(self, value):
        self._alipay_uid = value
    @property
    def belong_merchant_info(self):
        return self._belong_merchant_info

    @belong_merchant_info.setter
    def belong_merchant_info(self, value):
        if isinstance(value, BelongGreenMerchantInfo):
            self._belong_merchant_info = value
        else:
            self._belong_merchant_info = BelongGreenMerchantInfo.from_alipay_dict(value)
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def industry_type(self):
        return self._industry_type

    @industry_type.setter
    def industry_type(self, value):
        self._industry_type = value
    @property
    def order_link(self):
        return self._order_link

    @order_link.setter
    def order_link(self, value):
        self._order_link = value
    @property
    def qr_code_id(self):
        return self._qr_code_id

    @qr_code_id.setter
    def qr_code_id(self, value):
        self._qr_code_id = value
    @property
    def scan_time(self):
        return self._scan_time

    @scan_time.setter
    def scan_time(self, value):
        self._scan_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_uid:
            if hasattr(self.alipay_uid, 'to_alipay_dict'):
                params['alipay_uid'] = self.alipay_uid.to_alipay_dict()
            else:
                params['alipay_uid'] = self.alipay_uid
        if self.belong_merchant_info:
            if hasattr(self.belong_merchant_info, 'to_alipay_dict'):
                params['belong_merchant_info'] = self.belong_merchant_info.to_alipay_dict()
            else:
                params['belong_merchant_info'] = self.belong_merchant_info
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.industry_type:
            if hasattr(self.industry_type, 'to_alipay_dict'):
                params['industry_type'] = self.industry_type.to_alipay_dict()
            else:
                params['industry_type'] = self.industry_type
        if self.order_link:
            if hasattr(self.order_link, 'to_alipay_dict'):
                params['order_link'] = self.order_link.to_alipay_dict()
            else:
                params['order_link'] = self.order_link
        if self.qr_code_id:
            if hasattr(self.qr_code_id, 'to_alipay_dict'):
                params['qr_code_id'] = self.qr_code_id.to_alipay_dict()
            else:
                params['qr_code_id'] = self.qr_code_id
        if self.scan_time:
            if hasattr(self.scan_time, 'to_alipay_dict'):
                params['scan_time'] = self.scan_time.to_alipay_dict()
            else:
                params['scan_time'] = self.scan_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceGreenItemenergySendModel()
        if 'alipay_uid' in d:
            o.alipay_uid = d['alipay_uid']
        if 'belong_merchant_info' in d:
            o.belong_merchant_info = d['belong_merchant_info']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'industry_type' in d:
            o.industry_type = d['industry_type']
        if 'order_link' in d:
            o.order_link = d['order_link']
        if 'qr_code_id' in d:
            o.qr_code_id = d['qr_code_id']
        if 'scan_time' in d:
            o.scan_time = d['scan_time']
        return o


