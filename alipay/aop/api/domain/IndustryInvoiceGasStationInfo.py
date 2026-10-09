#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndustryInvoiceGasStationInfo(object):

    def __init__(self):
        self._channel_type = None
        self._gas_gun_no = None
        self._gas_station_name = None
        self._gas_station_tax_no = None
        self._invoice_trigger_type = None
        self._item_amount = None
        self._item_num = None
        self._order_status = None
        self._pay_time = None
        self._plate_no = None
        self._related_item_serial_no = None
        self._serial_no = None
        self._trade_biz_no = None
        self._trade_no = None
        self._trade_product = None
        self._unit_price = None

    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def gas_gun_no(self):
        return self._gas_gun_no

    @gas_gun_no.setter
    def gas_gun_no(self, value):
        self._gas_gun_no = value
    @property
    def gas_station_name(self):
        return self._gas_station_name

    @gas_station_name.setter
    def gas_station_name(self, value):
        self._gas_station_name = value
    @property
    def gas_station_tax_no(self):
        return self._gas_station_tax_no

    @gas_station_tax_no.setter
    def gas_station_tax_no(self, value):
        self._gas_station_tax_no = value
    @property
    def invoice_trigger_type(self):
        return self._invoice_trigger_type

    @invoice_trigger_type.setter
    def invoice_trigger_type(self, value):
        self._invoice_trigger_type = value
    @property
    def item_amount(self):
        return self._item_amount

    @item_amount.setter
    def item_amount(self, value):
        self._item_amount = value
    @property
    def item_num(self):
        return self._item_num

    @item_num.setter
    def item_num(self, value):
        self._item_num = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def related_item_serial_no(self):
        return self._related_item_serial_no

    @related_item_serial_no.setter
    def related_item_serial_no(self, value):
        self._related_item_serial_no = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def trade_biz_no(self):
        return self._trade_biz_no

    @trade_biz_no.setter
    def trade_biz_no(self, value):
        self._trade_biz_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_product(self):
        return self._trade_product

    @trade_product.setter
    def trade_product(self, value):
        self._trade_product = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.gas_gun_no:
            if hasattr(self.gas_gun_no, 'to_alipay_dict'):
                params['gas_gun_no'] = self.gas_gun_no.to_alipay_dict()
            else:
                params['gas_gun_no'] = self.gas_gun_no
        if self.gas_station_name:
            if hasattr(self.gas_station_name, 'to_alipay_dict'):
                params['gas_station_name'] = self.gas_station_name.to_alipay_dict()
            else:
                params['gas_station_name'] = self.gas_station_name
        if self.gas_station_tax_no:
            if hasattr(self.gas_station_tax_no, 'to_alipay_dict'):
                params['gas_station_tax_no'] = self.gas_station_tax_no.to_alipay_dict()
            else:
                params['gas_station_tax_no'] = self.gas_station_tax_no
        if self.invoice_trigger_type:
            if hasattr(self.invoice_trigger_type, 'to_alipay_dict'):
                params['invoice_trigger_type'] = self.invoice_trigger_type.to_alipay_dict()
            else:
                params['invoice_trigger_type'] = self.invoice_trigger_type
        if self.item_amount:
            if hasattr(self.item_amount, 'to_alipay_dict'):
                params['item_amount'] = self.item_amount.to_alipay_dict()
            else:
                params['item_amount'] = self.item_amount
        if self.item_num:
            if hasattr(self.item_num, 'to_alipay_dict'):
                params['item_num'] = self.item_num.to_alipay_dict()
            else:
                params['item_num'] = self.item_num
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.related_item_serial_no:
            if hasattr(self.related_item_serial_no, 'to_alipay_dict'):
                params['related_item_serial_no'] = self.related_item_serial_no.to_alipay_dict()
            else:
                params['related_item_serial_no'] = self.related_item_serial_no
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.trade_biz_no:
            if hasattr(self.trade_biz_no, 'to_alipay_dict'):
                params['trade_biz_no'] = self.trade_biz_no.to_alipay_dict()
            else:
                params['trade_biz_no'] = self.trade_biz_no
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_product:
            if hasattr(self.trade_product, 'to_alipay_dict'):
                params['trade_product'] = self.trade_product.to_alipay_dict()
            else:
                params['trade_product'] = self.trade_product
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryInvoiceGasStationInfo()
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'gas_gun_no' in d:
            o.gas_gun_no = d['gas_gun_no']
        if 'gas_station_name' in d:
            o.gas_station_name = d['gas_station_name']
        if 'gas_station_tax_no' in d:
            o.gas_station_tax_no = d['gas_station_tax_no']
        if 'invoice_trigger_type' in d:
            o.invoice_trigger_type = d['invoice_trigger_type']
        if 'item_amount' in d:
            o.item_amount = d['item_amount']
        if 'item_num' in d:
            o.item_num = d['item_num']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'related_item_serial_no' in d:
            o.related_item_serial_no = d['related_item_serial_no']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'trade_biz_no' in d:
            o.trade_biz_no = d['trade_biz_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_product' in d:
            o.trade_product = d['trade_product']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o


