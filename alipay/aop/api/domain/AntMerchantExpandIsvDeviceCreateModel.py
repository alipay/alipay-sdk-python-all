#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryInfo import DeliveryInfo
from alipay.aop.api.domain.DeviceApplyTemplate import DeviceApplyTemplate


class AntMerchantExpandIsvDeviceCreateModel(object):

    def __init__(self):
        self._biz_type = None
        self._channel_isv_pid = None
        self._delivery_info = None
        self._device_list = None
        self._operator_contact = None
        self._operator_name = None
        self._pid = None
        self._reason = None
        self._shop_id = None
        self._usage_detail = None
        self._usage_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def channel_isv_pid(self):
        return self._channel_isv_pid

    @channel_isv_pid.setter
    def channel_isv_pid(self, value):
        self._channel_isv_pid = value
    @property
    def delivery_info(self):
        return self._delivery_info

    @delivery_info.setter
    def delivery_info(self, value):
        if isinstance(value, DeliveryInfo):
            self._delivery_info = value
        else:
            self._delivery_info = DeliveryInfo.from_alipay_dict(value)
    @property
    def device_list(self):
        return self._device_list

    @device_list.setter
    def device_list(self, value):
        if isinstance(value, list):
            self._device_list = list()
            for i in value:
                if isinstance(i, DeviceApplyTemplate):
                    self._device_list.append(i)
                else:
                    self._device_list.append(DeviceApplyTemplate.from_alipay_dict(i))
    @property
    def operator_contact(self):
        return self._operator_contact

    @operator_contact.setter
    def operator_contact(self, value):
        self._operator_contact = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def usage_detail(self):
        return self._usage_detail

    @usage_detail.setter
    def usage_detail(self, value):
        self._usage_detail = value
    @property
    def usage_type(self):
        return self._usage_type

    @usage_type.setter
    def usage_type(self, value):
        self._usage_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.channel_isv_pid:
            if hasattr(self.channel_isv_pid, 'to_alipay_dict'):
                params['channel_isv_pid'] = self.channel_isv_pid.to_alipay_dict()
            else:
                params['channel_isv_pid'] = self.channel_isv_pid
        if self.delivery_info:
            if hasattr(self.delivery_info, 'to_alipay_dict'):
                params['delivery_info'] = self.delivery_info.to_alipay_dict()
            else:
                params['delivery_info'] = self.delivery_info
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
        if self.operator_contact:
            if hasattr(self.operator_contact, 'to_alipay_dict'):
                params['operator_contact'] = self.operator_contact.to_alipay_dict()
            else:
                params['operator_contact'] = self.operator_contact
        if self.operator_name:
            if hasattr(self.operator_name, 'to_alipay_dict'):
                params['operator_name'] = self.operator_name.to_alipay_dict()
            else:
                params['operator_name'] = self.operator_name
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.usage_detail:
            if hasattr(self.usage_detail, 'to_alipay_dict'):
                params['usage_detail'] = self.usage_detail.to_alipay_dict()
            else:
                params['usage_detail'] = self.usage_detail
        if self.usage_type:
            if hasattr(self.usage_type, 'to_alipay_dict'):
                params['usage_type'] = self.usage_type.to_alipay_dict()
            else:
                params['usage_type'] = self.usage_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIsvDeviceCreateModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'channel_isv_pid' in d:
            o.channel_isv_pid = d['channel_isv_pid']
        if 'delivery_info' in d:
            o.delivery_info = d['delivery_info']
        if 'device_list' in d:
            o.device_list = d['device_list']
        if 'operator_contact' in d:
            o.operator_contact = d['operator_contact']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        if 'pid' in d:
            o.pid = d['pid']
        if 'reason' in d:
            o.reason = d['reason']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'usage_detail' in d:
            o.usage_detail = d['usage_detail']
        if 'usage_type' in d:
            o.usage_type = d['usage_type']
        return o


