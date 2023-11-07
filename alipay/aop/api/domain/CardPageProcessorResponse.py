#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardPageProcessorResponse(object):

    def __init__(self):
        self._cancel_type = None
        self._card_type = None
        self._create_date = None
        self._id = None
        self._login_id = None
        self._merchant_name = None
        self._name = None
        self._open_id = None
        self._order_id = None
        self._remain_count = None
        self._spc_template_id = None
        self._status = None
        self._total_count = None
        self._user_id = None

    @property
    def cancel_type(self):
        return self._cancel_type

    @cancel_type.setter
    def cancel_type(self, value):
        self._cancel_type = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
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
    def remain_count(self):
        return self._remain_count

    @remain_count.setter
    def remain_count(self, value):
        self._remain_count = value
    @property
    def spc_template_id(self):
        return self._spc_template_id

    @spc_template_id.setter
    def spc_template_id(self, value):
        self._spc_template_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_type:
            if hasattr(self.cancel_type, 'to_alipay_dict'):
                params['cancel_type'] = self.cancel_type.to_alipay_dict()
            else:
                params['cancel_type'] = self.cancel_type
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.create_date:
            if hasattr(self.create_date, 'to_alipay_dict'):
                params['create_date'] = self.create_date.to_alipay_dict()
            else:
                params['create_date'] = self.create_date
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        if self.remain_count:
            if hasattr(self.remain_count, 'to_alipay_dict'):
                params['remain_count'] = self.remain_count.to_alipay_dict()
            else:
                params['remain_count'] = self.remain_count
        if self.spc_template_id:
            if hasattr(self.spc_template_id, 'to_alipay_dict'):
                params['spc_template_id'] = self.spc_template_id.to_alipay_dict()
            else:
                params['spc_template_id'] = self.spc_template_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
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
        o = CardPageProcessorResponse()
        if 'cancel_type' in d:
            o.cancel_type = d['cancel_type']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'create_date' in d:
            o.create_date = d['create_date']
        if 'id' in d:
            o.id = d['id']
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'name' in d:
            o.name = d['name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'remain_count' in d:
            o.remain_count = d['remain_count']
        if 'spc_template_id' in d:
            o.spc_template_id = d['spc_template_id']
        if 'status' in d:
            o.status = d['status']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


