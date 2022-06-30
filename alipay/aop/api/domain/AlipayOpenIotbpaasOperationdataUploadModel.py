#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperationData import OperationData


class AlipayOpenIotbpaasOperationdataUploadModel(object):

    def __init__(self):
        self._date = None
        self._device_id = None
        self._device_sn = None
        self._operation_data_list = None
        self._partner_id = None
        self._shop_address = None
        self._shop_id = None
        self._shop_name = None
        self._smid = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def operation_data_list(self):
        return self._operation_data_list

    @operation_data_list.setter
    def operation_data_list(self, value):
        if isinstance(value, list):
            self._operation_data_list = list()
            for i in value:
                if isinstance(i, OperationData):
                    self._operation_data_list.append(i)
                else:
                    self._operation_data_list.append(OperationData.from_alipay_dict(i))
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def shop_address(self):
        return self._shop_address

    @shop_address.setter
    def shop_address(self, value):
        self._shop_address = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.operation_data_list:
            if isinstance(self.operation_data_list, list):
                for i in range(0, len(self.operation_data_list)):
                    element = self.operation_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operation_data_list[i] = element.to_alipay_dict()
            if hasattr(self.operation_data_list, 'to_alipay_dict'):
                params['operation_data_list'] = self.operation_data_list.to_alipay_dict()
            else:
                params['operation_data_list'] = self.operation_data_list
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.shop_address:
            if hasattr(self.shop_address, 'to_alipay_dict'):
                params['shop_address'] = self.shop_address.to_alipay_dict()
            else:
                params['shop_address'] = self.shop_address
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotbpaasOperationdataUploadModel()
        if 'date' in d:
            o.date = d['date']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'operation_data_list' in d:
            o.operation_data_list = d['operation_data_list']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'shop_address' in d:
            o.shop_address = d['shop_address']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'smid' in d:
            o.smid = d['smid']
        return o


