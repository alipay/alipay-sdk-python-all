#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnifiedSettleTradeInstOrderInfo(object):

    def __init__(self):
        self._amount = None
        self._biz_memo = None
        self._gmt_create = None
        self._gmt_modified = None
        self._inst_serial_no = None
        self._order_id = None
        self._payer_card_name = None
        self._payer_card_no = None
        self._payer_inst_id = None
        self._status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_memo(self):
        return self._biz_memo

    @biz_memo.setter
    def biz_memo(self, value):
        self._biz_memo = value
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
    def inst_serial_no(self):
        return self._inst_serial_no

    @inst_serial_no.setter
    def inst_serial_no(self, value):
        self._inst_serial_no = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def payer_card_name(self):
        return self._payer_card_name

    @payer_card_name.setter
    def payer_card_name(self, value):
        self._payer_card_name = value
    @property
    def payer_card_no(self):
        return self._payer_card_no

    @payer_card_no.setter
    def payer_card_no(self, value):
        self._payer_card_no = value
    @property
    def payer_inst_id(self):
        return self._payer_inst_id

    @payer_inst_id.setter
    def payer_inst_id(self, value):
        self._payer_inst_id = value
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
        if self.biz_memo:
            if hasattr(self.biz_memo, 'to_alipay_dict'):
                params['biz_memo'] = self.biz_memo.to_alipay_dict()
            else:
                params['biz_memo'] = self.biz_memo
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
        if self.inst_serial_no:
            if hasattr(self.inst_serial_no, 'to_alipay_dict'):
                params['inst_serial_no'] = self.inst_serial_no.to_alipay_dict()
            else:
                params['inst_serial_no'] = self.inst_serial_no
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.payer_card_name:
            if hasattr(self.payer_card_name, 'to_alipay_dict'):
                params['payer_card_name'] = self.payer_card_name.to_alipay_dict()
            else:
                params['payer_card_name'] = self.payer_card_name
        if self.payer_card_no:
            if hasattr(self.payer_card_no, 'to_alipay_dict'):
                params['payer_card_no'] = self.payer_card_no.to_alipay_dict()
            else:
                params['payer_card_no'] = self.payer_card_no
        if self.payer_inst_id:
            if hasattr(self.payer_inst_id, 'to_alipay_dict'):
                params['payer_inst_id'] = self.payer_inst_id.to_alipay_dict()
            else:
                params['payer_inst_id'] = self.payer_inst_id
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
        o = UnifiedSettleTradeInstOrderInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_memo' in d:
            o.biz_memo = d['biz_memo']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'inst_serial_no' in d:
            o.inst_serial_no = d['inst_serial_no']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'payer_card_name' in d:
            o.payer_card_name = d['payer_card_name']
        if 'payer_card_no' in d:
            o.payer_card_no = d['payer_card_no']
        if 'payer_inst_id' in d:
            o.payer_inst_id = d['payer_inst_id']
        if 'status' in d:
            o.status = d['status']
        return o


