#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantApplyItemInfo import MerchantApplyItemInfo
from alipay.aop.api.domain.MerchantApplyPerformRecordInfo import MerchantApplyPerformRecordInfo


class MerchantApplyInfo(object):

    def __init__(self):
        self._applier = None
        self._id = None
        self._item_infos = None
        self._perform_record_infos = None
        self._status = None

    @property
    def applier(self):
        return self._applier

    @applier.setter
    def applier(self, value):
        self._applier = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, list):
            self._item_infos = list()
            for i in value:
                if isinstance(i, MerchantApplyItemInfo):
                    self._item_infos.append(i)
                else:
                    self._item_infos.append(MerchantApplyItemInfo.from_alipay_dict(i))
    @property
    def perform_record_infos(self):
        return self._perform_record_infos

    @perform_record_infos.setter
    def perform_record_infos(self, value):
        if isinstance(value, list):
            self._perform_record_infos = list()
            for i in value:
                if isinstance(i, MerchantApplyPerformRecordInfo):
                    self._perform_record_infos.append(i)
                else:
                    self._perform_record_infos.append(MerchantApplyPerformRecordInfo.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.applier:
            if hasattr(self.applier, 'to_alipay_dict'):
                params['applier'] = self.applier.to_alipay_dict()
            else:
                params['applier'] = self.applier
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.item_infos:
            if isinstance(self.item_infos, list):
                for i in range(0, len(self.item_infos)):
                    element = self.item_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_infos[i] = element.to_alipay_dict()
            if hasattr(self.item_infos, 'to_alipay_dict'):
                params['item_infos'] = self.item_infos.to_alipay_dict()
            else:
                params['item_infos'] = self.item_infos
        if self.perform_record_infos:
            if isinstance(self.perform_record_infos, list):
                for i in range(0, len(self.perform_record_infos)):
                    element = self.perform_record_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.perform_record_infos[i] = element.to_alipay_dict()
            if hasattr(self.perform_record_infos, 'to_alipay_dict'):
                params['perform_record_infos'] = self.perform_record_infos.to_alipay_dict()
            else:
                params['perform_record_infos'] = self.perform_record_infos
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
        o = MerchantApplyInfo()
        if 'applier' in d:
            o.applier = d['applier']
        if 'id' in d:
            o.id = d['id']
        if 'item_infos' in d:
            o.item_infos = d['item_infos']
        if 'perform_record_infos' in d:
            o.perform_record_infos = d['perform_record_infos']
        if 'status' in d:
            o.status = d['status']
        return o


