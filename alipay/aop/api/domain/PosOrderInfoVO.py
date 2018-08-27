#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PosOrderDeviceInfoVO import PosOrderDeviceInfoVO


class PosOrderInfoVO(object):

    def __init__(self):
        self._device_amount = None
        self._isv_name = None
        self._isv_pid = None
        self._machine_infos = None
        self._merchant_mobile = None
        self._merchant_name = None
        self._order_amt = None
        self._order_channel = None
        self._order_no = None
        self._seller_id = None
        self._seller_name = None
        self._taobao_login_id = None

    @property
    def device_amount(self):
        return self._device_amount

    @device_amount.setter
    def device_amount(self, value):
        self._device_amount = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def machine_infos(self):
        return self._machine_infos

    @machine_infos.setter
    def machine_infos(self, value):
        if isinstance(value, list):
            self._machine_infos = list()
            for i in value:
                if isinstance(i, PosOrderDeviceInfoVO):
                    self._machine_infos.append(i)
                else:
                    self._machine_infos.append(PosOrderDeviceInfoVO.from_alipay_dict(i))
    @property
    def merchant_mobile(self):
        return self._merchant_mobile

    @merchant_mobile.setter
    def merchant_mobile(self, value):
        self._merchant_mobile = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def order_amt(self):
        return self._order_amt

    @order_amt.setter
    def order_amt(self, value):
        self._order_amt = value
    @property
    def order_channel(self):
        return self._order_channel

    @order_channel.setter
    def order_channel(self, value):
        self._order_channel = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def seller_name(self):
        return self._seller_name

    @seller_name.setter
    def seller_name(self, value):
        self._seller_name = value
    @property
    def taobao_login_id(self):
        return self._taobao_login_id

    @taobao_login_id.setter
    def taobao_login_id(self, value):
        self._taobao_login_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_amount:
            if hasattr(self.device_amount, 'to_alipay_dict'):
                params['device_amount'] = self.device_amount.to_alipay_dict()
            else:
                params['device_amount'] = self.device_amount
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.machine_infos:
            if isinstance(self.machine_infos, list):
                for i in range(0, len(self.machine_infos)):
                    element = self.machine_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.machine_infos[i] = element.to_alipay_dict()
            if hasattr(self.machine_infos, 'to_alipay_dict'):
                params['machine_infos'] = self.machine_infos.to_alipay_dict()
            else:
                params['machine_infos'] = self.machine_infos
        if self.merchant_mobile:
            if hasattr(self.merchant_mobile, 'to_alipay_dict'):
                params['merchant_mobile'] = self.merchant_mobile.to_alipay_dict()
            else:
                params['merchant_mobile'] = self.merchant_mobile
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.order_amt:
            if hasattr(self.order_amt, 'to_alipay_dict'):
                params['order_amt'] = self.order_amt.to_alipay_dict()
            else:
                params['order_amt'] = self.order_amt
        if self.order_channel:
            if hasattr(self.order_channel, 'to_alipay_dict'):
                params['order_channel'] = self.order_channel.to_alipay_dict()
            else:
                params['order_channel'] = self.order_channel
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.seller_name:
            if hasattr(self.seller_name, 'to_alipay_dict'):
                params['seller_name'] = self.seller_name.to_alipay_dict()
            else:
                params['seller_name'] = self.seller_name
        if self.taobao_login_id:
            if hasattr(self.taobao_login_id, 'to_alipay_dict'):
                params['taobao_login_id'] = self.taobao_login_id.to_alipay_dict()
            else:
                params['taobao_login_id'] = self.taobao_login_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PosOrderInfoVO()
        if 'device_amount' in d:
            o.device_amount = d['device_amount']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'machine_infos' in d:
            o.machine_infos = d['machine_infos']
        if 'merchant_mobile' in d:
            o.merchant_mobile = d['merchant_mobile']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'order_amt' in d:
            o.order_amt = d['order_amt']
        if 'order_channel' in d:
            o.order_channel = d['order_channel']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'seller_name' in d:
            o.seller_name = d['seller_name']
        if 'taobao_login_id' in d:
            o.taobao_login_id = d['taobao_login_id']
        return o


