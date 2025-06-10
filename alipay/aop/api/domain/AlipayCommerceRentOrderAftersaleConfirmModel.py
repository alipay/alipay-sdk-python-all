#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AftersaleMediaInfoVO import AftersaleMediaInfoVO


class AlipayCommerceRentOrderAftersaleConfirmModel(object):

    def __init__(self):
        self._additional_description = None
        self._additional_media_list = None
        self._aftersale_id = None
        self._buyer_id = None
        self._buyer_open_id = None
        self._operation_type = None
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
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
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
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
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
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'reason_code' in d:
            o.reason_code = d['reason_code']
        return o


