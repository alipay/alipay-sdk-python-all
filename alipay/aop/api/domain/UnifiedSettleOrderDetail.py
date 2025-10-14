#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnifiedSettleOrderDetail(object):

    def __init__(self):
        self._amount = None
        self._biz_scene = None
        self._external_inst_biz_date = None
        self._external_inst_create_date = None
        self._gmt_create = None
        self._inst_order_id = None
        self._order_id = None
        self._order_sync_id = None
        self._out_request_no = None
        self._out_trade_no = None
        self._request_type = None
        self._status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def external_inst_biz_date(self):
        return self._external_inst_biz_date

    @external_inst_biz_date.setter
    def external_inst_biz_date(self, value):
        self._external_inst_biz_date = value
    @property
    def external_inst_create_date(self):
        return self._external_inst_create_date

    @external_inst_create_date.setter
    def external_inst_create_date(self, value):
        self._external_inst_create_date = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def inst_order_id(self):
        return self._inst_order_id

    @inst_order_id.setter
    def inst_order_id(self, value):
        self._inst_order_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_sync_id(self):
        return self._order_sync_id

    @order_sync_id.setter
    def order_sync_id(self, value):
        self._order_sync_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def request_type(self):
        return self._request_type

    @request_type.setter
    def request_type(self, value):
        self._request_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.external_inst_biz_date:
            if hasattr(self.external_inst_biz_date, 'to_alipay_dict'):
                params['external_inst_biz_date'] = self.external_inst_biz_date.to_alipay_dict()
            else:
                params['external_inst_biz_date'] = self.external_inst_biz_date
        if self.external_inst_create_date:
            if hasattr(self.external_inst_create_date, 'to_alipay_dict'):
                params['external_inst_create_date'] = self.external_inst_create_date.to_alipay_dict()
            else:
                params['external_inst_create_date'] = self.external_inst_create_date
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.inst_order_id:
            if hasattr(self.inst_order_id, 'to_alipay_dict'):
                params['inst_order_id'] = self.inst_order_id.to_alipay_dict()
            else:
                params['inst_order_id'] = self.inst_order_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_sync_id:
            if hasattr(self.order_sync_id, 'to_alipay_dict'):
                params['order_sync_id'] = self.order_sync_id.to_alipay_dict()
            else:
                params['order_sync_id'] = self.order_sync_id
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.request_type:
            if hasattr(self.request_type, 'to_alipay_dict'):
                params['request_type'] = self.request_type.to_alipay_dict()
            else:
                params['request_type'] = self.request_type
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
        o = UnifiedSettleOrderDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'external_inst_biz_date' in d:
            o.external_inst_biz_date = d['external_inst_biz_date']
        if 'external_inst_create_date' in d:
            o.external_inst_create_date = d['external_inst_create_date']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'inst_order_id' in d:
            o.inst_order_id = d['inst_order_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_sync_id' in d:
            o.order_sync_id = d['order_sync_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'request_type' in d:
            o.request_type = d['request_type']
        if 'status' in d:
            o.status = d['status']
        return o


