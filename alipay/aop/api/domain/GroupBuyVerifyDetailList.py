#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupBuyVerifyDetailList(object):

    def __init__(self):
        self._biz_time = None
        self._certificate_code = None
        self._certificate_id = None
        self._certificate_original_price = None
        self._certificate_real_price = None
        self._data_type = None
        self._item_id = None
        self._item_title = None
        self._merchant_fund_amount = None
        self._merchant_real_receipt_amount = None
        self._order_amount = None
        self._order_no = None
        self._other_fund_amount = None
        self._out_biz_no = None
        self._out_order_id = None
        self._partner_id = None
        self._partner_open_id = None
        self._platform_fund_amount = None
        self._trade_no = None
        self._user_id = None
        self._user_open_id = None
        self._verify_order_no = None
        self._verify_shop_id = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def certificate_code(self):
        return self._certificate_code

    @certificate_code.setter
    def certificate_code(self, value):
        self._certificate_code = value
    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def certificate_original_price(self):
        return self._certificate_original_price

    @certificate_original_price.setter
    def certificate_original_price(self, value):
        self._certificate_original_price = value
    @property
    def certificate_real_price(self):
        return self._certificate_real_price

    @certificate_real_price.setter
    def certificate_real_price(self, value):
        self._certificate_real_price = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_title(self):
        return self._item_title

    @item_title.setter
    def item_title(self, value):
        self._item_title = value
    @property
    def merchant_fund_amount(self):
        return self._merchant_fund_amount

    @merchant_fund_amount.setter
    def merchant_fund_amount(self, value):
        self._merchant_fund_amount = value
    @property
    def merchant_real_receipt_amount(self):
        return self._merchant_real_receipt_amount

    @merchant_real_receipt_amount.setter
    def merchant_real_receipt_amount(self, value):
        self._merchant_real_receipt_amount = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def other_fund_amount(self):
        return self._other_fund_amount

    @other_fund_amount.setter
    def other_fund_amount(self, value):
        self._other_fund_amount = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def partner_open_id(self):
        return self._partner_open_id

    @partner_open_id.setter
    def partner_open_id(self, value):
        self._partner_open_id = value
    @property
    def platform_fund_amount(self):
        return self._platform_fund_amount

    @platform_fund_amount.setter
    def platform_fund_amount(self, value):
        self._platform_fund_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_open_id(self):
        return self._user_open_id

    @user_open_id.setter
    def user_open_id(self, value):
        self._user_open_id = value
    @property
    def verify_order_no(self):
        return self._verify_order_no

    @verify_order_no.setter
    def verify_order_no(self, value):
        self._verify_order_no = value
    @property
    def verify_shop_id(self):
        return self._verify_shop_id

    @verify_shop_id.setter
    def verify_shop_id(self, value):
        self._verify_shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.certificate_code:
            if hasattr(self.certificate_code, 'to_alipay_dict'):
                params['certificate_code'] = self.certificate_code.to_alipay_dict()
            else:
                params['certificate_code'] = self.certificate_code
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.certificate_original_price:
            if hasattr(self.certificate_original_price, 'to_alipay_dict'):
                params['certificate_original_price'] = self.certificate_original_price.to_alipay_dict()
            else:
                params['certificate_original_price'] = self.certificate_original_price
        if self.certificate_real_price:
            if hasattr(self.certificate_real_price, 'to_alipay_dict'):
                params['certificate_real_price'] = self.certificate_real_price.to_alipay_dict()
            else:
                params['certificate_real_price'] = self.certificate_real_price
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_title:
            if hasattr(self.item_title, 'to_alipay_dict'):
                params['item_title'] = self.item_title.to_alipay_dict()
            else:
                params['item_title'] = self.item_title
        if self.merchant_fund_amount:
            if hasattr(self.merchant_fund_amount, 'to_alipay_dict'):
                params['merchant_fund_amount'] = self.merchant_fund_amount.to_alipay_dict()
            else:
                params['merchant_fund_amount'] = self.merchant_fund_amount
        if self.merchant_real_receipt_amount:
            if hasattr(self.merchant_real_receipt_amount, 'to_alipay_dict'):
                params['merchant_real_receipt_amount'] = self.merchant_real_receipt_amount.to_alipay_dict()
            else:
                params['merchant_real_receipt_amount'] = self.merchant_real_receipt_amount
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.other_fund_amount:
            if hasattr(self.other_fund_amount, 'to_alipay_dict'):
                params['other_fund_amount'] = self.other_fund_amount.to_alipay_dict()
            else:
                params['other_fund_amount'] = self.other_fund_amount
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.partner_open_id:
            if hasattr(self.partner_open_id, 'to_alipay_dict'):
                params['partner_open_id'] = self.partner_open_id.to_alipay_dict()
            else:
                params['partner_open_id'] = self.partner_open_id
        if self.platform_fund_amount:
            if hasattr(self.platform_fund_amount, 'to_alipay_dict'):
                params['platform_fund_amount'] = self.platform_fund_amount.to_alipay_dict()
            else:
                params['platform_fund_amount'] = self.platform_fund_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_open_id:
            if hasattr(self.user_open_id, 'to_alipay_dict'):
                params['user_open_id'] = self.user_open_id.to_alipay_dict()
            else:
                params['user_open_id'] = self.user_open_id
        if self.verify_order_no:
            if hasattr(self.verify_order_no, 'to_alipay_dict'):
                params['verify_order_no'] = self.verify_order_no.to_alipay_dict()
            else:
                params['verify_order_no'] = self.verify_order_no
        if self.verify_shop_id:
            if hasattr(self.verify_shop_id, 'to_alipay_dict'):
                params['verify_shop_id'] = self.verify_shop_id.to_alipay_dict()
            else:
                params['verify_shop_id'] = self.verify_shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupBuyVerifyDetailList()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'certificate_code' in d:
            o.certificate_code = d['certificate_code']
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'certificate_original_price' in d:
            o.certificate_original_price = d['certificate_original_price']
        if 'certificate_real_price' in d:
            o.certificate_real_price = d['certificate_real_price']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_title' in d:
            o.item_title = d['item_title']
        if 'merchant_fund_amount' in d:
            o.merchant_fund_amount = d['merchant_fund_amount']
        if 'merchant_real_receipt_amount' in d:
            o.merchant_real_receipt_amount = d['merchant_real_receipt_amount']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'other_fund_amount' in d:
            o.other_fund_amount = d['other_fund_amount']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'partner_open_id' in d:
            o.partner_open_id = d['partner_open_id']
        if 'platform_fund_amount' in d:
            o.platform_fund_amount = d['platform_fund_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_open_id' in d:
            o.user_open_id = d['user_open_id']
        if 'verify_order_no' in d:
            o.verify_order_no = d['verify_order_no']
        if 'verify_shop_id' in d:
            o.verify_shop_id = d['verify_shop_id']
        return o


