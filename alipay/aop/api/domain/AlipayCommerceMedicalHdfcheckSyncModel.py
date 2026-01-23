#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SyncStatusItemInfo import SyncStatusItemInfo


class AlipayCommerceMedicalHdfcheckSyncModel(object):

    def __init__(self):
        self._biz_source = None
        self._cancel_reason = None
        self._cancel_time = None
        self._hdf_apply_no = None
        self._item_info_list = None
        self._order_price = None
        self._union_apply_no = None
        self._union_apply_pay_status = None

    @property
    def biz_source(self):
        return self._biz_source

    @biz_source.setter
    def biz_source(self, value):
        self._biz_source = value
    @property
    def cancel_reason(self):
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, value):
        self._cancel_reason = value
    @property
    def cancel_time(self):
        return self._cancel_time

    @cancel_time.setter
    def cancel_time(self, value):
        self._cancel_time = value
    @property
    def hdf_apply_no(self):
        return self._hdf_apply_no

    @hdf_apply_no.setter
    def hdf_apply_no(self, value):
        self._hdf_apply_no = value
    @property
    def item_info_list(self):
        return self._item_info_list

    @item_info_list.setter
    def item_info_list(self, value):
        if isinstance(value, list):
            self._item_info_list = list()
            for i in value:
                if isinstance(i, SyncStatusItemInfo):
                    self._item_info_list.append(i)
                else:
                    self._item_info_list.append(SyncStatusItemInfo.from_alipay_dict(i))
    @property
    def order_price(self):
        return self._order_price

    @order_price.setter
    def order_price(self, value):
        self._order_price = value
    @property
    def union_apply_no(self):
        return self._union_apply_no

    @union_apply_no.setter
    def union_apply_no(self, value):
        self._union_apply_no = value
    @property
    def union_apply_pay_status(self):
        return self._union_apply_pay_status

    @union_apply_pay_status.setter
    def union_apply_pay_status(self, value):
        self._union_apply_pay_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_source:
            if hasattr(self.biz_source, 'to_alipay_dict'):
                params['biz_source'] = self.biz_source.to_alipay_dict()
            else:
                params['biz_source'] = self.biz_source
        if self.cancel_reason:
            if hasattr(self.cancel_reason, 'to_alipay_dict'):
                params['cancel_reason'] = self.cancel_reason.to_alipay_dict()
            else:
                params['cancel_reason'] = self.cancel_reason
        if self.cancel_time:
            if hasattr(self.cancel_time, 'to_alipay_dict'):
                params['cancel_time'] = self.cancel_time.to_alipay_dict()
            else:
                params['cancel_time'] = self.cancel_time
        if self.hdf_apply_no:
            if hasattr(self.hdf_apply_no, 'to_alipay_dict'):
                params['hdf_apply_no'] = self.hdf_apply_no.to_alipay_dict()
            else:
                params['hdf_apply_no'] = self.hdf_apply_no
        if self.item_info_list:
            if isinstance(self.item_info_list, list):
                for i in range(0, len(self.item_info_list)):
                    element = self.item_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_info_list[i] = element.to_alipay_dict()
            if hasattr(self.item_info_list, 'to_alipay_dict'):
                params['item_info_list'] = self.item_info_list.to_alipay_dict()
            else:
                params['item_info_list'] = self.item_info_list
        if self.order_price:
            if hasattr(self.order_price, 'to_alipay_dict'):
                params['order_price'] = self.order_price.to_alipay_dict()
            else:
                params['order_price'] = self.order_price
        if self.union_apply_no:
            if hasattr(self.union_apply_no, 'to_alipay_dict'):
                params['union_apply_no'] = self.union_apply_no.to_alipay_dict()
            else:
                params['union_apply_no'] = self.union_apply_no
        if self.union_apply_pay_status:
            if hasattr(self.union_apply_pay_status, 'to_alipay_dict'):
                params['union_apply_pay_status'] = self.union_apply_pay_status.to_alipay_dict()
            else:
                params['union_apply_pay_status'] = self.union_apply_pay_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfcheckSyncModel()
        if 'biz_source' in d:
            o.biz_source = d['biz_source']
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'cancel_time' in d:
            o.cancel_time = d['cancel_time']
        if 'hdf_apply_no' in d:
            o.hdf_apply_no = d['hdf_apply_no']
        if 'item_info_list' in d:
            o.item_info_list = d['item_info_list']
        if 'order_price' in d:
            o.order_price = d['order_price']
        if 'union_apply_no' in d:
            o.union_apply_no = d['union_apply_no']
        if 'union_apply_pay_status' in d:
            o.union_apply_pay_status = d['union_apply_pay_status']
        return o


