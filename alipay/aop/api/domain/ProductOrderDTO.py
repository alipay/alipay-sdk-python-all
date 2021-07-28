#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SignActivityDTO import SignActivityDTO


class ProductOrderDTO(object):

    def __init__(self):
        self._active_datetime = None
        self._inactive_datetime = None
        self._order_id = None
        self._order_user_id = None
        self._ordered_channel = None
        self._ordering_datetime = None
        self._out_merchant_id = None
        self._prod_name = None
        self._ps_code = None
        self._sign_activity_dto = None
        self._status = None

    @property
    def active_datetime(self):
        return self._active_datetime

    @active_datetime.setter
    def active_datetime(self, value):
        self._active_datetime = value
    @property
    def inactive_datetime(self):
        return self._inactive_datetime

    @inactive_datetime.setter
    def inactive_datetime(self, value):
        self._inactive_datetime = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_user_id(self):
        return self._order_user_id

    @order_user_id.setter
    def order_user_id(self, value):
        self._order_user_id = value
    @property
    def ordered_channel(self):
        return self._ordered_channel

    @ordered_channel.setter
    def ordered_channel(self, value):
        self._ordered_channel = value
    @property
    def ordering_datetime(self):
        return self._ordering_datetime

    @ordering_datetime.setter
    def ordering_datetime(self, value):
        self._ordering_datetime = value
    @property
    def out_merchant_id(self):
        return self._out_merchant_id

    @out_merchant_id.setter
    def out_merchant_id(self, value):
        self._out_merchant_id = value
    @property
    def prod_name(self):
        return self._prod_name

    @prod_name.setter
    def prod_name(self, value):
        self._prod_name = value
    @property
    def ps_code(self):
        return self._ps_code

    @ps_code.setter
    def ps_code(self, value):
        self._ps_code = value
    @property
    def sign_activity_dto(self):
        return self._sign_activity_dto

    @sign_activity_dto.setter
    def sign_activity_dto(self, value):
        if isinstance(value, SignActivityDTO):
            self._sign_activity_dto = value
        else:
            self._sign_activity_dto = SignActivityDTO.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_datetime:
            if hasattr(self.active_datetime, 'to_alipay_dict'):
                params['active_datetime'] = self.active_datetime.to_alipay_dict()
            else:
                params['active_datetime'] = self.active_datetime
        if self.inactive_datetime:
            if hasattr(self.inactive_datetime, 'to_alipay_dict'):
                params['inactive_datetime'] = self.inactive_datetime.to_alipay_dict()
            else:
                params['inactive_datetime'] = self.inactive_datetime
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_user_id:
            if hasattr(self.order_user_id, 'to_alipay_dict'):
                params['order_user_id'] = self.order_user_id.to_alipay_dict()
            else:
                params['order_user_id'] = self.order_user_id
        if self.ordered_channel:
            if hasattr(self.ordered_channel, 'to_alipay_dict'):
                params['ordered_channel'] = self.ordered_channel.to_alipay_dict()
            else:
                params['ordered_channel'] = self.ordered_channel
        if self.ordering_datetime:
            if hasattr(self.ordering_datetime, 'to_alipay_dict'):
                params['ordering_datetime'] = self.ordering_datetime.to_alipay_dict()
            else:
                params['ordering_datetime'] = self.ordering_datetime
        if self.out_merchant_id:
            if hasattr(self.out_merchant_id, 'to_alipay_dict'):
                params['out_merchant_id'] = self.out_merchant_id.to_alipay_dict()
            else:
                params['out_merchant_id'] = self.out_merchant_id
        if self.prod_name:
            if hasattr(self.prod_name, 'to_alipay_dict'):
                params['prod_name'] = self.prod_name.to_alipay_dict()
            else:
                params['prod_name'] = self.prod_name
        if self.ps_code:
            if hasattr(self.ps_code, 'to_alipay_dict'):
                params['ps_code'] = self.ps_code.to_alipay_dict()
            else:
                params['ps_code'] = self.ps_code
        if self.sign_activity_dto:
            if hasattr(self.sign_activity_dto, 'to_alipay_dict'):
                params['sign_activity_dto'] = self.sign_activity_dto.to_alipay_dict()
            else:
                params['sign_activity_dto'] = self.sign_activity_dto
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductOrderDTO()
        if 'active_datetime' in d:
            o.active_datetime = d['active_datetime']
        if 'inactive_datetime' in d:
            o.inactive_datetime = d['inactive_datetime']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_user_id' in d:
            o.order_user_id = d['order_user_id']
        if 'ordered_channel' in d:
            o.ordered_channel = d['ordered_channel']
        if 'ordering_datetime' in d:
            o.ordering_datetime = d['ordering_datetime']
        if 'out_merchant_id' in d:
            o.out_merchant_id = d['out_merchant_id']
        if 'prod_name' in d:
            o.prod_name = d['prod_name']
        if 'ps_code' in d:
            o.ps_code = d['ps_code']
        if 'sign_activity_dto' in d:
            o.sign_activity_dto = d['sign_activity_dto']
        if 'status' in d:
            o.status = d['status']
        return o


