#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetTransferDetailDTO(object):

    def __init__(self):
        self._amount = None
        self._asset_id = None
        self._biz_param = None
        self._biz_type = None
        self._cash = None
        self._count = None
        self._detail_id = None
        self._detail_tag = None
        self._gmt_create = None
        self._gmt_modified = None
        self._order_id = None
        self._status = None
        self._template_id = None
        self._trade_no = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def biz_param(self):
        return self._biz_param

    @biz_param.setter
    def biz_param(self, value):
        self._biz_param = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, value):
        self._cash = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def detail_id(self):
        return self._detail_id

    @detail_id.setter
    def detail_id(self, value):
        self._detail_id = value
    @property
    def detail_tag(self):
        return self._detail_tag

    @detail_tag.setter
    def detail_tag(self, value):
        self._detail_tag = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.biz_param:
            if hasattr(self.biz_param, 'to_alipay_dict'):
                params['biz_param'] = self.biz_param.to_alipay_dict()
            else:
                params['biz_param'] = self.biz_param
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.cash:
            if hasattr(self.cash, 'to_alipay_dict'):
                params['cash'] = self.cash.to_alipay_dict()
            else:
                params['cash'] = self.cash
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.detail_id:
            if hasattr(self.detail_id, 'to_alipay_dict'):
                params['detail_id'] = self.detail_id.to_alipay_dict()
            else:
                params['detail_id'] = self.detail_id
        if self.detail_tag:
            if hasattr(self.detail_tag, 'to_alipay_dict'):
                params['detail_tag'] = self.detail_tag.to_alipay_dict()
            else:
                params['detail_tag'] = self.detail_tag
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
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
        o = AssetTransferDetailDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'biz_param' in d:
            o.biz_param = d['biz_param']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'cash' in d:
            o.cash = d['cash']
        if 'count' in d:
            o.count = d['count']
        if 'detail_id' in d:
            o.detail_id = d['detail_id']
        if 'detail_tag' in d:
            o.detail_tag = d['detail_tag']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'status' in d:
            o.status = d['status']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


