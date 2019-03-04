#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KdsDeviceModel import KdsDeviceModel
from alipay.aop.api.domain.KdsPrinterModel import KdsPrinterModel


class KdsInfoModel(object):

    def __init__(self):
        self._delete_flag = None
        self._device_list = None
        self._dinner_type = None
        self._has_device = None
        self._has_stall = None
        self._kds_id = None
        self._kds_name = None
        self._kds_type = None
        self._print_flag = None
        self._printer_device_id = None
        self._printer_list = None
        self._shop_id = None

    @property
    def delete_flag(self):
        return self._delete_flag

    @delete_flag.setter
    def delete_flag(self, value):
        self._delete_flag = value
    @property
    def device_list(self):
        return self._device_list

    @device_list.setter
    def device_list(self, value):
        if isinstance(value, list):
            self._device_list = list()
            for i in value:
                if isinstance(i, KdsDeviceModel):
                    self._device_list.append(i)
                else:
                    self._device_list.append(KdsDeviceModel.from_alipay_dict(i))
    @property
    def dinner_type(self):
        return self._dinner_type

    @dinner_type.setter
    def dinner_type(self, value):
        if isinstance(value, list):
            self._dinner_type = list()
            for i in value:
                self._dinner_type.append(i)
    @property
    def has_device(self):
        return self._has_device

    @has_device.setter
    def has_device(self, value):
        self._has_device = value
    @property
    def has_stall(self):
        return self._has_stall

    @has_stall.setter
    def has_stall(self, value):
        self._has_stall = value
    @property
    def kds_id(self):
        return self._kds_id

    @kds_id.setter
    def kds_id(self, value):
        self._kds_id = value
    @property
    def kds_name(self):
        return self._kds_name

    @kds_name.setter
    def kds_name(self, value):
        self._kds_name = value
    @property
    def kds_type(self):
        return self._kds_type

    @kds_type.setter
    def kds_type(self, value):
        self._kds_type = value
    @property
    def print_flag(self):
        return self._print_flag

    @print_flag.setter
    def print_flag(self, value):
        self._print_flag = value
    @property
    def printer_device_id(self):
        return self._printer_device_id

    @printer_device_id.setter
    def printer_device_id(self, value):
        self._printer_device_id = value
    @property
    def printer_list(self):
        return self._printer_list

    @printer_list.setter
    def printer_list(self, value):
        if isinstance(value, list):
            self._printer_list = list()
            for i in value:
                if isinstance(i, KdsPrinterModel):
                    self._printer_list.append(i)
                else:
                    self._printer_list.append(KdsPrinterModel.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.delete_flag:
            if hasattr(self.delete_flag, 'to_alipay_dict'):
                params['delete_flag'] = self.delete_flag.to_alipay_dict()
            else:
                params['delete_flag'] = self.delete_flag
        if self.device_list:
            if isinstance(self.device_list, list):
                for i in range(0, len(self.device_list)):
                    element = self.device_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_list[i] = element.to_alipay_dict()
            if hasattr(self.device_list, 'to_alipay_dict'):
                params['device_list'] = self.device_list.to_alipay_dict()
            else:
                params['device_list'] = self.device_list
        if self.dinner_type:
            if isinstance(self.dinner_type, list):
                for i in range(0, len(self.dinner_type)):
                    element = self.dinner_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dinner_type[i] = element.to_alipay_dict()
            if hasattr(self.dinner_type, 'to_alipay_dict'):
                params['dinner_type'] = self.dinner_type.to_alipay_dict()
            else:
                params['dinner_type'] = self.dinner_type
        if self.has_device:
            if hasattr(self.has_device, 'to_alipay_dict'):
                params['has_device'] = self.has_device.to_alipay_dict()
            else:
                params['has_device'] = self.has_device
        if self.has_stall:
            if hasattr(self.has_stall, 'to_alipay_dict'):
                params['has_stall'] = self.has_stall.to_alipay_dict()
            else:
                params['has_stall'] = self.has_stall
        if self.kds_id:
            if hasattr(self.kds_id, 'to_alipay_dict'):
                params['kds_id'] = self.kds_id.to_alipay_dict()
            else:
                params['kds_id'] = self.kds_id
        if self.kds_name:
            if hasattr(self.kds_name, 'to_alipay_dict'):
                params['kds_name'] = self.kds_name.to_alipay_dict()
            else:
                params['kds_name'] = self.kds_name
        if self.kds_type:
            if hasattr(self.kds_type, 'to_alipay_dict'):
                params['kds_type'] = self.kds_type.to_alipay_dict()
            else:
                params['kds_type'] = self.kds_type
        if self.print_flag:
            if hasattr(self.print_flag, 'to_alipay_dict'):
                params['print_flag'] = self.print_flag.to_alipay_dict()
            else:
                params['print_flag'] = self.print_flag
        if self.printer_device_id:
            if hasattr(self.printer_device_id, 'to_alipay_dict'):
                params['printer_device_id'] = self.printer_device_id.to_alipay_dict()
            else:
                params['printer_device_id'] = self.printer_device_id
        if self.printer_list:
            if isinstance(self.printer_list, list):
                for i in range(0, len(self.printer_list)):
                    element = self.printer_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.printer_list[i] = element.to_alipay_dict()
            if hasattr(self.printer_list, 'to_alipay_dict'):
                params['printer_list'] = self.printer_list.to_alipay_dict()
            else:
                params['printer_list'] = self.printer_list
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KdsInfoModel()
        if 'delete_flag' in d:
            o.delete_flag = d['delete_flag']
        if 'device_list' in d:
            o.device_list = d['device_list']
        if 'dinner_type' in d:
            o.dinner_type = d['dinner_type']
        if 'has_device' in d:
            o.has_device = d['has_device']
        if 'has_stall' in d:
            o.has_stall = d['has_stall']
        if 'kds_id' in d:
            o.kds_id = d['kds_id']
        if 'kds_name' in d:
            o.kds_name = d['kds_name']
        if 'kds_type' in d:
            o.kds_type = d['kds_type']
        if 'print_flag' in d:
            o.print_flag = d['print_flag']
        if 'printer_device_id' in d:
            o.printer_device_id = d['printer_device_id']
        if 'printer_list' in d:
            o.printer_list = d['printer_list']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


