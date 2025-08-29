#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AftersaleMediaInfoVO import AftersaleMediaInfoVO
from alipay.aop.api.domain.AftersaleCompensationInfoVO import AftersaleCompensationInfoVO
from alipay.aop.api.domain.AftersalePayItemVO import AftersalePayItemVO


class AlipayCommerceRentOrderAftersaleConfirmModel(object):

    def __init__(self):
        self._additional_description = None
        self._additional_media_list = None
        self._aftersale_id = None
        self._buyer_id = None
        self._buyer_open_id = None
        self._compensation_info = None
        self._operation_type = None
        self._out_aftersale_id = None
        self._pay_amount = None
        self._pay_items = None
        self._reason_code = None

    @property
    def additional_description(self):
        return self._additional_description

    @additional_description.setter
    def additional_description(self, value):
        self._additional_description = value
    @property
    def additional_media_list(self):
        return self._additional_media_list

    @additional_media_list.setter
    def additional_media_list(self, value):
        if isinstance(value, list):
            self._additional_media_list = list()
            for i in value:
                if isinstance(i, AftersaleMediaInfoVO):
                    self._additional_media_list.append(i)
                else:
                    self._additional_media_list.append(AftersaleMediaInfoVO.from_alipay_dict(i))
    @property
    def aftersale_id(self):
        return self._aftersale_id

    @aftersale_id.setter
    def aftersale_id(self, value):
        self._aftersale_id = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def compensation_info(self):
        return self._compensation_info

    @compensation_info.setter
    def compensation_info(self, value):
        if isinstance(value, AftersaleCompensationInfoVO):
            self._compensation_info = value
        else:
            self._compensation_info = AftersaleCompensationInfoVO.from_alipay_dict(value)
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def out_aftersale_id(self):
        return self._out_aftersale_id

    @out_aftersale_id.setter
    def out_aftersale_id(self, value):
        self._out_aftersale_id = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_items(self):
        return self._pay_items

    @pay_items.setter
    def pay_items(self, value):
        if isinstance(value, list):
            self._pay_items = list()
            for i in value:
                if isinstance(i, AftersalePayItemVO):
                    self._pay_items.append(i)
                else:
                    self._pay_items.append(AftersalePayItemVO.from_alipay_dict(i))
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.additional_description:
            if hasattr(self.additional_description, 'to_alipay_dict'):
                params['additional_description'] = self.additional_description.to_alipay_dict()
            else:
                params['additional_description'] = self.additional_description
        if self.additional_media_list:
            if isinstance(self.additional_media_list, list):
                for i in range(0, len(self.additional_media_list)):
                    element = self.additional_media_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.additional_media_list[i] = element.to_alipay_dict()
            if hasattr(self.additional_media_list, 'to_alipay_dict'):
                params['additional_media_list'] = self.additional_media_list.to_alipay_dict()
            else:
                params['additional_media_list'] = self.additional_media_list
        if self.aftersale_id:
            if hasattr(self.aftersale_id, 'to_alipay_dict'):
                params['aftersale_id'] = self.aftersale_id.to_alipay_dict()
            else:
                params['aftersale_id'] = self.aftersale_id
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.compensation_info:
            if hasattr(self.compensation_info, 'to_alipay_dict'):
                params['compensation_info'] = self.compensation_info.to_alipay_dict()
            else:
                params['compensation_info'] = self.compensation_info
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.out_aftersale_id:
            if hasattr(self.out_aftersale_id, 'to_alipay_dict'):
                params['out_aftersale_id'] = self.out_aftersale_id.to_alipay_dict()
            else:
                params['out_aftersale_id'] = self.out_aftersale_id
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_items:
            if isinstance(self.pay_items, list):
                for i in range(0, len(self.pay_items)):
                    element = self.pay_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_items[i] = element.to_alipay_dict()
            if hasattr(self.pay_items, 'to_alipay_dict'):
                params['pay_items'] = self.pay_items.to_alipay_dict()
            else:
                params['pay_items'] = self.pay_items
        if self.reason_code:
            if hasattr(self.reason_code, 'to_alipay_dict'):
                params['reason_code'] = self.reason_code.to_alipay_dict()
            else:
                params['reason_code'] = self.reason_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentOrderAftersaleConfirmModel()
        if 'additional_description' in d:
            o.additional_description = d['additional_description']
        if 'additional_media_list' in d:
            o.additional_media_list = d['additional_media_list']
        if 'aftersale_id' in d:
            o.aftersale_id = d['aftersale_id']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'compensation_info' in d:
            o.compensation_info = d['compensation_info']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'out_aftersale_id' in d:
            o.out_aftersale_id = d['out_aftersale_id']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_items' in d:
            o.pay_items = d['pay_items']
        if 'reason_code' in d:
            o.reason_code = d['reason_code']
        return o


