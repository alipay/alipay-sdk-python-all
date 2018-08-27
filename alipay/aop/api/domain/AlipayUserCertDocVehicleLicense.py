#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCertDocVehicleLicense(object):

    def __init__(self):
        self._encoded_img_main = None
        self._encoded_img_vice = None
        self._engine_no = None
        self._issue_date = None
        self._model = None
        self._owner = None
        self._plate_no = None
        self._register_date = None
        self._vin = None

    @property
    def encoded_img_main(self):
        return self._encoded_img_main

    @encoded_img_main.setter
    def encoded_img_main(self, value):
        self._encoded_img_main = value
    @property
    def encoded_img_vice(self):
        return self._encoded_img_vice

    @encoded_img_vice.setter
    def encoded_img_vice(self, value):
        self._encoded_img_vice = value
    @property
    def engine_no(self):
        return self._engine_no

    @engine_no.setter
    def engine_no(self, value):
        self._engine_no = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        self._vin = value


    def to_alipay_dict(self):
        params = dict()
        if self.encoded_img_main:
            if hasattr(self.encoded_img_main, 'to_alipay_dict'):
                params['encoded_img_main'] = self.encoded_img_main.to_alipay_dict()
            else:
                params['encoded_img_main'] = self.encoded_img_main
        if self.encoded_img_vice:
            if hasattr(self.encoded_img_vice, 'to_alipay_dict'):
                params['encoded_img_vice'] = self.encoded_img_vice.to_alipay_dict()
            else:
                params['encoded_img_vice'] = self.encoded_img_vice
        if self.engine_no:
            if hasattr(self.engine_no, 'to_alipay_dict'):
                params['engine_no'] = self.engine_no.to_alipay_dict()
            else:
                params['engine_no'] = self.engine_no
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
        if self.model:
            if hasattr(self.model, 'to_alipay_dict'):
                params['model'] = self.model.to_alipay_dict()
            else:
                params['model'] = self.model
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
        if self.vin:
            if hasattr(self.vin, 'to_alipay_dict'):
                params['vin'] = self.vin.to_alipay_dict()
            else:
                params['vin'] = self.vin
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCertDocVehicleLicense()
        if 'encoded_img_main' in d:
            o.encoded_img_main = d['encoded_img_main']
        if 'encoded_img_vice' in d:
            o.encoded_img_vice = d['encoded_img_vice']
        if 'engine_no' in d:
            o.engine_no = d['engine_no']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'model' in d:
            o.model = d['model']
        if 'owner' in d:
            o.owner = d['owner']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'vin' in d:
            o.vin = d['vin']
        return o


