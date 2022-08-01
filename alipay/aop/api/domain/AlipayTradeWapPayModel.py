#!/usr/bin/env python
# -*- coding: utf-8 -*-
from alipay.aop.api.domain.ExtUserInfo import ExtUserInfo
from alipay.aop.api.domain.ExtendParams import ExtendParams
from alipay.aop.api.domain.GoodsDetail import GoodsDetail
from alipay.aop.api.domain.InvoiceInfo import InvoiceInfo
from alipay.aop.api.domain.RoyaltyInfo import RoyaltyInfo
from alipay.aop.api.domain.SettleInfo import SettleInfo
from alipay.aop.api.domain.SubMerchant import SubMerchant


class AlipayTradeWapPayModel(object):
    openapi_types = {
            "auth_token": "str",
            "body": "str",
            "business_params": "str",
            "disable_pay_channels": "str",
            "enable_pay_channels": "str",
            "ext_user_info": "str",
            "extend_params": "str",
            "goods_type": "str",
            "invoice_info": "str",
            "merchant_order_no": "str",
            "out_trade_no": "str",
            "passback_params": "str",
            "product_code": "str",
            "promo_params": "str",
            "quit_url": "str",
            "royalty_info": "str",
            "seller_id": "str",
            "settle_info": "str",
            "specified_channel": "str",
            "store_id": "str",
            "sub_merchant": "str",
            "subject": "str",
            "time_expire": "str",
            "timeout_express": "str",
            "total_amount": "float",
            "goods_detail": "list"
        }

    def __init__(self):
        self._auth_token = None
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
        self._quit_url = None
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
    def auth_token(self):
        return self._auth_token

    @auth_token.setter
    def auth_token(self, value):
        self._auth_token = value

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
    def quit_url(self):
        return self._quit_url

    @quit_url.setter
    def quit_url(self, value):
        self._quit_url = value

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
        # support PY2 and PY3
        try:
            def iteritems(d, **kw):
                return iter(d.items(**kw))
        except Exception as _:
            def iteritems(d, **kw):
                return d.iteritems(**kw)

        params = dict()
        for attr in iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                params[attr] = list(
                    map(lambda x: x.to_alipay_dict() if hasattr(
                        x, "to_alipay_dict") else x, value)
                )
            elif hasattr(value, 'to_alipay_dict'):
                params[attr] = value.to_alipay_dict()
            elif value:
                params[attr] = value

        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeWapPayModel()
        if 'auth_token' in d:
            o.auth_token = d['auth_token']
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
        if 'quit_url' in d:
            o.quit_url = d['quit_url']
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
