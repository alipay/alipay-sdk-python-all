#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOfflinelaborInsuranceQueryModel(object):

    def __init__(self):
        self._channel_user_id = None
        self._channel_user_source = None
        self._mode = None
        self._open_id = None
        self._page_no = None
        self._page_size = None
        self._product_list = None
        self._status = None
        self._type = None

    @property
    def channel_user_id(self):
        return self._channel_user_id

    @channel_user_id.setter
    def channel_user_id(self, value):
        self._channel_user_id = value
    @property
    def channel_user_source(self):
        return self._channel_user_source

    @channel_user_source.setter
    def channel_user_source(self, value):
        self._channel_user_source = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    def product_list(self):
        return self._product_list

    @product_list.setter
    def product_list(self, value):
        if isinstance(value, list):
            self._product_list = list()
            for i in value:
                self._product_list.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_user_id:
            if hasattr(self.channel_user_id, 'to_alipay_dict'):
                params['channel_user_id'] = self.channel_user_id.to_alipay_dict()
            else:
                params['channel_user_id'] = self.channel_user_id
        if self.channel_user_source:
            if hasattr(self.channel_user_source, 'to_alipay_dict'):
                params['channel_user_source'] = self.channel_user_source.to_alipay_dict()
            else:
                params['channel_user_source'] = self.channel_user_source
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        if self.product_list:
            if isinstance(self.product_list, list):
                for i in range(0, len(self.product_list)):
                    element = self.product_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_list[i] = element.to_alipay_dict()
            if hasattr(self.product_list, 'to_alipay_dict'):
                params['product_list'] = self.product_list.to_alipay_dict()
            else:
                params['product_list'] = self.product_list
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOfflinelaborInsuranceQueryModel()
        if 'channel_user_id' in d:
            o.channel_user_id = d['channel_user_id']
        if 'channel_user_source' in d:
            o.channel_user_source = d['channel_user_source']
        if 'mode' in d:
            o.mode = d['mode']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'product_list' in d:
            o.product_list = d['product_list']
        if 'status' in d:
            o.status = d['status']
        if 'type' in d:
            o.type = d['type']
        return o


