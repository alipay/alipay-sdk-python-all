#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduTradeExtInfo import EduTradeExtInfo


class AlipayCommerceEducateTradeCreateModel(object):

    def __init__(self):
        self._count = None
        self._ext_info = None
        self._gmt_create = None
        self._gmt_expired = None
        self._gmt_modified = None
        self._gmt_paytime = None
        self._good_id = None
        self._isv_order_no = None
        self._pay_amount = None
        self._shop_id = None
        self._smid = None
        self._source = None
        self._title = None
        self._total_amount = None
        self._trade_no = None
        self._trade_status = None
        self._trans_currency = None
        self._user_id = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, EduTradeExtInfo):
            self._ext_info = value
        else:
            self._ext_info = EduTradeExtInfo.from_alipay_dict(value)
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_expired(self):
        return self._gmt_expired

    @gmt_expired.setter
    def gmt_expired(self, value):
        self._gmt_expired = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def gmt_paytime(self):
        return self._gmt_paytime

    @gmt_paytime.setter
    def gmt_paytime(self, value):
        self._gmt_paytime = value
    @property
    def good_id(self):
        return self._good_id

    @good_id.setter
    def good_id(self, value):
        self._good_id = value
    @property
    def isv_order_no(self):
        return self._isv_order_no

    @isv_order_no.setter
    def isv_order_no(self, value):
        self._isv_order_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value
    @property
    def trans_currency(self):
        return self._trans_currency

    @trans_currency.setter
    def trans_currency(self, value):
        self._trans_currency = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_expired:
            if hasattr(self.gmt_expired, 'to_alipay_dict'):
                params['gmt_expired'] = self.gmt_expired.to_alipay_dict()
            else:
                params['gmt_expired'] = self.gmt_expired
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.gmt_paytime:
            if hasattr(self.gmt_paytime, 'to_alipay_dict'):
                params['gmt_paytime'] = self.gmt_paytime.to_alipay_dict()
            else:
                params['gmt_paytime'] = self.gmt_paytime
        if self.good_id:
            if hasattr(self.good_id, 'to_alipay_dict'):
                params['good_id'] = self.good_id.to_alipay_dict()
            else:
                params['good_id'] = self.good_id
        if self.isv_order_no:
            if hasattr(self.isv_order_no, 'to_alipay_dict'):
                params['isv_order_no'] = self.isv_order_no.to_alipay_dict()
            else:
                params['isv_order_no'] = self.isv_order_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_status:
            if hasattr(self.trade_status, 'to_alipay_dict'):
                params['trade_status'] = self.trade_status.to_alipay_dict()
            else:
                params['trade_status'] = self.trade_status
        if self.trans_currency:
            if hasattr(self.trans_currency, 'to_alipay_dict'):
                params['trans_currency'] = self.trans_currency.to_alipay_dict()
            else:
                params['trans_currency'] = self.trans_currency
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
        o = AlipayCommerceEducateTradeCreateModel()
        if 'count' in d:
            o.count = d['count']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_expired' in d:
            o.gmt_expired = d['gmt_expired']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'gmt_paytime' in d:
            o.gmt_paytime = d['gmt_paytime']
        if 'good_id' in d:
            o.good_id = d['good_id']
        if 'isv_order_no' in d:
            o.isv_order_no = d['isv_order_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'smid' in d:
            o.smid = d['smid']
        if 'source' in d:
            o.source = d['source']
        if 'title' in d:
            o.title = d['title']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_status' in d:
            o.trade_status = d['trade_status']
        if 'trans_currency' in d:
            o.trans_currency = d['trans_currency']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


