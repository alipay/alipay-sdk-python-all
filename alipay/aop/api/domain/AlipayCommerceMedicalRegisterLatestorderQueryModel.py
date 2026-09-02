#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalRegisterLatestorderQueryModel(object):

    def __init__(self):
        self._channel = None
        self._open_id = None
        self._order_id = None
        self._order_prop = None
        self._page_no = None
        self._page_size = None
        self._select_hos_institution_code = None
        self._select_hos_uniq_code = None
        self._status = None
        self._user_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
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
    def order_prop(self):
        return self._order_prop

    @order_prop.setter
    def order_prop(self, value):
        self._order_prop = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def select_hos_institution_code(self):
        return self._select_hos_institution_code

    @select_hos_institution_code.setter
    def select_hos_institution_code(self, value):
        self._select_hos_institution_code = value
    @property
    def select_hos_uniq_code(self):
        return self._select_hos_uniq_code

    @select_hos_uniq_code.setter
    def select_hos_uniq_code(self, value):
        self._select_hos_uniq_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if isinstance(value, list):
            self._status = list()
            for i in value:
                self._status.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
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
        if self.order_prop:
            if hasattr(self.order_prop, 'to_alipay_dict'):
                params['order_prop'] = self.order_prop.to_alipay_dict()
            else:
                params['order_prop'] = self.order_prop
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.select_hos_institution_code:
            if hasattr(self.select_hos_institution_code, 'to_alipay_dict'):
                params['select_hos_institution_code'] = self.select_hos_institution_code.to_alipay_dict()
            else:
                params['select_hos_institution_code'] = self.select_hos_institution_code
        if self.select_hos_uniq_code:
            if hasattr(self.select_hos_uniq_code, 'to_alipay_dict'):
                params['select_hos_uniq_code'] = self.select_hos_uniq_code.to_alipay_dict()
            else:
                params['select_hos_uniq_code'] = self.select_hos_uniq_code
        if self.status:
            if isinstance(self.status, list):
                for i in range(0, len(self.status)):
                    element = self.status[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status[i] = element.to_alipay_dict()
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AlipayCommerceMedicalRegisterLatestorderQueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_prop' in d:
            o.order_prop = d['order_prop']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'select_hos_institution_code' in d:
            o.select_hos_institution_code = d['select_hos_institution_code']
        if 'select_hos_uniq_code' in d:
            o.select_hos_uniq_code = d['select_hos_uniq_code']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


