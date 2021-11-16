#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AgreementParams import AgreementParams
from alipay.aop.api.domain.BusinessParams import BusinessParams
from alipay.aop.api.domain.ExtUserInfo import ExtUserInfo
from alipay.aop.api.domain.ExtendParams import ExtendParams
from alipay.aop.api.domain.GoodsDetail import GoodsDetail
from alipay.aop.api.domain.PayParams import PayParams
from alipay.aop.api.domain.PromoParam import PromoParam
from alipay.aop.api.domain.RoyaltyInfo import RoyaltyInfo
from alipay.aop.api.domain.SettleInfo import SettleInfo
from alipay.aop.api.domain.SubMerchant import SubMerchant


class AlipayTradePayModel(object):

    def __init__(self):
        self._advance_payment_type = None
        self._agreement_params = None
        self._alipay_store_id = None
        self._auth_code = None
        self._auth_confirm_mode = None
        self._auth_no = None
        self._body = None
        self._business_params = None
        self._buyer_id = None
        self._disable_pay_channels = None
        self._discountable_amount = None
        self._ext_user_info = None
        self._extend_params = None
        self._goods_detail = None
        self._is_async_pay = None
        self._merchant_order_no = None
        self._operator_id = None
        self._out_trade_no = None
        self._passback_params = None
        self._pay_params = None
        self._product_code = None
        self._promo_params = None
        self._query_options = None
        self._request_org_pid = None
        self._royalty_info = None
        self._scene = None
        self._seller_id = None
        self._settle_currency = None
        self._settle_info = None
        self._store_id = None
        self._sub_merchant = None
        self._subject = None
        self._terminal_id = None
        self._terminal_params = None
        self._time_expire = None
        self._timeout_express = None
        self._total_amount = None
        self._trans_currency = None
        self._undiscountable_amount = None

    @property
    def advance_payment_type(self):
        return self._advance_payment_type

    @advance_payment_type.setter
    def advance_payment_type(self, value):
        self._advance_payment_type = value
    @property
    def agreement_params(self):
        return self._agreement_params

    @agreement_params.setter
    def agreement_params(self, value):
        if isinstance(value, AgreementParams):
            self._agreement_params = value
        else:
            self._agreement_params = AgreementParams.from_alipay_dict(value)
    @property
    def alipay_store_id(self):
        return self._alipay_store_id

    @alipay_store_id.setter
    def alipay_store_id(self, value):
        self._alipay_store_id = value
    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def auth_confirm_mode(self):
        return self._auth_confirm_mode

    @auth_confirm_mode.setter
    def auth_confirm_mode(self, value):
        self._auth_confirm_mode = value
    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value
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
        if isinstance(value, BusinessParams):
            self._business_params = value
        else:
            self._business_params = BusinessParams.from_alipay_dict(value)
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def disable_pay_channels(self):
        return self._disable_pay_channels

    @disable_pay_channels.setter
    def disable_pay_channels(self, value):
        self._disable_pay_channels = value
    @property
    def discountable_amount(self):
        return self._discountable_amount

    @discountable_amount.setter
    def discountable_amount(self, value):
        self._discountable_amount = value
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
    def is_async_pay(self):
        return self._is_async_pay

    @is_async_pay.setter
    def is_async_pay(self, value):
        self._is_async_pay = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
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
    def pay_params(self):
        return self._pay_params

    @pay_params.setter
    def pay_params(self, value):
        if isinstance(value, PayParams):
            self._pay_params = value
        else:
            self._pay_params = PayParams.from_alipay_dict(value)
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
        if isinstance(value, PromoParam):
            self._promo_params = value
        else:
            self._promo_params = PromoParam.from_alipay_dict(value)
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
    def request_org_pid(self):
        return self._request_org_pid

    @request_org_pid.setter
    def request_org_pid(self, value):
        self._request_org_pid = value
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
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def settle_currency(self):
        return self._settle_currency

    @settle_currency.setter
    def settle_currency(self, value):
        self._settle_currency = value
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
    def terminal_id(self):
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, value):
        self._terminal_id = value
    @property
    def terminal_params(self):
        return self._terminal_params

    @terminal_params.setter
    def terminal_params(self, value):
        self._terminal_params = value
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
    @property
    def trans_currency(self):
        return self._trans_currency

    @trans_currency.setter
    def trans_currency(self, value):
        self._trans_currency = value
    @property
    def undiscountable_amount(self):
        return self._undiscountable_amount

    @undiscountable_amount.setter
    def undiscountable_amount(self, value):
        self._undiscountable_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.advance_payment_type:
            if hasattr(self.advance_payment_type, 'to_alipay_dict'):
                params['advance_payment_type'] = self.advance_payment_type.to_alipay_dict()
            else:
                params['advance_payment_type'] = self.advance_payment_type
        if self.agreement_params:
            if hasattr(self.agreement_params, 'to_alipay_dict'):
                params['agreement_params'] = self.agreement_params.to_alipay_dict()
            else:
                params['agreement_params'] = self.agreement_params
        if self.alipay_store_id:
            if hasattr(self.alipay_store_id, 'to_alipay_dict'):
                params['alipay_store_id'] = self.alipay_store_id.to_alipay_dict()
            else:
                params['alipay_store_id'] = self.alipay_store_id
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.auth_confirm_mode:
            if hasattr(self.auth_confirm_mode, 'to_alipay_dict'):
                params['auth_confirm_mode'] = self.auth_confirm_mode.to_alipay_dict()
            else:
                params['auth_confirm_mode'] = self.auth_confirm_mode
        if self.auth_no:
            if hasattr(self.auth_no, 'to_alipay_dict'):
                params['auth_no'] = self.auth_no.to_alipay_dict()
            else:
                params['auth_no'] = self.auth_no
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
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.disable_pay_channels:
            if hasattr(self.disable_pay_channels, 'to_alipay_dict'):
                params['disable_pay_channels'] = self.disable_pay_channels.to_alipay_dict()
            else:
                params['disable_pay_channels'] = self.disable_pay_channels
        if self.discountable_amount:
            if hasattr(self.discountable_amount, 'to_alipay_dict'):
                params['discountable_amount'] = self.discountable_amount.to_alipay_dict()
            else:
                params['discountable_amount'] = self.discountable_amount
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
        if self.is_async_pay:
            if hasattr(self.is_async_pay, 'to_alipay_dict'):
                params['is_async_pay'] = self.is_async_pay.to_alipay_dict()
            else:
                params['is_async_pay'] = self.is_async_pay
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
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
        if self.pay_params:
            if hasattr(self.pay_params, 'to_alipay_dict'):
                params['pay_params'] = self.pay_params.to_alipay_dict()
            else:
                params['pay_params'] = self.pay_params
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
        if self.request_org_pid:
            if hasattr(self.request_org_pid, 'to_alipay_dict'):
                params['request_org_pid'] = self.request_org_pid.to_alipay_dict()
            else:
                params['request_org_pid'] = self.request_org_pid
        if self.royalty_info:
            if hasattr(self.royalty_info, 'to_alipay_dict'):
                params['royalty_info'] = self.royalty_info.to_alipay_dict()
            else:
                params['royalty_info'] = self.royalty_info
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.settle_currency:
            if hasattr(self.settle_currency, 'to_alipay_dict'):
                params['settle_currency'] = self.settle_currency.to_alipay_dict()
            else:
                params['settle_currency'] = self.settle_currency
        if self.settle_info:
            if hasattr(self.settle_info, 'to_alipay_dict'):
                params['settle_info'] = self.settle_info.to_alipay_dict()
            else:
                params['settle_info'] = self.settle_info
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
        if self.terminal_id:
            if hasattr(self.terminal_id, 'to_alipay_dict'):
                params['terminal_id'] = self.terminal_id.to_alipay_dict()
            else:
                params['terminal_id'] = self.terminal_id
        if self.terminal_params:
            if hasattr(self.terminal_params, 'to_alipay_dict'):
                params['terminal_params'] = self.terminal_params.to_alipay_dict()
            else:
                params['terminal_params'] = self.terminal_params
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
        if self.trans_currency:
            if hasattr(self.trans_currency, 'to_alipay_dict'):
                params['trans_currency'] = self.trans_currency.to_alipay_dict()
            else:
                params['trans_currency'] = self.trans_currency
        if self.undiscountable_amount:
            if hasattr(self.undiscountable_amount, 'to_alipay_dict'):
                params['undiscountable_amount'] = self.undiscountable_amount.to_alipay_dict()
            else:
                params['undiscountable_amount'] = self.undiscountable_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradePayModel()
        if 'advance_payment_type' in d:
            o.advance_payment_type = d['advance_payment_type']
        if 'agreement_params' in d:
            o.agreement_params = d['agreement_params']
        if 'alipay_store_id' in d:
            o.alipay_store_id = d['alipay_store_id']
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'auth_confirm_mode' in d:
            o.auth_confirm_mode = d['auth_confirm_mode']
        if 'auth_no' in d:
            o.auth_no = d['auth_no']
        if 'body' in d:
            o.body = d['body']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'disable_pay_channels' in d:
            o.disable_pay_channels = d['disable_pay_channels']
        if 'discountable_amount' in d:
            o.discountable_amount = d['discountable_amount']
        if 'ext_user_info' in d:
            o.ext_user_info = d['ext_user_info']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'goods_detail' in d:
            o.goods_detail = d['goods_detail']
        if 'is_async_pay' in d:
            o.is_async_pay = d['is_async_pay']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'passback_params' in d:
            o.passback_params = d['passback_params']
        if 'pay_params' in d:
            o.pay_params = d['pay_params']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'promo_params' in d:
            o.promo_params = d['promo_params']
        if 'query_options' in d:
            o.query_options = d['query_options']
        if 'request_org_pid' in d:
            o.request_org_pid = d['request_org_pid']
        if 'royalty_info' in d:
            o.royalty_info = d['royalty_info']
        if 'scene' in d:
            o.scene = d['scene']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'settle_currency' in d:
            o.settle_currency = d['settle_currency']
        if 'settle_info' in d:
            o.settle_info = d['settle_info']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'sub_merchant' in d:
            o.sub_merchant = d['sub_merchant']
        if 'subject' in d:
            o.subject = d['subject']
        if 'terminal_id' in d:
            o.terminal_id = d['terminal_id']
        if 'terminal_params' in d:
            o.terminal_params = d['terminal_params']
        if 'time_expire' in d:
            o.time_expire = d['time_expire']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trans_currency' in d:
            o.trans_currency = d['trans_currency']
        if 'undiscountable_amount' in d:
            o.undiscountable_amount = d['undiscountable_amount']
        return o


