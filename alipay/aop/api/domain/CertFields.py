#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertFields(object):

    def __init__(self):
        self._address = None
        self._birth = None
        self._certno = None
        self._expires = None
        self._expiresend = None
        self._expiresstart = None
        self._issuingauthority = None
        self._name = None
        self._number = None
        self._race = None
        self._renewalnum = None
        self._sex = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value
    @property
    def certno(self):
        return self._certno

    @certno.setter
    def certno(self, value):
        self._certno = value
    @property
    def expires(self):
        return self._expires

    @expires.setter
    def expires(self, value):
        self._expires = value
    @property
    def expiresend(self):
        return self._expiresend

    @expiresend.setter
    def expiresend(self, value):
        self._expiresend = value
    @property
    def expiresstart(self):
        return self._expiresstart

    @expiresstart.setter
    def expiresstart(self, value):
        self._expiresstart = value
    @property
    def issuingauthority(self):
        return self._issuingauthority

    @issuingauthority.setter
    def issuingauthority(self, value):
        self._issuingauthority = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, value):
        self._race = value
    @property
    def renewalnum(self):
        return self._renewalnum

    @renewalnum.setter
    def renewalnum(self, value):
        self._renewalnum = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.birth:
            if hasattr(self.birth, 'to_alipay_dict'):
                params['birth'] = self.birth.to_alipay_dict()
            else:
                params['birth'] = self.birth
        if self.certno:
            if hasattr(self.certno, 'to_alipay_dict'):
                params['certno'] = self.certno.to_alipay_dict()
            else:
                params['certno'] = self.certno
        if self.expires:
            if hasattr(self.expires, 'to_alipay_dict'):
                params['expires'] = self.expires.to_alipay_dict()
            else:
                params['expires'] = self.expires
        if self.expiresend:
            if hasattr(self.expiresend, 'to_alipay_dict'):
                params['expiresend'] = self.expiresend.to_alipay_dict()
            else:
                params['expiresend'] = self.expiresend
        if self.expiresstart:
            if hasattr(self.expiresstart, 'to_alipay_dict'):
                params['expiresstart'] = self.expiresstart.to_alipay_dict()
            else:
                params['expiresstart'] = self.expiresstart
        if self.issuingauthority:
            if hasattr(self.issuingauthority, 'to_alipay_dict'):
                params['issuingauthority'] = self.issuingauthority.to_alipay_dict()
            else:
                params['issuingauthority'] = self.issuingauthority
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.number:
            if hasattr(self.number, 'to_alipay_dict'):
                params['number'] = self.number.to_alipay_dict()
            else:
                params['number'] = self.number
        if self.race:
            if hasattr(self.race, 'to_alipay_dict'):
                params['race'] = self.race.to_alipay_dict()
            else:
                params['race'] = self.race
        if self.renewalnum:
            if hasattr(self.renewalnum, 'to_alipay_dict'):
                params['renewalnum'] = self.renewalnum.to_alipay_dict()
            else:
                params['renewalnum'] = self.renewalnum
        if self.sex:
            if hasattr(self.sex, 'to_alipay_dict'):
                params['sex'] = self.sex.to_alipay_dict()
            else:
                params['sex'] = self.sex
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertFields()
        if 'address' in d:
            o.address = d['address']
        if 'birth' in d:
            o.birth = d['birth']
        if 'certno' in d:
            o.certno = d['certno']
        if 'expires' in d:
            o.expires = d['expires']
        if 'expiresend' in d:
            o.expiresend = d['expiresend']
        if 'expiresstart' in d:
            o.expiresstart = d['expiresstart']
        if 'issuingauthority' in d:
            o.issuingauthority = d['issuingauthority']
        if 'name' in d:
            o.name = d['name']
        if 'number' in d:
            o.number = d['number']
        if 'race' in d:
            o.race = d['race']
        if 'renewalnum' in d:
            o.renewalnum = d['renewalnum']
        if 'sex' in d:
            o.sex = d['sex']
        return o


