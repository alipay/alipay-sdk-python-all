#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftTransferApplyModel(object):

    def __init__(self):
        self._channel_tenant = None
        self._id_no = None
        self._id_type = None
        self._open_id = None
        self._order_no = None
        self._price_cent = None
        self._req_msg_id = None
        self._sku_id = None

    @property
    def channel_tenant(self):
        return self._channel_tenant

    @channel_tenant.setter
    def channel_tenant(self, value):
        self._channel_tenant = value
    @property
    def id_no(self):
        return self._id_no

    @id_no.setter
    def id_no(self, value):
        self._id_no = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def price_cent(self):
        return self._price_cent

    @price_cent.setter
    def price_cent(self, value):
        self._price_cent = value
    @property
    def req_msg_id(self):
        return self._req_msg_id

    @req_msg_id.setter
    def req_msg_id(self, value):
        self._req_msg_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_tenant:
            if hasattr(self.channel_tenant, 'to_alipay_dict'):
                params['channel_tenant'] = self.channel_tenant.to_alipay_dict()
            else:
                params['channel_tenant'] = self.channel_tenant
        if self.id_no:
            if hasattr(self.id_no, 'to_alipay_dict'):
                params['id_no'] = self.id_no.to_alipay_dict()
            else:
                params['id_no'] = self.id_no
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.price_cent:
            if hasattr(self.price_cent, 'to_alipay_dict'):
                params['price_cent'] = self.price_cent.to_alipay_dict()
            else:
                params['price_cent'] = self.price_cent
        if self.req_msg_id:
            if hasattr(self.req_msg_id, 'to_alipay_dict'):
                params['req_msg_id'] = self.req_msg_id.to_alipay_dict()
            else:
                params['req_msg_id'] = self.req_msg_id
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftTransferApplyModel()
        if 'channel_tenant' in d:
            o.channel_tenant = d['channel_tenant']
        if 'id_no' in d:
            o.id_no = d['id_no']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'price_cent' in d:
            o.price_cent = d['price_cent']
        if 'req_msg_id' in d:
            o.req_msg_id = d['req_msg_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


