#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LegalRepresentativeInfo(object):

    def __init__(self):
        self._legal_representative_cert_indate = None
        self._legal_representative_cert_no = None
        self._legal_representative_cert_pic_back = None
        self._legal_representative_cert_pic_front = None
        self._legal_representative_cert_type = None
        self._legal_representative_name = None

    @property
    def legal_representative_cert_indate(self):
        return self._legal_representative_cert_indate

    @legal_representative_cert_indate.setter
    def legal_representative_cert_indate(self, value):
        self._legal_representative_cert_indate = value
    @property
    def legal_representative_cert_no(self):
        return self._legal_representative_cert_no

    @legal_representative_cert_no.setter
    def legal_representative_cert_no(self, value):
        self._legal_representative_cert_no = value
    @property
    def legal_representative_cert_pic_back(self):
        return self._legal_representative_cert_pic_back

    @legal_representative_cert_pic_back.setter
    def legal_representative_cert_pic_back(self, value):
        self._legal_representative_cert_pic_back = value
    @property
    def legal_representative_cert_pic_front(self):
        return self._legal_representative_cert_pic_front

    @legal_representative_cert_pic_front.setter
    def legal_representative_cert_pic_front(self, value):
        self._legal_representative_cert_pic_front = value
    @property
    def legal_representative_cert_type(self):
        return self._legal_representative_cert_type

    @legal_representative_cert_type.setter
    def legal_representative_cert_type(self, value):
        self._legal_representative_cert_type = value
    @property
    def legal_representative_name(self):
        return self._legal_representative_name

    @legal_representative_name.setter
    def legal_representative_name(self, value):
        self._legal_representative_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.legal_representative_cert_indate:
            if hasattr(self.legal_representative_cert_indate, 'to_alipay_dict'):
                params['legal_representative_cert_indate'] = self.legal_representative_cert_indate.to_alipay_dict()
            else:
                params['legal_representative_cert_indate'] = self.legal_representative_cert_indate
        if self.legal_representative_cert_no:
            if hasattr(self.legal_representative_cert_no, 'to_alipay_dict'):
                params['legal_representative_cert_no'] = self.legal_representative_cert_no.to_alipay_dict()
            else:
                params['legal_representative_cert_no'] = self.legal_representative_cert_no
        if self.legal_representative_cert_pic_back:
            if hasattr(self.legal_representative_cert_pic_back, 'to_alipay_dict'):
                params['legal_representative_cert_pic_back'] = self.legal_representative_cert_pic_back.to_alipay_dict()
            else:
                params['legal_representative_cert_pic_back'] = self.legal_representative_cert_pic_back
        if self.legal_representative_cert_pic_front:
            if hasattr(self.legal_representative_cert_pic_front, 'to_alipay_dict'):
                params['legal_representative_cert_pic_front'] = self.legal_representative_cert_pic_front.to_alipay_dict()
            else:
                params['legal_representative_cert_pic_front'] = self.legal_representative_cert_pic_front
        if self.legal_representative_cert_type:
            if hasattr(self.legal_representative_cert_type, 'to_alipay_dict'):
                params['legal_representative_cert_type'] = self.legal_representative_cert_type.to_alipay_dict()
            else:
                params['legal_representative_cert_type'] = self.legal_representative_cert_type
        if self.legal_representative_name:
            if hasattr(self.legal_representative_name, 'to_alipay_dict'):
                params['legal_representative_name'] = self.legal_representative_name.to_alipay_dict()
            else:
                params['legal_representative_name'] = self.legal_representative_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LegalRepresentativeInfo()
        if 'legal_representative_cert_indate' in d:
            o.legal_representative_cert_indate = d['legal_representative_cert_indate']
        if 'legal_representative_cert_no' in d:
            o.legal_representative_cert_no = d['legal_representative_cert_no']
        if 'legal_representative_cert_pic_back' in d:
            o.legal_representative_cert_pic_back = d['legal_representative_cert_pic_back']
        if 'legal_representative_cert_pic_front' in d:
            o.legal_representative_cert_pic_front = d['legal_representative_cert_pic_front']
        if 'legal_representative_cert_type' in d:
            o.legal_representative_cert_type = d['legal_representative_cert_type']
        if 'legal_representative_name' in d:
            o.legal_representative_name = d['legal_representative_name']
        return o


