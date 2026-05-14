#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRentOrderDispatchConfirmModel(object):

    def __init__(self):
        self._buyer_id = None
        self._buyer_open_id = None
        self._operation_type = None
        self._reason_desc = None
        self._rent_dispatch_id = None

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
    def reason_desc(self):
        return self._reason_desc

    @reason_desc.setter
    def reason_desc(self, value):
        self._reason_desc = value
    @property
    def rent_dispatch_id(self):
        return self._rent_dispatch_id

    @rent_dispatch_id.setter
    def rent_dispatch_id(self, value):
        self._rent_dispatch_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.reason_desc:
            if hasattr(self.reason_desc, 'to_alipay_dict'):
                params['reason_desc'] = self.reason_desc.to_alipay_dict()
            else:
                params['reason_desc'] = self.reason_desc
        if self.rent_dispatch_id:
            if hasattr(self.rent_dispatch_id, 'to_alipay_dict'):
                params['rent_dispatch_id'] = self.rent_dispatch_id.to_alipay_dict()
            else:
                params['rent_dispatch_id'] = self.rent_dispatch_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentOrderDispatchConfirmModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'reason_desc' in d:
            o.reason_desc = d['reason_desc']
        if 'rent_dispatch_id' in d:
            o.rent_dispatch_id = d['rent_dispatch_id']
        return o


