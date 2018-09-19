#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceItemQueryOpenModel import InvoiceItemQueryOpenModel
from alipay.aop.api.domain.InvoiceTradeFundItem import InvoiceTradeFundItem
from alipay.aop.api.domain.InvoiceTradeGoodsItem import InvoiceTradeGoodsItem


class InvoiceTradeInfo(object):

    def __init__(self):
        self._alipay_trade_no = None
        self._create_trade_date = None
        self._einv_trade_id = None
        self._goods_name = None
        self._invoice_content = None
        self._m_name = None
        self._m_short_name = None
        self._merchant_id = None
        self._out_biz_no = None
        self._payment_trade_date = None
        self._real_amount = None
        self._sub_m_name = None
        self._sub_m_short_name = None
        self._trade_amount = None
        self._trade_fund_list = None
        self._trade_goods_list = None
        self._trade_no = None
        self._user_id = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def create_trade_date(self):
        return self._create_trade_date

    @create_trade_date.setter
    def create_trade_date(self, value):
        self._create_trade_date = value
    @property
    def einv_trade_id(self):
        return self._einv_trade_id

    @einv_trade_id.setter
    def einv_trade_id(self, value):
        self._einv_trade_id = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def invoice_content(self):
        return self._invoice_content

    @invoice_content.setter
    def invoice_content(self, value):
        if isinstance(value, list):
            self._invoice_content = list()
            for i in value:
                if isinstance(i, InvoiceItemQueryOpenModel):
                    self._invoice_content.append(i)
                else:
                    self._invoice_content.append(InvoiceItemQueryOpenModel.from_alipay_dict(i))
    @property
    def m_name(self):
        return self._m_name

    @m_name.setter
    def m_name(self, value):
        self._m_name = value
    @property
    def m_short_name(self):
        return self._m_short_name

    @m_short_name.setter
    def m_short_name(self, value):
        self._m_short_name = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def payment_trade_date(self):
        return self._payment_trade_date

    @payment_trade_date.setter
    def payment_trade_date(self, value):
        self._payment_trade_date = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def sub_m_name(self):
        return self._sub_m_name

    @sub_m_name.setter
    def sub_m_name(self, value):
        self._sub_m_name = value
    @property
    def sub_m_short_name(self):
        return self._sub_m_short_name

    @sub_m_short_name.setter
    def sub_m_short_name(self, value):
        self._sub_m_short_name = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_fund_list(self):
        return self._trade_fund_list

    @trade_fund_list.setter
    def trade_fund_list(self, value):
        if isinstance(value, list):
            self._trade_fund_list = list()
            for i in value:
                if isinstance(i, InvoiceTradeFundItem):
                    self._trade_fund_list.append(i)
                else:
                    self._trade_fund_list.append(InvoiceTradeFundItem.from_alipay_dict(i))
    @property
    def trade_goods_list(self):
        return self._trade_goods_list

    @trade_goods_list.setter
    def trade_goods_list(self, value):
        if isinstance(value, list):
            self._trade_goods_list = list()
            for i in value:
                if isinstance(i, InvoiceTradeGoodsItem):
                    self._trade_goods_list.append(i)
                else:
                    self._trade_goods_list.append(InvoiceTradeGoodsItem.from_alipay_dict(i))
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


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.create_trade_date:
            if hasattr(self.create_trade_date, 'to_alipay_dict'):
                params['create_trade_date'] = self.create_trade_date.to_alipay_dict()
            else:
                params['create_trade_date'] = self.create_trade_date
        if self.einv_trade_id:
            if hasattr(self.einv_trade_id, 'to_alipay_dict'):
                params['einv_trade_id'] = self.einv_trade_id.to_alipay_dict()
            else:
                params['einv_trade_id'] = self.einv_trade_id
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.invoice_content:
            if isinstance(self.invoice_content, list):
                for i in range(0, len(self.invoice_content)):
                    element = self.invoice_content[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_content[i] = element.to_alipay_dict()
            if hasattr(self.invoice_content, 'to_alipay_dict'):
                params['invoice_content'] = self.invoice_content.to_alipay_dict()
            else:
                params['invoice_content'] = self.invoice_content
        if self.m_name:
            if hasattr(self.m_name, 'to_alipay_dict'):
                params['m_name'] = self.m_name.to_alipay_dict()
            else:
                params['m_name'] = self.m_name
        if self.m_short_name:
            if hasattr(self.m_short_name, 'to_alipay_dict'):
                params['m_short_name'] = self.m_short_name.to_alipay_dict()
            else:
                params['m_short_name'] = self.m_short_name
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.payment_trade_date:
            if hasattr(self.payment_trade_date, 'to_alipay_dict'):
                params['payment_trade_date'] = self.payment_trade_date.to_alipay_dict()
            else:
                params['payment_trade_date'] = self.payment_trade_date
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.sub_m_name:
            if hasattr(self.sub_m_name, 'to_alipay_dict'):
                params['sub_m_name'] = self.sub_m_name.to_alipay_dict()
            else:
                params['sub_m_name'] = self.sub_m_name
        if self.sub_m_short_name:
            if hasattr(self.sub_m_short_name, 'to_alipay_dict'):
                params['sub_m_short_name'] = self.sub_m_short_name.to_alipay_dict()
            else:
                params['sub_m_short_name'] = self.sub_m_short_name
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        if self.trade_fund_list:
            if isinstance(self.trade_fund_list, list):
                for i in range(0, len(self.trade_fund_list)):
                    element = self.trade_fund_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_fund_list[i] = element.to_alipay_dict()
            if hasattr(self.trade_fund_list, 'to_alipay_dict'):
                params['trade_fund_list'] = self.trade_fund_list.to_alipay_dict()
            else:
                params['trade_fund_list'] = self.trade_fund_list
        if self.trade_goods_list:
            if isinstance(self.trade_goods_list, list):
                for i in range(0, len(self.trade_goods_list)):
                    element = self.trade_goods_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_goods_list[i] = element.to_alipay_dict()
            if hasattr(self.trade_goods_list, 'to_alipay_dict'):
                params['trade_goods_list'] = self.trade_goods_list.to_alipay_dict()
            else:
                params['trade_goods_list'] = self.trade_goods_list
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceTradeInfo()
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'create_trade_date' in d:
            o.create_trade_date = d['create_trade_date']
        if 'einv_trade_id' in d:
            o.einv_trade_id = d['einv_trade_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'invoice_content' in d:
            o.invoice_content = d['invoice_content']
        if 'm_name' in d:
            o.m_name = d['m_name']
        if 'm_short_name' in d:
            o.m_short_name = d['m_short_name']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payment_trade_date' in d:
            o.payment_trade_date = d['payment_trade_date']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'sub_m_name' in d:
            o.sub_m_name = d['sub_m_name']
        if 'sub_m_short_name' in d:
            o.sub_m_short_name = d['sub_m_short_name']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_fund_list' in d:
            o.trade_fund_list = d['trade_fund_list']
        if 'trade_goods_list' in d:
            o.trade_goods_list = d['trade_goods_list']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


