#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IsvMerchantSalesDetailRequest(object):

    def __init__(self):
        self._coupons_quantity = None
        self._device_detail = None
        self._merchant_pid = None
        self._mini_appid = None
        self._operation_place = None
        self._out_biz_no = None
        self._promotor_pid = None
        self._sales_amount = None
        self._sales_quantity = None
        self._sub_promotor_pid = None
        self._write_off_amount = None
        self._write_off_quantity = None

    @property
    def coupons_quantity(self):
        return self._coupons_quantity

    @coupons_quantity.setter
    def coupons_quantity(self, value):
        self._coupons_quantity = value
    @property
    def device_detail(self):
        return self._device_detail

    @device_detail.setter
    def device_detail(self, value):
        self._device_detail = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def mini_appid(self):
        return self._mini_appid

    @mini_appid.setter
    def mini_appid(self, value):
        self._mini_appid = value
    @property
    def operation_place(self):
        return self._operation_place

    @operation_place.setter
    def operation_place(self, value):
        self._operation_place = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def promotor_pid(self):
        return self._promotor_pid

    @promotor_pid.setter
    def promotor_pid(self, value):
        self._promotor_pid = value
    @property
    def sales_amount(self):
        return self._sales_amount

    @sales_amount.setter
    def sales_amount(self, value):
        self._sales_amount = value
    @property
    def sales_quantity(self):
        return self._sales_quantity

    @sales_quantity.setter
    def sales_quantity(self, value):
        self._sales_quantity = value
    @property
    def sub_promotor_pid(self):
        return self._sub_promotor_pid

    @sub_promotor_pid.setter
    def sub_promotor_pid(self, value):
        self._sub_promotor_pid = value
    @property
    def write_off_amount(self):
        return self._write_off_amount

    @write_off_amount.setter
    def write_off_amount(self, value):
        self._write_off_amount = value
    @property
    def write_off_quantity(self):
        return self._write_off_quantity

    @write_off_quantity.setter
    def write_off_quantity(self, value):
        self._write_off_quantity = value


    def to_alipay_dict(self):
        params = dict()
        if self.coupons_quantity:
            if hasattr(self.coupons_quantity, 'to_alipay_dict'):
                params['coupons_quantity'] = self.coupons_quantity.to_alipay_dict()
            else:
                params['coupons_quantity'] = self.coupons_quantity
        if self.device_detail:
            if hasattr(self.device_detail, 'to_alipay_dict'):
                params['device_detail'] = self.device_detail.to_alipay_dict()
            else:
                params['device_detail'] = self.device_detail
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.mini_appid:
            if hasattr(self.mini_appid, 'to_alipay_dict'):
                params['mini_appid'] = self.mini_appid.to_alipay_dict()
            else:
                params['mini_appid'] = self.mini_appid
        if self.operation_place:
            if hasattr(self.operation_place, 'to_alipay_dict'):
                params['operation_place'] = self.operation_place.to_alipay_dict()
            else:
                params['operation_place'] = self.operation_place
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.promotor_pid:
            if hasattr(self.promotor_pid, 'to_alipay_dict'):
                params['promotor_pid'] = self.promotor_pid.to_alipay_dict()
            else:
                params['promotor_pid'] = self.promotor_pid
        if self.sales_amount:
            if hasattr(self.sales_amount, 'to_alipay_dict'):
                params['sales_amount'] = self.sales_amount.to_alipay_dict()
            else:
                params['sales_amount'] = self.sales_amount
        if self.sales_quantity:
            if hasattr(self.sales_quantity, 'to_alipay_dict'):
                params['sales_quantity'] = self.sales_quantity.to_alipay_dict()
            else:
                params['sales_quantity'] = self.sales_quantity
        if self.sub_promotor_pid:
            if hasattr(self.sub_promotor_pid, 'to_alipay_dict'):
                params['sub_promotor_pid'] = self.sub_promotor_pid.to_alipay_dict()
            else:
                params['sub_promotor_pid'] = self.sub_promotor_pid
        if self.write_off_amount:
            if hasattr(self.write_off_amount, 'to_alipay_dict'):
                params['write_off_amount'] = self.write_off_amount.to_alipay_dict()
            else:
                params['write_off_amount'] = self.write_off_amount
        if self.write_off_quantity:
            if hasattr(self.write_off_quantity, 'to_alipay_dict'):
                params['write_off_quantity'] = self.write_off_quantity.to_alipay_dict()
            else:
                params['write_off_quantity'] = self.write_off_quantity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IsvMerchantSalesDetailRequest()
        if 'coupons_quantity' in d:
            o.coupons_quantity = d['coupons_quantity']
        if 'device_detail' in d:
            o.device_detail = d['device_detail']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'mini_appid' in d:
            o.mini_appid = d['mini_appid']
        if 'operation_place' in d:
            o.operation_place = d['operation_place']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'promotor_pid' in d:
            o.promotor_pid = d['promotor_pid']
        if 'sales_amount' in d:
            o.sales_amount = d['sales_amount']
        if 'sales_quantity' in d:
            o.sales_quantity = d['sales_quantity']
        if 'sub_promotor_pid' in d:
            o.sub_promotor_pid = d['sub_promotor_pid']
        if 'write_off_amount' in d:
            o.write_off_amount = d['write_off_amount']
        if 'write_off_quantity' in d:
            o.write_off_quantity = d['write_off_quantity']
        return o


