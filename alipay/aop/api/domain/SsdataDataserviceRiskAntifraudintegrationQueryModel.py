#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceRiskAntifraudintegrationQueryModel(object):

    def __init__(self):
        self._address = None
        self._bank_card = None
        self._cert_no = None
        self._cert_type = None
        self._email = None
        self._imei = None
        self._ip = None
        self._mac = None
        self._mobile = None
        self._name = None
        self._partner_id = None
        self._wifimac = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def bank_card(self):
        return self._bank_card

    @bank_card.setter
    def bank_card(self, value):
        self._bank_card = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def imei(self):
        return self._imei

    @imei.setter
    def imei(self, value):
        self._imei = value
    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value
    @property
    def mac(self):
        return self._mac

    @mac.setter
    def mac(self, value):
        self._mac = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def wifimac(self):
        return self._wifimac

    @wifimac.setter
    def wifimac(self, value):
        self._wifimac = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.bank_card:
            if hasattr(self.bank_card, 'to_alipay_dict'):
                params['bank_card'] = self.bank_card.to_alipay_dict()
            else:
                params['bank_card'] = self.bank_card
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.imei:
            if hasattr(self.imei, 'to_alipay_dict'):
                params['imei'] = self.imei.to_alipay_dict()
            else:
                params['imei'] = self.imei
        if self.ip:
            if hasattr(self.ip, 'to_alipay_dict'):
                params['ip'] = self.ip.to_alipay_dict()
            else:
                params['ip'] = self.ip
        if self.mac:
            if hasattr(self.mac, 'to_alipay_dict'):
                params['mac'] = self.mac.to_alipay_dict()
            else:
                params['mac'] = self.mac
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.wifimac:
            if hasattr(self.wifimac, 'to_alipay_dict'):
                params['wifimac'] = self.wifimac.to_alipay_dict()
            else:
                params['wifimac'] = self.wifimac
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceRiskAntifraudintegrationQueryModel()
        if 'address' in d:
            o.address = d['address']
        if 'bank_card' in d:
            o.bank_card = d['bank_card']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'email' in d:
            o.email = d['email']
        if 'imei' in d:
            o.imei = d['imei']
        if 'ip' in d:
            o.ip = d['ip']
        if 'mac' in d:
            o.mac = d['mac']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'wifimac' in d:
            o.wifimac = d['wifimac']
        return o


