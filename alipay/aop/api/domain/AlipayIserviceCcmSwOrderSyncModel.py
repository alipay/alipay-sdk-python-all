#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LogisticInfo import LogisticInfo
from alipay.aop.api.domain.SpuInfo import SpuInfo


class AlipayIserviceCcmSwOrderSyncModel(object):

    def __init__(self):
        self._amount = None
        self._link_url = None
        self._logistic_count = None
        self._logistics = None
        self._order_create_time = None
        self._order_id = None
        self._order_type = None
        self._spu_count = None
        self._spus = None
        self._status = None
        self._sub_status = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def link_url(self):
        return self._link_url

    @link_url.setter
    def link_url(self, value):
        self._link_url = value
    @property
    def logistic_count(self):
        return self._logistic_count

    @logistic_count.setter
    def logistic_count(self, value):
        self._logistic_count = value
    @property
    def logistics(self):
        return self._logistics

    @logistics.setter
    def logistics(self, value):
        if isinstance(value, list):
            self._logistics = list()
            for i in value:
                if isinstance(i, LogisticInfo):
                    self._logistics.append(i)
                else:
                    self._logistics.append(LogisticInfo.from_alipay_dict(i))
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def spu_count(self):
        return self._spu_count

    @spu_count.setter
    def spu_count(self, value):
        self._spu_count = value
    @property
    def spus(self):
        return self._spus

    @spus.setter
    def spus(self, value):
        if isinstance(value, list):
            self._spus = list()
            for i in value:
                if isinstance(i, SpuInfo):
                    self._spus.append(i)
                else:
                    self._spus.append(SpuInfo.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_status(self):
        return self._sub_status

    @sub_status.setter
    def sub_status(self, value):
        self._sub_status = value
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
        if self.link_url:
            if hasattr(self.link_url, 'to_alipay_dict'):
                params['link_url'] = self.link_url.to_alipay_dict()
            else:
                params['link_url'] = self.link_url
        if self.logistic_count:
            if hasattr(self.logistic_count, 'to_alipay_dict'):
                params['logistic_count'] = self.logistic_count.to_alipay_dict()
            else:
                params['logistic_count'] = self.logistic_count
        if self.logistics:
            if isinstance(self.logistics, list):
                for i in range(0, len(self.logistics)):
                    element = self.logistics[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logistics[i] = element.to_alipay_dict()
            if hasattr(self.logistics, 'to_alipay_dict'):
                params['logistics'] = self.logistics.to_alipay_dict()
            else:
                params['logistics'] = self.logistics
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.spu_count:
            if hasattr(self.spu_count, 'to_alipay_dict'):
                params['spu_count'] = self.spu_count.to_alipay_dict()
            else:
                params['spu_count'] = self.spu_count
        if self.spus:
            if isinstance(self.spus, list):
                for i in range(0, len(self.spus)):
                    element = self.spus[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.spus[i] = element.to_alipay_dict()
            if hasattr(self.spus, 'to_alipay_dict'):
                params['spus'] = self.spus.to_alipay_dict()
            else:
                params['spus'] = self.spus
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_status:
            if hasattr(self.sub_status, 'to_alipay_dict'):
                params['sub_status'] = self.sub_status.to_alipay_dict()
            else:
                params['sub_status'] = self.sub_status
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
        o = AlipayIserviceCcmSwOrderSyncModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'link_url' in d:
            o.link_url = d['link_url']
        if 'logistic_count' in d:
            o.logistic_count = d['logistic_count']
        if 'logistics' in d:
            o.logistics = d['logistics']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'spu_count' in d:
            o.spu_count = d['spu_count']
        if 'spus' in d:
            o.spus = d['spus']
        if 'status' in d:
            o.status = d['status']
        if 'sub_status' in d:
            o.sub_status = d['sub_status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


