#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AftersaleItemInfoDTO import AftersaleItemInfoDTO
from alipay.aop.api.domain.AftersaleAddressInfoDTO import AftersaleAddressInfoDTO


class AlipayOpenMiniOrderAftersaleCreateModel(object):

    def __init__(self):
        self._aftersale_reason_code = None
        self._item_infos = None
        self._merchant_address_info = None
        self._open_id = None
        self._order_id = None
        self._out_aftersale_id = None
        self._out_order_id = None
        self._path = None
        self._refund_amount = None
        self._refund_reason = None
        self._type = None
        self._user_id = None

    @property
    def aftersale_reason_code(self):
        return self._aftersale_reason_code

    @aftersale_reason_code.setter
    def aftersale_reason_code(self, value):
        self._aftersale_reason_code = value
    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, list):
            self._item_infos = list()
            for i in value:
                if isinstance(i, AftersaleItemInfoDTO):
                    self._item_infos.append(i)
                else:
                    self._item_infos.append(AftersaleItemInfoDTO.from_alipay_dict(i))
    @property
    def merchant_address_info(self):
        return self._merchant_address_info

    @merchant_address_info.setter
    def merchant_address_info(self, value):
        if isinstance(value, AftersaleAddressInfoDTO):
            self._merchant_address_info = value
        else:
            self._merchant_address_info = AftersaleAddressInfoDTO.from_alipay_dict(value)
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
    def out_aftersale_id(self):
        return self._out_aftersale_id

    @out_aftersale_id.setter
    def out_aftersale_id(self, value):
        self._out_aftersale_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.aftersale_reason_code:
            if hasattr(self.aftersale_reason_code, 'to_alipay_dict'):
                params['aftersale_reason_code'] = self.aftersale_reason_code.to_alipay_dict()
            else:
                params['aftersale_reason_code'] = self.aftersale_reason_code
        if self.item_infos:
            if isinstance(self.item_infos, list):
                for i in range(0, len(self.item_infos)):
                    element = self.item_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_infos[i] = element.to_alipay_dict()
            if hasattr(self.item_infos, 'to_alipay_dict'):
                params['item_infos'] = self.item_infos.to_alipay_dict()
            else:
                params['item_infos'] = self.item_infos
        if self.merchant_address_info:
            if hasattr(self.merchant_address_info, 'to_alipay_dict'):
                params['merchant_address_info'] = self.merchant_address_info.to_alipay_dict()
            else:
                params['merchant_address_info'] = self.merchant_address_info
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
        if self.out_aftersale_id:
            if hasattr(self.out_aftersale_id, 'to_alipay_dict'):
                params['out_aftersale_id'] = self.out_aftersale_id.to_alipay_dict()
            else:
                params['out_aftersale_id'] = self.out_aftersale_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        o = AlipayOpenMiniOrderAftersaleCreateModel()
        if 'aftersale_reason_code' in d:
            o.aftersale_reason_code = d['aftersale_reason_code']
        if 'item_infos' in d:
            o.item_infos = d['item_infos']
        if 'merchant_address_info' in d:
            o.merchant_address_info = d['merchant_address_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_aftersale_id' in d:
            o.out_aftersale_id = d['out_aftersale_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'path' in d:
            o.path = d['path']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


