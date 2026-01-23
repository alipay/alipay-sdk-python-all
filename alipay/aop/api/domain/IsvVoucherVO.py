#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IsvVoucherVO(object):

    def __init__(self):
        self._available_cash = None
        self._available_count = None
        self._freeze_amount = None
        self._freeze_cash = None
        self._gmt_active = None
        self._gmt_expired = None
        self._gmt_extend = None
        self._name = None
        self._recycle_amount = None
        self._redirect_url = None
        self._status = None
        self._total_amount = None
        self._total_cash = None
        self._total_count = None
        self._transfer_amount = None
        self._used_count = None
        self._voucher_description = None
        self._voucher_id = None

    @property
    def available_cash(self):
        return self._available_cash

    @available_cash.setter
    def available_cash(self, value):
        self._available_cash = value
    @property
    def available_count(self):
        return self._available_count

    @available_count.setter
    def available_count(self, value):
        self._available_count = value
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def freeze_cash(self):
        return self._freeze_cash

    @freeze_cash.setter
    def freeze_cash(self, value):
        self._freeze_cash = value
    @property
    def gmt_active(self):
        return self._gmt_active

    @gmt_active.setter
    def gmt_active(self, value):
        self._gmt_active = value
    @property
    def gmt_expired(self):
        return self._gmt_expired

    @gmt_expired.setter
    def gmt_expired(self, value):
        self._gmt_expired = value
    @property
    def gmt_extend(self):
        return self._gmt_extend

    @gmt_extend.setter
    def gmt_extend(self, value):
        self._gmt_extend = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def recycle_amount(self):
        return self._recycle_amount

    @recycle_amount.setter
    def recycle_amount(self, value):
        self._recycle_amount = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_cash(self):
        return self._total_cash

    @total_cash.setter
    def total_cash(self, value):
        self._total_cash = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def transfer_amount(self):
        return self._transfer_amount

    @transfer_amount.setter
    def transfer_amount(self, value):
        self._transfer_amount = value
    @property
    def used_count(self):
        return self._used_count

    @used_count.setter
    def used_count(self, value):
        self._used_count = value
    @property
    def voucher_description(self):
        return self._voucher_description

    @voucher_description.setter
    def voucher_description(self, value):
        self._voucher_description = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_cash:
            if hasattr(self.available_cash, 'to_alipay_dict'):
                params['available_cash'] = self.available_cash.to_alipay_dict()
            else:
                params['available_cash'] = self.available_cash
        if self.available_count:
            if hasattr(self.available_count, 'to_alipay_dict'):
                params['available_count'] = self.available_count.to_alipay_dict()
            else:
                params['available_count'] = self.available_count
        if self.freeze_amount:
            if hasattr(self.freeze_amount, 'to_alipay_dict'):
                params['freeze_amount'] = self.freeze_amount.to_alipay_dict()
            else:
                params['freeze_amount'] = self.freeze_amount
        if self.freeze_cash:
            if hasattr(self.freeze_cash, 'to_alipay_dict'):
                params['freeze_cash'] = self.freeze_cash.to_alipay_dict()
            else:
                params['freeze_cash'] = self.freeze_cash
        if self.gmt_active:
            if hasattr(self.gmt_active, 'to_alipay_dict'):
                params['gmt_active'] = self.gmt_active.to_alipay_dict()
            else:
                params['gmt_active'] = self.gmt_active
        if self.gmt_expired:
            if hasattr(self.gmt_expired, 'to_alipay_dict'):
                params['gmt_expired'] = self.gmt_expired.to_alipay_dict()
            else:
                params['gmt_expired'] = self.gmt_expired
        if self.gmt_extend:
            if hasattr(self.gmt_extend, 'to_alipay_dict'):
                params['gmt_extend'] = self.gmt_extend.to_alipay_dict()
            else:
                params['gmt_extend'] = self.gmt_extend
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.recycle_amount:
            if hasattr(self.recycle_amount, 'to_alipay_dict'):
                params['recycle_amount'] = self.recycle_amount.to_alipay_dict()
            else:
                params['recycle_amount'] = self.recycle_amount
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.total_cash:
            if hasattr(self.total_cash, 'to_alipay_dict'):
                params['total_cash'] = self.total_cash.to_alipay_dict()
            else:
                params['total_cash'] = self.total_cash
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        if self.transfer_amount:
            if hasattr(self.transfer_amount, 'to_alipay_dict'):
                params['transfer_amount'] = self.transfer_amount.to_alipay_dict()
            else:
                params['transfer_amount'] = self.transfer_amount
        if self.used_count:
            if hasattr(self.used_count, 'to_alipay_dict'):
                params['used_count'] = self.used_count.to_alipay_dict()
            else:
                params['used_count'] = self.used_count
        if self.voucher_description:
            if hasattr(self.voucher_description, 'to_alipay_dict'):
                params['voucher_description'] = self.voucher_description.to_alipay_dict()
            else:
                params['voucher_description'] = self.voucher_description
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
        o = IsvVoucherVO()
        if 'available_cash' in d:
            o.available_cash = d['available_cash']
        if 'available_count' in d:
            o.available_count = d['available_count']
        if 'freeze_amount' in d:
            o.freeze_amount = d['freeze_amount']
        if 'freeze_cash' in d:
            o.freeze_cash = d['freeze_cash']
        if 'gmt_active' in d:
            o.gmt_active = d['gmt_active']
        if 'gmt_expired' in d:
            o.gmt_expired = d['gmt_expired']
        if 'gmt_extend' in d:
            o.gmt_extend = d['gmt_extend']
        if 'name' in d:
            o.name = d['name']
        if 'recycle_amount' in d:
            o.recycle_amount = d['recycle_amount']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        if 'status' in d:
            o.status = d['status']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'total_cash' in d:
            o.total_cash = d['total_cash']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'transfer_amount' in d:
            o.transfer_amount = d['transfer_amount']
        if 'used_count' in d:
            o.used_count = d['used_count']
        if 'voucher_description' in d:
            o.voucher_description = d['voucher_description']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


