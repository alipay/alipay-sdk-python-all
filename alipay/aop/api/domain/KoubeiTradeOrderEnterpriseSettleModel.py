#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiTradeOrderEnterpriseSettleModel(object):

    def __init__(self):
        self._biz_product = None
        self._biz_scene = None
        self._buyer_amount = None
        self._buyer_id = None
        self._buyer_type = None
        self._enterprise_amount = None
        self._ext_info = None
        self._mdiscount_amount = None
        self._out_order_no = None
        self._partner_id = None
        self._platform_discount_amount = None
        self._real_amount = None
        self._shop_id = None
        self._total_amount = None
        self._trade_close_timeout = None
        self._trade_finish_timeout = None

    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def buyer_amount(self):
        return self._buyer_amount

    @buyer_amount.setter
    def buyer_amount(self, value):
        self._buyer_amount = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_type(self):
        return self._buyer_type

    @buyer_type.setter
    def buyer_type(self, value):
        self._buyer_type = value
    @property
    def enterprise_amount(self):
        return self._enterprise_amount

    @enterprise_amount.setter
    def enterprise_amount(self, value):
        self._enterprise_amount = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def mdiscount_amount(self):
        return self._mdiscount_amount

    @mdiscount_amount.setter
    def mdiscount_amount(self, value):
        self._mdiscount_amount = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def platform_discount_amount(self):
        return self._platform_discount_amount

    @platform_discount_amount.setter
    def platform_discount_amount(self, value):
        self._platform_discount_amount = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_close_timeout(self):
        return self._trade_close_timeout

    @trade_close_timeout.setter
    def trade_close_timeout(self, value):
        self._trade_close_timeout = value
    @property
    def trade_finish_timeout(self):
        return self._trade_finish_timeout

    @trade_finish_timeout.setter
    def trade_finish_timeout(self, value):
        self._trade_finish_timeout = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.buyer_amount:
            if hasattr(self.buyer_amount, 'to_alipay_dict'):
                params['buyer_amount'] = self.buyer_amount.to_alipay_dict()
            else:
                params['buyer_amount'] = self.buyer_amount
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_type:
            if hasattr(self.buyer_type, 'to_alipay_dict'):
                params['buyer_type'] = self.buyer_type.to_alipay_dict()
            else:
                params['buyer_type'] = self.buyer_type
        if self.enterprise_amount:
            if hasattr(self.enterprise_amount, 'to_alipay_dict'):
                params['enterprise_amount'] = self.enterprise_amount.to_alipay_dict()
            else:
                params['enterprise_amount'] = self.enterprise_amount
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.mdiscount_amount:
            if hasattr(self.mdiscount_amount, 'to_alipay_dict'):
                params['mdiscount_amount'] = self.mdiscount_amount.to_alipay_dict()
            else:
                params['mdiscount_amount'] = self.mdiscount_amount
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.platform_discount_amount:
            if hasattr(self.platform_discount_amount, 'to_alipay_dict'):
                params['platform_discount_amount'] = self.platform_discount_amount.to_alipay_dict()
            else:
                params['platform_discount_amount'] = self.platform_discount_amount
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_close_timeout:
            if hasattr(self.trade_close_timeout, 'to_alipay_dict'):
                params['trade_close_timeout'] = self.trade_close_timeout.to_alipay_dict()
            else:
                params['trade_close_timeout'] = self.trade_close_timeout
        if self.trade_finish_timeout:
            if hasattr(self.trade_finish_timeout, 'to_alipay_dict'):
                params['trade_finish_timeout'] = self.trade_finish_timeout.to_alipay_dict()
            else:
                params['trade_finish_timeout'] = self.trade_finish_timeout
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiTradeOrderEnterpriseSettleModel()
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'buyer_amount' in d:
            o.buyer_amount = d['buyer_amount']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_type' in d:
            o.buyer_type = d['buyer_type']
        if 'enterprise_amount' in d:
            o.enterprise_amount = d['enterprise_amount']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'mdiscount_amount' in d:
            o.mdiscount_amount = d['mdiscount_amount']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'platform_discount_amount' in d:
            o.platform_discount_amount = d['platform_discount_amount']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_close_timeout' in d:
            o.trade_close_timeout = d['trade_close_timeout']
        if 'trade_finish_timeout' in d:
            o.trade_finish_timeout = d['trade_finish_timeout']
        return o


