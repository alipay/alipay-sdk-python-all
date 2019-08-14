#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TradePrecreateConfirmIndirectMerchantInfo import TradePrecreateConfirmIndirectMerchantInfo
from alipay.aop.api.domain.TradePrecreateConfirmTradeMerchantInfo import TradePrecreateConfirmTradeMerchantInfo
from alipay.aop.api.domain.TradePrecreateConfirmOrderInfo import TradePrecreateConfirmOrderInfo
from alipay.aop.api.domain.TradePrecreateConfirmPrecreateCodeInfo import TradePrecreateConfirmPrecreateCodeInfo
from alipay.aop.api.domain.TradePrecreateConfirmTradeStoreInfo import TradePrecreateConfirmTradeStoreInfo


class AlipayTradePrecreateConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradePrecreateConfirmResponse, self).__init__()
        self._acquiring_mode = None
        self._indirect_merchant_info = None
        self._merchant_info = None
        self._merchant_order_no = None
        self._order_create_time = None
        self._order_info = None
        self._out_trade_no = None
        self._partner_id = None
        self._precreate_code_info = None
        self._settle_serial_no = None
        self._store_info = None
        self._total_amount = None
        self._trade_no = None

    @property
    def acquiring_mode(self):
        return self._acquiring_mode

    @acquiring_mode.setter
    def acquiring_mode(self, value):
        self._acquiring_mode = value
    @property
    def indirect_merchant_info(self):
        return self._indirect_merchant_info

    @indirect_merchant_info.setter
    def indirect_merchant_info(self, value):
        if isinstance(value, TradePrecreateConfirmIndirectMerchantInfo):
            self._indirect_merchant_info = value
        else:
            self._indirect_merchant_info = TradePrecreateConfirmIndirectMerchantInfo.from_alipay_dict(value)
    @property
    def merchant_info(self):
        return self._merchant_info

    @merchant_info.setter
    def merchant_info(self, value):
        if isinstance(value, TradePrecreateConfirmTradeMerchantInfo):
            self._merchant_info = value
        else:
            self._merchant_info = TradePrecreateConfirmTradeMerchantInfo.from_alipay_dict(value)
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_info(self):
        return self._order_info

    @order_info.setter
    def order_info(self, value):
        if isinstance(value, TradePrecreateConfirmOrderInfo):
            self._order_info = value
        else:
            self._order_info = TradePrecreateConfirmOrderInfo.from_alipay_dict(value)
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def precreate_code_info(self):
        return self._precreate_code_info

    @precreate_code_info.setter
    def precreate_code_info(self, value):
        if isinstance(value, TradePrecreateConfirmPrecreateCodeInfo):
            self._precreate_code_info = value
        else:
            self._precreate_code_info = TradePrecreateConfirmPrecreateCodeInfo.from_alipay_dict(value)
    @property
    def settle_serial_no(self):
        return self._settle_serial_no

    @settle_serial_no.setter
    def settle_serial_no(self, value):
        self._settle_serial_no = value
    @property
    def store_info(self):
        return self._store_info

    @store_info.setter
    def store_info(self, value):
        if isinstance(value, TradePrecreateConfirmTradeStoreInfo):
            self._store_info = value
        else:
            self._store_info = TradePrecreateConfirmTradeStoreInfo.from_alipay_dict(value)
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradePrecreateConfirmResponse, self).parse_response_content(response_content)
        if 'acquiring_mode' in response:
            self.acquiring_mode = response['acquiring_mode']
        if 'indirect_merchant_info' in response:
            self.indirect_merchant_info = response['indirect_merchant_info']
        if 'merchant_info' in response:
            self.merchant_info = response['merchant_info']
        if 'merchant_order_no' in response:
            self.merchant_order_no = response['merchant_order_no']
        if 'order_create_time' in response:
            self.order_create_time = response['order_create_time']
        if 'order_info' in response:
            self.order_info = response['order_info']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'precreate_code_info' in response:
            self.precreate_code_info = response['precreate_code_info']
        if 'settle_serial_no' in response:
            self.settle_serial_no = response['settle_serial_no']
        if 'store_info' in response:
            self.store_info = response['store_info']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
