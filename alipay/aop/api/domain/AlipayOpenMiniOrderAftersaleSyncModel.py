#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AftersaleLogisticsInfoDTO import AftersaleLogisticsInfoDTO
from alipay.aop.api.domain.AftersaleAddressInfoDTO import AftersaleAddressInfoDTO


class AlipayOpenMiniOrderAftersaleSyncModel(object):

    def __init__(self):
        self._action_code = None
        self._aftersale_id = None
        self._audit_reason = None
        self._audit_status = None
        self._logistics_list = None
        self._merchant_address_info = None
        self._merchant_agree_refund_amount = None
        self._open_id = None
        self._order_id = None
        self._out_order_id = None
        self._out_refund_request_no_list = None
        self._return_delivery_type = None
        self._user_id = None

    @property
    def action_code(self):
        return self._action_code

    @action_code.setter
    def action_code(self, value):
        self._action_code = value
    @property
    def aftersale_id(self):
        return self._aftersale_id

    @aftersale_id.setter
    def aftersale_id(self, value):
        self._aftersale_id = value
    @property
    def audit_reason(self):
        return self._audit_reason

    @audit_reason.setter
    def audit_reason(self, value):
        self._audit_reason = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def logistics_list(self):
        return self._logistics_list

    @logistics_list.setter
    def logistics_list(self, value):
        if isinstance(value, list):
            self._logistics_list = list()
            for i in value:
                if isinstance(i, AftersaleLogisticsInfoDTO):
                    self._logistics_list.append(i)
                else:
                    self._logistics_list.append(AftersaleLogisticsInfoDTO.from_alipay_dict(i))
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
    def merchant_agree_refund_amount(self):
        return self._merchant_agree_refund_amount

    @merchant_agree_refund_amount.setter
    def merchant_agree_refund_amount(self, value):
        self._merchant_agree_refund_amount = value
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
    def out_refund_request_no_list(self):
        return self._out_refund_request_no_list

    @out_refund_request_no_list.setter
    def out_refund_request_no_list(self, value):
        if isinstance(value, list):
            self._out_refund_request_no_list = list()
            for i in value:
                self._out_refund_request_no_list.append(i)
    @property
    def return_delivery_type(self):
        return self._return_delivery_type

    @return_delivery_type.setter
    def return_delivery_type(self, value):
        self._return_delivery_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_code:
            if hasattr(self.action_code, 'to_alipay_dict'):
                params['action_code'] = self.action_code.to_alipay_dict()
            else:
                params['action_code'] = self.action_code
        if self.aftersale_id:
            if hasattr(self.aftersale_id, 'to_alipay_dict'):
                params['aftersale_id'] = self.aftersale_id.to_alipay_dict()
            else:
                params['aftersale_id'] = self.aftersale_id
        if self.audit_reason:
            if hasattr(self.audit_reason, 'to_alipay_dict'):
                params['audit_reason'] = self.audit_reason.to_alipay_dict()
            else:
                params['audit_reason'] = self.audit_reason
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.logistics_list:
            if isinstance(self.logistics_list, list):
                for i in range(0, len(self.logistics_list)):
                    element = self.logistics_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logistics_list[i] = element.to_alipay_dict()
            if hasattr(self.logistics_list, 'to_alipay_dict'):
                params['logistics_list'] = self.logistics_list.to_alipay_dict()
            else:
                params['logistics_list'] = self.logistics_list
        if self.merchant_address_info:
            if hasattr(self.merchant_address_info, 'to_alipay_dict'):
                params['merchant_address_info'] = self.merchant_address_info.to_alipay_dict()
            else:
                params['merchant_address_info'] = self.merchant_address_info
        if self.merchant_agree_refund_amount:
            if hasattr(self.merchant_agree_refund_amount, 'to_alipay_dict'):
                params['merchant_agree_refund_amount'] = self.merchant_agree_refund_amount.to_alipay_dict()
            else:
                params['merchant_agree_refund_amount'] = self.merchant_agree_refund_amount
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
        if self.out_refund_request_no_list:
            if isinstance(self.out_refund_request_no_list, list):
                for i in range(0, len(self.out_refund_request_no_list)):
                    element = self.out_refund_request_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_refund_request_no_list[i] = element.to_alipay_dict()
            if hasattr(self.out_refund_request_no_list, 'to_alipay_dict'):
                params['out_refund_request_no_list'] = self.out_refund_request_no_list.to_alipay_dict()
            else:
                params['out_refund_request_no_list'] = self.out_refund_request_no_list
        if self.return_delivery_type:
            if hasattr(self.return_delivery_type, 'to_alipay_dict'):
                params['return_delivery_type'] = self.return_delivery_type.to_alipay_dict()
            else:
                params['return_delivery_type'] = self.return_delivery_type
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
        o = AlipayOpenMiniOrderAftersaleSyncModel()
        if 'action_code' in d:
            o.action_code = d['action_code']
        if 'aftersale_id' in d:
            o.aftersale_id = d['aftersale_id']
        if 'audit_reason' in d:
            o.audit_reason = d['audit_reason']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'logistics_list' in d:
            o.logistics_list = d['logistics_list']
        if 'merchant_address_info' in d:
            o.merchant_address_info = d['merchant_address_info']
        if 'merchant_agree_refund_amount' in d:
            o.merchant_agree_refund_amount = d['merchant_agree_refund_amount']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_refund_request_no_list' in d:
            o.out_refund_request_no_list = d['out_refund_request_no_list']
        if 'return_delivery_type' in d:
            o.return_delivery_type = d['return_delivery_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


