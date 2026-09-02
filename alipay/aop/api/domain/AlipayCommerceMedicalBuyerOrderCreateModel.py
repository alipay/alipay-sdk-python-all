#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemInfos import ItemInfos
from alipay.aop.api.domain.ServicePackageInfo import ServicePackageInfo


class AlipayCommerceMedicalBuyerOrderCreateModel(object):

    def __init__(self):
        self._app_type = None
        self._fulfillment_no = None
        self._items = None
        self._patient_id = None
        self._seller = None
        self._service_package = None
        self._source = None
        self._store_id = None

    @property
    def app_type(self):
        return self._app_type

    @app_type.setter
    def app_type(self, value):
        self._app_type = value
    @property
    def fulfillment_no(self):
        return self._fulfillment_no

    @fulfillment_no.setter
    def fulfillment_no(self, value):
        self._fulfillment_no = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, ItemInfos):
                    self._items.append(i)
                else:
                    self._items.append(ItemInfos.from_alipay_dict(i))
    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value
    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        self._seller = value
    @property
    def service_package(self):
        return self._service_package

    @service_package.setter
    def service_package(self, value):
        if isinstance(value, ServicePackageInfo):
            self._service_package = value
        else:
            self._service_package = ServicePackageInfo.from_alipay_dict(value)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_type:
            if hasattr(self.app_type, 'to_alipay_dict'):
                params['app_type'] = self.app_type.to_alipay_dict()
            else:
                params['app_type'] = self.app_type
        if self.fulfillment_no:
            if hasattr(self.fulfillment_no, 'to_alipay_dict'):
                params['fulfillment_no'] = self.fulfillment_no.to_alipay_dict()
            else:
                params['fulfillment_no'] = self.fulfillment_no
        if self.items:
            if isinstance(self.items, list):
                for i in range(0, len(self.items)):
                    element = self.items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.items[i] = element.to_alipay_dict()
            if hasattr(self.items, 'to_alipay_dict'):
                params['items'] = self.items.to_alipay_dict()
            else:
                params['items'] = self.items
        if self.patient_id:
            if hasattr(self.patient_id, 'to_alipay_dict'):
                params['patient_id'] = self.patient_id.to_alipay_dict()
            else:
                params['patient_id'] = self.patient_id
        if self.seller:
            if hasattr(self.seller, 'to_alipay_dict'):
                params['seller'] = self.seller.to_alipay_dict()
            else:
                params['seller'] = self.seller
        if self.service_package:
            if hasattr(self.service_package, 'to_alipay_dict'):
                params['service_package'] = self.service_package.to_alipay_dict()
            else:
                params['service_package'] = self.service_package
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalBuyerOrderCreateModel()
        if 'app_type' in d:
            o.app_type = d['app_type']
        if 'fulfillment_no' in d:
            o.fulfillment_no = d['fulfillment_no']
        if 'items' in d:
            o.items = d['items']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        if 'seller' in d:
            o.seller = d['seller']
        if 'service_package' in d:
            o.service_package = d['service_package']
        if 'source' in d:
            o.source = d['source']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


