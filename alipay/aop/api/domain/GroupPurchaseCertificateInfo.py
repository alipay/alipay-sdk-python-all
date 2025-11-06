#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupPurchaseCertificateInfo(object):

    def __init__(self):
        self._legal_back_pic = None
        self._legal_end_time = None
        self._legal_front_pic = None
        self._legal_name = None
        self._legal_no = None

    @property
    def legal_back_pic(self):
        return self._legal_back_pic

    @legal_back_pic.setter
    def legal_back_pic(self, value):
        self._legal_back_pic = value
    @property
    def legal_end_time(self):
        return self._legal_end_time

    @legal_end_time.setter
    def legal_end_time(self, value):
        self._legal_end_time = value
    @property
    def legal_front_pic(self):
        return self._legal_front_pic

    @legal_front_pic.setter
    def legal_front_pic(self, value):
        self._legal_front_pic = value
    @property
    def legal_name(self):
        return self._legal_name

    @legal_name.setter
    def legal_name(self, value):
        self._legal_name = value
    @property
    def legal_no(self):
        return self._legal_no

    @legal_no.setter
    def legal_no(self, value):
        self._legal_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.legal_back_pic:
            if hasattr(self.legal_back_pic, 'to_alipay_dict'):
                params['legal_back_pic'] = self.legal_back_pic.to_alipay_dict()
            else:
                params['legal_back_pic'] = self.legal_back_pic
        if self.legal_end_time:
            if hasattr(self.legal_end_time, 'to_alipay_dict'):
                params['legal_end_time'] = self.legal_end_time.to_alipay_dict()
            else:
                params['legal_end_time'] = self.legal_end_time
        if self.legal_front_pic:
            if hasattr(self.legal_front_pic, 'to_alipay_dict'):
                params['legal_front_pic'] = self.legal_front_pic.to_alipay_dict()
            else:
                params['legal_front_pic'] = self.legal_front_pic
        if self.legal_name:
            if hasattr(self.legal_name, 'to_alipay_dict'):
                params['legal_name'] = self.legal_name.to_alipay_dict()
            else:
                params['legal_name'] = self.legal_name
        if self.legal_no:
            if hasattr(self.legal_no, 'to_alipay_dict'):
                params['legal_no'] = self.legal_no.to_alipay_dict()
            else:
                params['legal_no'] = self.legal_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupPurchaseCertificateInfo()
        if 'legal_back_pic' in d:
            o.legal_back_pic = d['legal_back_pic']
        if 'legal_end_time' in d:
            o.legal_end_time = d['legal_end_time']
        if 'legal_front_pic' in d:
            o.legal_front_pic = d['legal_front_pic']
        if 'legal_name' in d:
            o.legal_name = d['legal_name']
        if 'legal_no' in d:
            o.legal_no = d['legal_no']
        return o


