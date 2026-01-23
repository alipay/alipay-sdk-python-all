#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleModifyAddressInfo import RecycleModifyAddressInfo
from alipay.aop.api.domain.RecycleSendContactInfo import RecycleSendContactInfo


class AlipayCommerceRecycleOrderModifyModel(object):

    def __init__(self):
        self._address_info = None
        self._modify_reason = None
        self._open_id = None
        self._order_id = None
        self._out_order_id = None
        self._send_order_contact_info = None
        self._user_id = None

    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, RecycleModifyAddressInfo):
            self._address_info = value
        else:
            self._address_info = RecycleModifyAddressInfo.from_alipay_dict(value)
    @property
    def modify_reason(self):
        return self._modify_reason

    @modify_reason.setter
    def modify_reason(self, value):
        self._modify_reason = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def send_order_contact_info(self):
        return self._send_order_contact_info

    @send_order_contact_info.setter
    def send_order_contact_info(self, value):
        if isinstance(value, RecycleSendContactInfo):
            self._send_order_contact_info = value
        else:
            self._send_order_contact_info = RecycleSendContactInfo.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_info:
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
        if self.modify_reason:
            if hasattr(self.modify_reason, 'to_alipay_dict'):
                params['modify_reason'] = self.modify_reason.to_alipay_dict()
            else:
                params['modify_reason'] = self.modify_reason
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.send_order_contact_info:
            if hasattr(self.send_order_contact_info, 'to_alipay_dict'):
                params['send_order_contact_info'] = self.send_order_contact_info.to_alipay_dict()
            else:
                params['send_order_contact_info'] = self.send_order_contact_info
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
        o = AlipayCommerceRecycleOrderModifyModel()
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'modify_reason' in d:
            o.modify_reason = d['modify_reason']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'send_order_contact_info' in d:
            o.send_order_contact_info = d['send_order_contact_info']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


