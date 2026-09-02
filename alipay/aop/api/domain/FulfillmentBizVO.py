#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExaminationItemVO import ExaminationItemVO
from alipay.aop.api.domain.FulfillmentBizPatientInfo import FulfillmentBizPatientInfo


class FulfillmentBizVO(object):

    def __init__(self):
        self._fulfillment_no = None
        self._fulfillment_status = None
        self._fulfillment_status_desc = None
        self._fulfillment_type = None
        self._items = None
        self._patient_infos = None
        self._service_package_id = None
        self._service_package_name = None

    @property
    def fulfillment_no(self):
        return self._fulfillment_no

    @fulfillment_no.setter
    def fulfillment_no(self, value):
        self._fulfillment_no = value
    @property
    def fulfillment_status(self):
        return self._fulfillment_status

    @fulfillment_status.setter
    def fulfillment_status(self, value):
        self._fulfillment_status = value
    @property
    def fulfillment_status_desc(self):
        return self._fulfillment_status_desc

    @fulfillment_status_desc.setter
    def fulfillment_status_desc(self, value):
        self._fulfillment_status_desc = value
    @property
    def fulfillment_type(self):
        return self._fulfillment_type

    @fulfillment_type.setter
    def fulfillment_type(self, value):
        self._fulfillment_type = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, ExaminationItemVO):
                    self._items.append(i)
                else:
                    self._items.append(ExaminationItemVO.from_alipay_dict(i))
    @property
    def patient_infos(self):
        return self._patient_infos

    @patient_infos.setter
    def patient_infos(self, value):
        if isinstance(value, list):
            self._patient_infos = list()
            for i in value:
                if isinstance(i, FulfillmentBizPatientInfo):
                    self._patient_infos.append(i)
                else:
                    self._patient_infos.append(FulfillmentBizPatientInfo.from_alipay_dict(i))
    @property
    def service_package_id(self):
        return self._service_package_id

    @service_package_id.setter
    def service_package_id(self, value):
        self._service_package_id = value
    @property
    def service_package_name(self):
        return self._service_package_name

    @service_package_name.setter
    def service_package_name(self, value):
        self._service_package_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.fulfillment_no:
            if hasattr(self.fulfillment_no, 'to_alipay_dict'):
                params['fulfillment_no'] = self.fulfillment_no.to_alipay_dict()
            else:
                params['fulfillment_no'] = self.fulfillment_no
        if self.fulfillment_status:
            if hasattr(self.fulfillment_status, 'to_alipay_dict'):
                params['fulfillment_status'] = self.fulfillment_status.to_alipay_dict()
            else:
                params['fulfillment_status'] = self.fulfillment_status
        if self.fulfillment_status_desc:
            if hasattr(self.fulfillment_status_desc, 'to_alipay_dict'):
                params['fulfillment_status_desc'] = self.fulfillment_status_desc.to_alipay_dict()
            else:
                params['fulfillment_status_desc'] = self.fulfillment_status_desc
        if self.fulfillment_type:
            if hasattr(self.fulfillment_type, 'to_alipay_dict'):
                params['fulfillment_type'] = self.fulfillment_type.to_alipay_dict()
            else:
                params['fulfillment_type'] = self.fulfillment_type
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
        if self.patient_infos:
            if isinstance(self.patient_infos, list):
                for i in range(0, len(self.patient_infos)):
                    element = self.patient_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.patient_infos[i] = element.to_alipay_dict()
            if hasattr(self.patient_infos, 'to_alipay_dict'):
                params['patient_infos'] = self.patient_infos.to_alipay_dict()
            else:
                params['patient_infos'] = self.patient_infos
        if self.service_package_id:
            if hasattr(self.service_package_id, 'to_alipay_dict'):
                params['service_package_id'] = self.service_package_id.to_alipay_dict()
            else:
                params['service_package_id'] = self.service_package_id
        if self.service_package_name:
            if hasattr(self.service_package_name, 'to_alipay_dict'):
                params['service_package_name'] = self.service_package_name.to_alipay_dict()
            else:
                params['service_package_name'] = self.service_package_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FulfillmentBizVO()
        if 'fulfillment_no' in d:
            o.fulfillment_no = d['fulfillment_no']
        if 'fulfillment_status' in d:
            o.fulfillment_status = d['fulfillment_status']
        if 'fulfillment_status_desc' in d:
            o.fulfillment_status_desc = d['fulfillment_status_desc']
        if 'fulfillment_type' in d:
            o.fulfillment_type = d['fulfillment_type']
        if 'items' in d:
            o.items = d['items']
        if 'patient_infos' in d:
            o.patient_infos = d['patient_infos']
        if 'service_package_id' in d:
            o.service_package_id = d['service_package_id']
        if 'service_package_name' in d:
            o.service_package_name = d['service_package_name']
        return o


