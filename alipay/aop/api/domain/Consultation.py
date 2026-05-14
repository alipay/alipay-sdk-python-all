#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Consultation(object):

    def __init__(self):
        self._app_type = None
        self._channel = None
        self._doctor_id = None
        self._fulfillable = None
        self._fulfillment_id = None
        self._fulfillment_status = None
        self._item_code = None
        self._patient_id = None
        self._service_item_id = None
        self._service_package_id = None
        self._service_package_name = None

    @property
    def app_type(self):
        return self._app_type

    @app_type.setter
    def app_type(self, value):
        self._app_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def fulfillable(self):
        return self._fulfillable

    @fulfillable.setter
    def fulfillable(self, value):
        self._fulfillable = value
    @property
    def fulfillment_id(self):
        return self._fulfillment_id

    @fulfillment_id.setter
    def fulfillment_id(self, value):
        self._fulfillment_id = value
    @property
    def fulfillment_status(self):
        return self._fulfillment_status

    @fulfillment_status.setter
    def fulfillment_status(self, value):
        self._fulfillment_status = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value
    @property
    def service_item_id(self):
        return self._service_item_id

    @service_item_id.setter
    def service_item_id(self, value):
        self._service_item_id = value
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
        if self.app_type:
            if hasattr(self.app_type, 'to_alipay_dict'):
                params['app_type'] = self.app_type.to_alipay_dict()
            else:
                params['app_type'] = self.app_type
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.fulfillable:
            if hasattr(self.fulfillable, 'to_alipay_dict'):
                params['fulfillable'] = self.fulfillable.to_alipay_dict()
            else:
                params['fulfillable'] = self.fulfillable
        if self.fulfillment_id:
            if hasattr(self.fulfillment_id, 'to_alipay_dict'):
                params['fulfillment_id'] = self.fulfillment_id.to_alipay_dict()
            else:
                params['fulfillment_id'] = self.fulfillment_id
        if self.fulfillment_status:
            if hasattr(self.fulfillment_status, 'to_alipay_dict'):
                params['fulfillment_status'] = self.fulfillment_status.to_alipay_dict()
            else:
                params['fulfillment_status'] = self.fulfillment_status
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.patient_id:
            if hasattr(self.patient_id, 'to_alipay_dict'):
                params['patient_id'] = self.patient_id.to_alipay_dict()
            else:
                params['patient_id'] = self.patient_id
        if self.service_item_id:
            if hasattr(self.service_item_id, 'to_alipay_dict'):
                params['service_item_id'] = self.service_item_id.to_alipay_dict()
            else:
                params['service_item_id'] = self.service_item_id
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
        o = Consultation()
        if 'app_type' in d:
            o.app_type = d['app_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'fulfillable' in d:
            o.fulfillable = d['fulfillable']
        if 'fulfillment_id' in d:
            o.fulfillment_id = d['fulfillment_id']
        if 'fulfillment_status' in d:
            o.fulfillment_status = d['fulfillment_status']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        if 'service_item_id' in d:
            o.service_item_id = d['service_item_id']
        if 'service_package_id' in d:
            o.service_package_id = d['service_package_id']
        if 'service_package_name' in d:
            o.service_package_name = d['service_package_name']
        return o


