#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbOrderVoucherModel(object):

    def __init__(self):
        self._expire_date = None
        self._funds_voucher_no = None
        self._item_id = None
        self._refund_reason = None
        self._refund_type = None
        self._shop_id = None
        self._status = None
        self._store_id = None
        self._ticket_effect_count = None
        self._ticket_refunded_count = None
        self._ticket_used_count = None
        self._voucher_id = None

    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def funds_voucher_no(self):
        return self._funds_voucher_no

    @funds_voucher_no.setter
    def funds_voucher_no(self, value):
        self._funds_voucher_no = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def refund_type(self):
        return self._refund_type

    @refund_type.setter
    def refund_type(self, value):
        self._refund_type = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def ticket_effect_count(self):
        return self._ticket_effect_count

    @ticket_effect_count.setter
    def ticket_effect_count(self, value):
        self._ticket_effect_count = value
    @property
    def ticket_refunded_count(self):
        return self._ticket_refunded_count

    @ticket_refunded_count.setter
    def ticket_refunded_count(self, value):
        self._ticket_refunded_count = value
    @property
    def ticket_used_count(self):
        return self._ticket_used_count

    @ticket_used_count.setter
    def ticket_used_count(self, value):
        self._ticket_used_count = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.funds_voucher_no:
            if hasattr(self.funds_voucher_no, 'to_alipay_dict'):
                params['funds_voucher_no'] = self.funds_voucher_no.to_alipay_dict()
            else:
                params['funds_voucher_no'] = self.funds_voucher_no
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.refund_type:
            if hasattr(self.refund_type, 'to_alipay_dict'):
                params['refund_type'] = self.refund_type.to_alipay_dict()
            else:
                params['refund_type'] = self.refund_type
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.ticket_effect_count:
            if hasattr(self.ticket_effect_count, 'to_alipay_dict'):
                params['ticket_effect_count'] = self.ticket_effect_count.to_alipay_dict()
            else:
                params['ticket_effect_count'] = self.ticket_effect_count
        if self.ticket_refunded_count:
            if hasattr(self.ticket_refunded_count, 'to_alipay_dict'):
                params['ticket_refunded_count'] = self.ticket_refunded_count.to_alipay_dict()
            else:
                params['ticket_refunded_count'] = self.ticket_refunded_count
        if self.ticket_used_count:
            if hasattr(self.ticket_used_count, 'to_alipay_dict'):
                params['ticket_used_count'] = self.ticket_used_count.to_alipay_dict()
            else:
                params['ticket_used_count'] = self.ticket_used_count
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbOrderVoucherModel()
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'funds_voucher_no' in d:
            o.funds_voucher_no = d['funds_voucher_no']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'refund_type' in d:
            o.refund_type = d['refund_type']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'ticket_effect_count' in d:
            o.ticket_effect_count = d['ticket_effect_count']
        if 'ticket_refunded_count' in d:
            o.ticket_refunded_count = d['ticket_refunded_count']
        if 'ticket_used_count' in d:
            o.ticket_used_count = d['ticket_used_count']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


