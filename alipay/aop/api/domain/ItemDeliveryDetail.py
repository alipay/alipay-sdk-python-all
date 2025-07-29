#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetItemVersion import AssetItemVersion
from alipay.aop.api.domain.OptionalItemInfo import OptionalItemInfo


class ItemDeliveryDetail(object):

    def __init__(self):
        self._amount = None
        self._assign_item_id = None
        self._batch_no = None
        self._item_version_info = None
        self._logistic_code = None
        self._logistics_name = None
        self._logistics_no = None
        self._optional_item_infos = None
        self._voucher_time = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def assign_item_id(self):
        return self._assign_item_id

    @assign_item_id.setter
    def assign_item_id(self, value):
        self._assign_item_id = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def item_version_info(self):
        return self._item_version_info

    @item_version_info.setter
    def item_version_info(self, value):
        if isinstance(value, AssetItemVersion):
            self._item_version_info = value
        else:
            self._item_version_info = AssetItemVersion.from_alipay_dict(value)
    @property
    def logistic_code(self):
        return self._logistic_code

    @logistic_code.setter
    def logistic_code(self, value):
        self._logistic_code = value
    @property
    def logistics_name(self):
        return self._logistics_name

    @logistics_name.setter
    def logistics_name(self, value):
        self._logistics_name = value
    @property
    def logistics_no(self):
        return self._logistics_no

    @logistics_no.setter
    def logistics_no(self, value):
        self._logistics_no = value
    @property
    def optional_item_infos(self):
        return self._optional_item_infos

    @optional_item_infos.setter
    def optional_item_infos(self, value):
        if isinstance(value, list):
            self._optional_item_infos = list()
            for i in value:
                if isinstance(i, OptionalItemInfo):
                    self._optional_item_infos.append(i)
                else:
                    self._optional_item_infos.append(OptionalItemInfo.from_alipay_dict(i))
    @property
    def voucher_time(self):
        return self._voucher_time

    @voucher_time.setter
    def voucher_time(self, value):
        self._voucher_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.assign_item_id:
            if hasattr(self.assign_item_id, 'to_alipay_dict'):
                params['assign_item_id'] = self.assign_item_id.to_alipay_dict()
            else:
                params['assign_item_id'] = self.assign_item_id
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.item_version_info:
            if hasattr(self.item_version_info, 'to_alipay_dict'):
                params['item_version_info'] = self.item_version_info.to_alipay_dict()
            else:
                params['item_version_info'] = self.item_version_info
        if self.logistic_code:
            if hasattr(self.logistic_code, 'to_alipay_dict'):
                params['logistic_code'] = self.logistic_code.to_alipay_dict()
            else:
                params['logistic_code'] = self.logistic_code
        if self.logistics_name:
            if hasattr(self.logistics_name, 'to_alipay_dict'):
                params['logistics_name'] = self.logistics_name.to_alipay_dict()
            else:
                params['logistics_name'] = self.logistics_name
        if self.logistics_no:
            if hasattr(self.logistics_no, 'to_alipay_dict'):
                params['logistics_no'] = self.logistics_no.to_alipay_dict()
            else:
                params['logistics_no'] = self.logistics_no
        if self.optional_item_infos:
            if isinstance(self.optional_item_infos, list):
                for i in range(0, len(self.optional_item_infos)):
                    element = self.optional_item_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.optional_item_infos[i] = element.to_alipay_dict()
            if hasattr(self.optional_item_infos, 'to_alipay_dict'):
                params['optional_item_infos'] = self.optional_item_infos.to_alipay_dict()
            else:
                params['optional_item_infos'] = self.optional_item_infos
        if self.voucher_time:
            if hasattr(self.voucher_time, 'to_alipay_dict'):
                params['voucher_time'] = self.voucher_time.to_alipay_dict()
            else:
                params['voucher_time'] = self.voucher_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemDeliveryDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'assign_item_id' in d:
            o.assign_item_id = d['assign_item_id']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'item_version_info' in d:
            o.item_version_info = d['item_version_info']
        if 'logistic_code' in d:
            o.logistic_code = d['logistic_code']
        if 'logistics_name' in d:
            o.logistics_name = d['logistics_name']
        if 'logistics_no' in d:
            o.logistics_no = d['logistics_no']
        if 'optional_item_infos' in d:
            o.optional_item_infos = d['optional_item_infos']
        if 'voucher_time' in d:
            o.voucher_time = d['voucher_time']
        return o


