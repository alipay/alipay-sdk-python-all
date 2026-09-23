#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalRightUrlQueryModel(object):

    def __init__(self):
        self._fulfillment_no = None
        self._service_item_id = None
        self._service_package_order_no = None

    @property
    def fulfillment_no(self):
        return self._fulfillment_no

    @fulfillment_no.setter
    def fulfillment_no(self, value):
        self._fulfillment_no = value
    @property
    def service_item_id(self):
        return self._service_item_id

    @service_item_id.setter
    def service_item_id(self, value):
        self._service_item_id = value
    @property
    def service_package_order_no(self):
        return self._service_package_order_no

    @service_package_order_no.setter
    def service_package_order_no(self, value):
        self._service_package_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.fulfillment_no:
            if hasattr(self.fulfillment_no, 'to_alipay_dict'):
                params['fulfillment_no'] = self.fulfillment_no.to_alipay_dict()
            else:
                params['fulfillment_no'] = self.fulfillment_no
        if self.service_item_id:
            if hasattr(self.service_item_id, 'to_alipay_dict'):
                params['service_item_id'] = self.service_item_id.to_alipay_dict()
            else:
                params['service_item_id'] = self.service_item_id
        if self.service_package_order_no:
            if hasattr(self.service_package_order_no, 'to_alipay_dict'):
                params['service_package_order_no'] = self.service_package_order_no.to_alipay_dict()
            else:
                params['service_package_order_no'] = self.service_package_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalRightUrlQueryModel()
        if 'fulfillment_no' in d:
            o.fulfillment_no = d['fulfillment_no']
        if 'service_item_id' in d:
            o.service_item_id = d['service_item_id']
        if 'service_package_order_no' in d:
            o.service_package_order_no = d['service_package_order_no']
        return o


