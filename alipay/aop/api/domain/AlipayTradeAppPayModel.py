#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SignParams import SignParams
from alipay.aop.api.domain.ExtUserInfo import ExtUserInfo
from alipay.aop.api.domain.ExtendParams import ExtendParams
from alipay.aop.api.domain.GoodsDetail import GoodsDetail
from alipay.aop.api.domain.InvoiceInfo import InvoiceInfo
from alipay.aop.api.domain.RoyaltyInfo import RoyaltyInfo
from alipay.aop.api.domain.SettleInfo import SettleInfo
from alipay.aop.api.domain.SubMerchant import SubMerchant


class AlipayTradeAppPayModel(object):

    def __init__(self):
        self._agreement_sign_params = None
        self._body = None
        self._business_params = None
        self._disable_pay_channels = None
        self._enable_pay_channels = None
        self._ext_user_info = None
        self._extend_params = None
        self._goods_detail = None
        self._goods_type = None
        self._invoice_info = None
        self._merchant_order_no = None
        self._out_trade_no = None
        self._passback_params = None
        self._product_code = None
        self._promo_params = None
        self._query_options = None
        self._royalty_info = None
        self._seller_id = None
        self._settle_info = None
        self._specified_channel = None
        self._store_id = None
        self._sub_merchant = None
        self._subject = None
        self._time_expire = None
        self._timeout_express = None
        self._total_amount = None

    @property
    def agreement_sign_params(self):
        return self._agreement_sign_params

    @agreement_sign_params.setter
    def agreement_sign_params(self, value):
        if isinstance(value, SignParams):
            self._agreement_sign_params = value
        else:
            self._agreement_sign_params = SignParams.from_alipay_dict(value)
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        self._business_params = value
    @property
    def disable_pay_channels(self):
        return self._disable_pay_channels

    @disable_pay_channels.setter
    def disable_pay_channels(self, value):
        self._disable_pay_channels = value
    @property
    def enable_pay_channels(self):
        return self._enable_pay_channels

    @enable_pay_channels.setter
    def enable_pay_channels(self, value):
        self._enable_pay_channels = value
    @property
    def ext_user_info(self):
        return self._ext_user_info

    @ext_user_info.setter
    def ext_user_info(self, value):
        if isinstance(value, ExtUserInfo):
            self._ext_user_info = value
        else:
            self._ext_user_info = ExtUserInfo.from_alipay_dict(value)
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, ExtendParams):
            self._extend_params = value
        else:
            self._extend_params = ExtendParams.from_alipay_dict(value)
    @property
    def goods_detail(self):
        return self._goods_detail

    @goods_detail.setter
    def goods_detail(self, value):
        if isinstance(value, list):
            self._goods_detail = list()
            for i in value:
                if isinstance(i, GoodsDetail):
                    self._goods_detail.append(i)
                else:
                    self._goods_detail.append(GoodsDetail.from_alipay_dict(i))
    @property
    def goods_type(self):
        return self._goods_type

    @goods_type.setter
    def goods_type(self, value):
        self._goods_type = value
    @property
    def invoice_info(self):
        return self._invoice_info

    @invoice_info.setter
    def invoice_info(self, value):
        if isinstance(value, InvoiceInfo):
            self._invoice_info = value
        else:
            self._invoice_info = InvoiceInfo.from_alipay_dict(value)
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def passback_params(self):
        return self._passback_params

    @passback_params.setter
    def passback_params(self, value):
        self._passback_params = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def promo_params(self):
        return self._promo_params

    @promo_params.setter
    def promo_params(self, value):
        self._promo_params = value
    @property
    def query_options(self):
        return self._query_options

    @query_options.setter
    def query_options(self, value):
        if isinstance(value, list):
            self._query_options = list()
            for i in value:
                self._query_options.append(i)
    @property
    def royalty_info(self):
        return self._royalty_info

    @royalty_info.setter
    def royalty_info(self, value):
        if isinstance(value, RoyaltyInfo):
            self._royalty_info = value
        else:
            self._royalty_info = RoyaltyInfo.from_alipay_dict(value)
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def settle_info(self):
        return self._settle_info

    @settle_info.setter
    def settle_info(self, value):
        if isinstance(value, SettleInfo):
            self._settle_info = value
        else:
            self._settle_info = SettleInfo.from_alipay_dict(value)
    @property
    def specified_channel(self):
        return self._specified_channel

    @specified_channel.setter
    def specified_channel(self, value):
        self._specified_channel = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def sub_merchant(self):
        return self._sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, value):
        if isinstance(value, SubMerchant):
            self._sub_merchant = value
        else:
            self._sub_merchant = SubMerchant.from_alipay_dict(value)
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def time_expire(self):
        return self._time_expire

    @time_expire.setter
    def time_expire(self, value):
        self._time_expire = value
    @property
    def timeout_express(self):
        return self._timeout_express

    @timeout_express.setter
    def timeout_express(self, value):
        self._timeout_express = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_sign_params:
            if hasattr(self.agreement_sign_params, 'to_alipay_dict'):
                params['agreement_sign_params'] = self.agreement_sign_params.to_alipay_dict()
            else:
                params['agreement_sign_params'] = self.agreement_sign_params
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.business_params:
            if hasattr(self.business_params, 'to_alipay_dict'):
                params['business_params'] = self.business_params.to_alipay_dict()
            else:
                params['business_params'] = self.business_params
        if self.disable_pay_channels:
            if hasattr(self.disable_pay_channels, 'to_alipay_dict'):
                params['disable_pay_channels'] = self.disable_pay_channels.to_alipay_dict()
            else:
                params['disable_pay_channels'] = self.disable_pay_channels
        if self.enable_pay_channels:
            if hasattr(self.enable_pay_channels, 'to_alipay_dict'):
                params['enable_pay_channels'] = self.enable_pay_channels.to_alipay_dict()
            else:
                params['enable_pay_channels'] = self.enable_pay_channels
        if self.ext_user_info:
            if hasattr(self.ext_user_info, 'to_alipay_dict'):
                params['ext_user_info'] = self.ext_user_info.to_alipay_dict()
            else:
                params['ext_user_info'] = self.ext_user_info
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.goods_detail:
            if isinstance(self.goods_detail, list):
                for i in range(0, len(self.goods_detail)):
                    element = self.goods_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_detail[i] = element.to_alipay_dict()
            if hasattr(self.goods_detail, 'to_alipay_dict'):
                params['goods_detail'] = self.goods_detail.to_alipay_dict()
            else:
                params['goods_detail'] = self.goods_detail
        if self.goods_type:
            if hasattr(self.goods_type, 'to_alipay_dict'):
                params['goods_type'] = self.goods_type.to_alipay_dict()
            else:
                params['goods_type'] = self.goods_type
        if self.invoice_info:
            if hasattr(self.invoice_info, 'to_alipay_dict'):
                params['invoice_info'] = self.invoice_info.to_alipay_dict()
            else:
                params['invoice_info'] = self.invoice_info
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.passback_params:
            if hasattr(self.passback_params, 'to_alipay_dict'):
                params['passback_params'] = self.passback_params.to_alipay_dict()
            else:
                params['passback_params'] = self.passback_params
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.promo_params:
            if hasattr(self.promo_params, 'to_alipay_dict'):
                params['promo_params'] = self.promo_params.to_alipay_dict()
            else:
                params['promo_params'] = self.promo_params
        if self.query_options:
            if isinstance(self.query_options, list):
                for i in range(0, len(self.query_options)):
                    element = self.query_options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.query_options[i] = element.to_alipay_dict()
            if hasattr(self.query_options, 'to_alipay_dict'):
                params['query_options'] = self.query_options.to_alipay_dict()
            else:
                params['query_options'] = self.query_options
        if self.royalty_info:
            if hasattr(self.royalty_info, 'to_alipay_dict'):
                params['royalty_info'] = self.royalty_info.to_alipay_dict()
            else:
                params['royalty_info'] = self.royalty_info
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.settle_info:
            if hasattr(self.settle_info, 'to_alipay_dict'):
                params['settle_info'] = self.settle_info.to_alipay_dict()
            else:
                params['settle_info'] = self.settle_info
        if self.specified_channel:
            if hasattr(self.specified_channel, 'to_alipay_dict'):
                params['specified_channel'] = self.specified_channel.to_alipay_dict()
            else:
                params['specified_channel'] = self.specified_channel
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.sub_merchant:
            if hasattr(self.sub_merchant, 'to_alipay_dict'):
                params['sub_merchant'] = self.sub_merchant.to_alipay_dict()
            else:
                params['sub_merchant'] = self.sub_merchant
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.time_expire:
            if hasattr(self.time_expire, 'to_alipay_dict'):
                params['time_expire'] = self.time_expire.to_alipay_dict()
            else:
                params['time_expire'] = self.time_expire
        if self.timeout_express:
            if hasattr(self.timeout_express, 'to_alipay_dict'):
                params['timeout_express'] = self.timeout_express.to_alipay_dict()
            else:
                params['timeout_express'] = self.timeout_express
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeAppPayModel()
        if 'agreement_sign_params' in d:
            o.agreement_sign_params = d['agreement_sign_params']
        if 'body' in d:
            o.body = d['body']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'disable_pay_channels' in d:
            o.disable_pay_channels = d['disable_pay_channels']
        if 'enable_pay_channels' in d:
            o.enable_pay_channels = d['enable_pay_channels']
        if 'ext_user_info' in d:
            o.ext_user_info = d['ext_user_info']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'goods_detail' in d:
            o.goods_detail = d['goods_detail']
        if 'goods_type' in d:
            o.goods_type = d['goods_type']
        if 'invoice_info' in d:
            o.invoice_info = d['invoice_info']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'passback_params' in d:
            o.passback_params = d['passback_params']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'promo_params' in d:
            o.promo_params = d['promo_params']
        if 'query_options' in d:
            o.query_options = d['query_options']
        if 'royalty_info' in d:
            o.royalty_info = d['royalty_info']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'settle_info' in d:
            o.settle_info = d['settle_info']
        if 'specified_channel' in d:
            o.specified_channel = d['specified_channel']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'sub_merchant' in d:
            o.sub_merchant = d['sub_merchant']
        if 'subject' in d:
            o.subject = d['subject']
        if 'time_expire' in d:
            o.time_expire = d['time_expire']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


