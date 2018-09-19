#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExproductconfResponse(object):

    def __init__(self):
        self._charge_inst = None
        self._chargeinst_name = None
        self._chargeoff_inst = None
        self._chargeoffinst_name = None
        self._city = None
        self._extend = None
        self._province = None
        self._status = None

    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def chargeinst_name(self):
        return self._chargeinst_name

    @chargeinst_name.setter
    def chargeinst_name(self, value):
        self._chargeinst_name = value
    @property
    def chargeoff_inst(self):
        return self._chargeoff_inst

    @chargeoff_inst.setter
    def chargeoff_inst(self, value):
        self._chargeoff_inst = value
    @property
    def chargeoffinst_name(self):
        return self._chargeoffinst_name

    @chargeoffinst_name.setter
    def chargeoffinst_name(self, value):
        self._chargeoffinst_name = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def extend(self):
        return self._extend

    @extend.setter
    def extend(self, value):
        self._extend = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = self.charge_inst.to_alipay_dict()
            else:
                params['charge_inst'] = self.charge_inst
        if self.chargeinst_name:
            if hasattr(self.chargeinst_name, 'to_alipay_dict'):
                params['chargeinst_name'] = self.chargeinst_name.to_alipay_dict()
            else:
                params['chargeinst_name'] = self.chargeinst_name
        if self.chargeoff_inst:
            if hasattr(self.chargeoff_inst, 'to_alipay_dict'):
                params['chargeoff_inst'] = self.chargeoff_inst.to_alipay_dict()
            else:
                params['chargeoff_inst'] = self.chargeoff_inst
        if self.chargeoffinst_name:
            if hasattr(self.chargeoffinst_name, 'to_alipay_dict'):
                params['chargeoffinst_name'] = self.chargeoffinst_name.to_alipay_dict()
            else:
                params['chargeoffinst_name'] = self.chargeoffinst_name
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.extend:
            if hasattr(self.extend, 'to_alipay_dict'):
                params['extend'] = self.extend.to_alipay_dict()
            else:
                params['extend'] = self.extend
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
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
        o = ExproductconfResponse()
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'chargeinst_name' in d:
            o.chargeinst_name = d['chargeinst_name']
        if 'chargeoff_inst' in d:
            o.chargeoff_inst = d['chargeoff_inst']
        if 'chargeoffinst_name' in d:
            o.chargeoffinst_name = d['chargeoffinst_name']
        if 'city' in d:
            o.city = d['city']
        if 'extend' in d:
            o.extend = d['extend']
        if 'province' in d:
            o.province = d['province']
        if 'status' in d:
            o.status = d['status']
        return o


