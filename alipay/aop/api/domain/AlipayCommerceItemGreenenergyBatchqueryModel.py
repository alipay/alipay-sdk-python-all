#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BelongGreenMerchantInfo import BelongGreenMerchantInfo
from alipay.aop.api.domain.GreenPaginator import GreenPaginator


class AlipayCommerceItemGreenenergyBatchqueryModel(object):

    def __init__(self):
        self._alipay_open_id = None
        self._alipay_uid = None
        self._belong_merchant_info = None
        self._energy_status = None
        self._paginator = None

    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_uid(self):
        return self._alipay_uid

    @alipay_uid.setter
    def alipay_uid(self, value):
        self._alipay_uid = value
    @property
    def belong_merchant_info(self):
        return self._belong_merchant_info

    @belong_merchant_info.setter
    def belong_merchant_info(self, value):
        if isinstance(value, BelongGreenMerchantInfo):
            self._belong_merchant_info = value
        else:
            self._belong_merchant_info = BelongGreenMerchantInfo.from_alipay_dict(value)
    @property
    def energy_status(self):
        return self._energy_status

    @energy_status.setter
    def energy_status(self, value):
        self._energy_status = value
    @property
    def paginator(self):
        return self._paginator

    @paginator.setter
    def paginator(self, value):
        if isinstance(value, GreenPaginator):
            self._paginator = value
        else:
            self._paginator = GreenPaginator.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_uid:
            if hasattr(self.alipay_uid, 'to_alipay_dict'):
                params['alipay_uid'] = self.alipay_uid.to_alipay_dict()
            else:
                params['alipay_uid'] = self.alipay_uid
        if self.belong_merchant_info:
            if hasattr(self.belong_merchant_info, 'to_alipay_dict'):
                params['belong_merchant_info'] = self.belong_merchant_info.to_alipay_dict()
            else:
                params['belong_merchant_info'] = self.belong_merchant_info
        if self.energy_status:
            if hasattr(self.energy_status, 'to_alipay_dict'):
                params['energy_status'] = self.energy_status.to_alipay_dict()
            else:
                params['energy_status'] = self.energy_status
        if self.paginator:
            if hasattr(self.paginator, 'to_alipay_dict'):
                params['paginator'] = self.paginator.to_alipay_dict()
            else:
                params['paginator'] = self.paginator
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceItemGreenenergyBatchqueryModel()
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_uid' in d:
            o.alipay_uid = d['alipay_uid']
        if 'belong_merchant_info' in d:
            o.belong_merchant_info = d['belong_merchant_info']
        if 'energy_status' in d:
            o.energy_status = d['energy_status']
        if 'paginator' in d:
            o.paginator = d['paginator']
        return o


